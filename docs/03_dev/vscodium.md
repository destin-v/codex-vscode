---
icon: simple/vscodium
---

# :simple-vscodium: VsCodium

This is a compilation of configuration settings, extensions, and add-on recommended for development using VSCodium.

## 📦 Recommended Extensions
<div class="grid cards" markdown>

-   #### Format/Lint

    ---
    * [Ruff](https://open-vsx.org/extension/charliermarsh/ruff)

-   #### Testing

    ---
    * [Python Test Explorer](https://open-vsx.org/extension/littlefoxteam/vscode-python-test-adapter)

-   #### Version Control

    ---
    * [Git Graph](https://open-vsx.org/extension/mhutchie/git-graph)

-   #### Containers

    ---
    * [Docker](https://open-vsx.org/extension/ms-azuretools/vscode-docker)


-   #### Misc

    ---
    * [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)


</div>

## 🅰 Fonts
You will need to install [**MesloLGLDZ Nerd Font**](https://www.nerdfonts.com/).  This will be used to display glyphs and icons for all of your terminals.

## ✨ Theme
To customize your themes you need to set them in your settings.json file.  To identify items you want to change in the editor, you will have to use the inspector:

++cmd+shift+p++ › **Inspect Editor Tokens and Scopes**

This feature allows you to view the settings and scope of any item in your editor.  Once you have identified the item you want to change, go to the `settings.json` and make the desired modifications.

## 🗂️ Tab Removal
In general you should never need to have tabs.  VSCodium provides an ordered list of all files and windows you have opened sorted alphabetically.  This is a much better way of accessing files.

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
    * ++cmd+shift+p++ › Remote-SSH: Kill VSCodium Server on Host...

    This will disable file locking and restart the remote VSCodium host.  You will have to download all of your extensions once it reconnects with the server.



## 📚 References:
* https://stackoverflow.com/questions/57024732/how-can-i-customize-python-syntax-highlighting-in-vs-code
* https://www.alveeakand.com/how-to-modify-themes-in-vscode/
