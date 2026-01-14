---
icon: material/rocket-launch
---

# :material-rocket-launch: Quickstart

> Learning starts with failure.
>
> **— Josiah Bancroft**

## 🛠️ uv

Install a package manager:
=== "brew"
    ```bash
    brew install uv
    ```

=== "curl"
    ``` bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "wget"
    ```bash
    wget -qO- https://astral.sh/uv/install.sh | sh
    ```

Install repo:
``` python
uv venv --python 3.12
uv sync
```


## 🏃 Hello World

<!-- termynal -->
```bash
$ uv run hello_world.py
hello world!
Done!
```
