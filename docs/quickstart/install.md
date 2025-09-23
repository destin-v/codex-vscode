## 🛠️ uv

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

``` py title="Install repo"
uv venv --python 3.12
uv sync
```

## 🏃 Hello World

```bash title="Hello World"
uv run tests/basic_test.py
```