UndoCloseTabs
=============


UndoCloseTabs is a Sublime Text 2/3 plugin that works just like chrome's undo close tab command.




Sponsors
-----
No sponsors yet.. :(

If you like the software, don't forget to donate to further development of it!

[![PayPal donate button](https://www.paypalobjects.com/webstatic/en_US/btn/btn_donate_pp_142x27.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=redhatboson@gmail.com&item_name=Donation_to_Sublime_Text_ UndoCloseTabs&item_number=1&no_shipping=1 "Donate to this project using Paypal")


Installing
----------
**With the Package Control plugin:** The easiest way to install UndoCloseTab is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart Sublime Text and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select UndoCloseTabs when the list appears. The advantage of using this method is that Package Control will automatically keep UndoCloseTabs up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/scriptburn/sublimetext-undoclosetabs) and copy the UndoCloseTabs folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/scriptburn/sublimetext-undoclosetabs.git UndoCloseTabs


The "Packages" directory is located at:

* OS X:

        ST2: ~/Library/Application Support/Sublime Text 2/Packages/
        ST3: ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ST2: ~/.config/sublime-text-2/Packages/
        ST3: ~/.config/sublime-text-3/Packages/

* Windows:

        ST2: %APPDATA%/Sublime Text 2/Packages/
        ST3: %APPDATA%/Sublime Text 3/Packages/




Usage
-----

You can set up your own key combo for this, by going to Preferences -> Key Bindings - User, and adding a command in that huge array: `{ "keys": ["ctrl+shift+t"], "command": "scb_undo_tab" },`. Default keybinding is `ctrl+shift+t`. You can use any other key you want, thought most of them are already taken.


Pull requests are welcome.

Troubleshooting
---------------
If you like living on the edge, please report any bugs you find on the [UndoCloseTabs issues](https://github.com/scriptburn/sublimetext-undoclosetabs/issues) page.
