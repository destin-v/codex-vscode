---
icon: material/microsoft-visual-studio-code
---

# :material-microsoft-visual-studio-code: VSCode

This is a compilation of configuration settings, extensions, and add-on recommended for development using VSCode.

## 📦 Recommended Extensions

??? note "Languages"

    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)


??? note "Docs"

    * [Automatic Doc String](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
    * [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
    * [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)


??? note "Formatting"

    * [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
    * [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)


??? note "Testing"

    * [Python Test Explorer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
    * [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)


??? note "Configuration Control"

    * [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

??? note "Containers"

    * [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    * [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

??? note "Remote"

    * [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
    * [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
    * [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)


??? note "Misc"

    * [Back & Forth](https://marketplace.visualstudio.com/items?itemName=nick-rudenko.back-n-forth)
    * [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

## 🅰 Fonts
You will need to install [**MesloLGLDZ Nerd Font**](https://www.nerdfonts.com/).  This will be used to display glyphs and icons for all of your terminals.

## ✨ Theme
To customize your themes you need to set them in your settings.json file.  To identify items you want to change in the editor, you will have to use the inspector:

++cmd+shift+p++ › **Inspect Editor Tokens and Scopes**

This feature allows you to view the settings and scope of any item in your editor.  Once you have identified the item you want to change, go to the `settings.json` and make the desired modifications.

## 🗂️ Tab Removal
In general you should never need to have tabs.  VSCode provides an ordered list of all files and windows you have opened sorted alphabetically.  This is a much better way of accessing files.

* ++cmd+p++     # shows all tabs
* Settings › Workbench › Editor: Show Tabs [OFF]

## 🔧 Troubleshooting

??? note "TestExplorer UI"

    To have TestExplorer UI properly detect your tests by pressing and selecting:

    * ++cmd+shift+p++ › Python: Configure Tests › Pytests › <target_dir>

    For a full explanation on how to properly set up the TestExplorer UI see [**here**](https://graycode.ie/blog/how-to-set-up-testing-explorer-with-python-pytest-in-vscode/).

??? note "SSH FileLocking"

    If performing remote development you may need to configure your file locking parameters depending on whether it is allowed on the host:

    * Settings › Remote.SSH: Lockfiles In Tmp [ON]
    * Settings › Remote.SSH: useFlock [OFF]
    * ++cmd+shift+p++ › Remote-SSH: Kill VSCode Server on Host...

    This will disable file locking and restart the remote VSCode host.  You will have to download all of your extensions once it reconnects with the server.



## 📚 References:
* https://stackoverflow.com/questions/57024732/how-can-i-customize-python-syntax-highlighting-in-vs-code
* https://www.alveeakand.com/how-to-modify-themes-in-vscode/
