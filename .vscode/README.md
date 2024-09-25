# VSCode

This is a compilation of configuration settings, extensions, and add-on recommended for development using VSCode.

## 📦 Recommended Extensions

<details>
  <summary>Code</summary>

  * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
</details>

<details>
  <summary>Documentation</summary>

  * [Automatic Doc String](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
  * [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  * [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)
</details>

<details>
  <summary>Linting / Formatting</summary>

  * [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
  * [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
</details>

<details>
  <summary>Testing</summary>

  * [Python Test Explorer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)
  * [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)
</details>

<details>
  <summary>Configuration Control</summary>

  * [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
</details>

<details>
  <summary>Containers</summary>

  * [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  * [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
</details>

<details>
  <summary>Remote</summary>

  * [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
  * [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
  * [Remote Explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer)
</details>

<details>
  <summary>Misc</summary>

  * [Back & Forth](https://marketplace.visualstudio.com/items?itemName=nick-rudenko.back-n-forth)
  * [Chronicler](https://marketplace.visualstudio.com/items?itemName=arcsine.chronicler)
  * [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
  </details>

## 🅰 Fonts
You will need to install [**MesloLGLDZ Nerd Font**](https://www.nerdfonts.com/).  This will be used to display glyphs and icons for all of your terminals.

## ✨ Theme
To customize your themes you need to set them in your settings.json file.  To identify items you want to change in the editor, you will have to use the inspector:

**Cmd-Shift-P › Inspect Editor Tokens and Scopes**

This feature allows you to view the settings and scope of any item in your editor.  Once you have identified the item you want to change, go to the `settings.json` and make the desired modifications.

## 🗂️ Tab Removal
In general you should never need to have tabs.  VSCode provides an ordered list of all files and windows you have opened sorted alphabetically.  This is a much better way of accessing files.

* **Cmd-P** # shows all tabs
* Settings › Workbench › Editor: Show Tabs [OFF]

## 🔧 Troubleshooting

<details>
<summary>TestExplorer UI</summary>
To have TestExplorer UI properly detect your tests by pressing and selecting:

* **Shift-Cmd-P** › Python: Configure Tests › Pytests › <target_dir>

For a full explanation on how to properly set up the TestExplorer UI see [**here**](https://graycode.ie/blog/how-to-set-up-testing-explorer-with-python-pytest-in-vscode/).
</details>

<details>
<summary>SSH FileLocking</summary>
If performing remote development you may need to configure your file locking parameters depending on whether it is allowed on the host:

* Settings › Remote.SSH: Lockfiles In Tmp [ON]
* Settings › Remote.SSH: useFlock [OFF]
* **Cmd-Shift-P** › Remote-SSH: Kill VSCode Server on Host...

This will disable file locking and restart the remote VSCode host.  You will have to download all of your extensions once it reconnects with the server.

</details>

## 📚 References:
* https://stackoverflow.com/questions/57024732/how-can-i-customize-python-syntax-highlighting-in-vs-code
* https://www.alveeakand.com/how-to-modify-themes-in-vscode/
