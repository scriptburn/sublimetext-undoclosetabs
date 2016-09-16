
import os
import sys
import sublime
import sublime_plugin


class ScbStack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


ScbStackData = ScbStack()


class ScbUndoTabCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global ScbStackData
        debug_write("UndoTabCommand stack  " +
                    ('empty' if ScbStackData.isEmpty() else ''))
        if not ScbStackData.isEmpty():
            pop = ScbStackData.peek()
            scb_debug_write("peek " + pop)
            window = sublime.active_window()
            window_id = window.id()
            if pop != None:
                window.open_file(ScbStackData.pop(),
                                 sublime.ENCODED_POSITION)


class UndoTabEventListener(sublime_plugin.EventListener):

    def on_close(self, view):
        global ScbStackData
        scb_debug_write("Adding to statck " +
                        ('none' if None == view.file_name() else view.file_name()))
        if view.file_name() != None:
            view_sel = view.sel()
            row, col = view.rowcol(view_sel[0].begin())
            current_location = "%s:%d" % (view.file_name(), row + 1)

            ScbStack.push(ScbStackData, current_location)


def scb_debug_write(text, prefix=False):
    sys.stdout.write(text + "\n")
