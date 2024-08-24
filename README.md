## Install

```
uv venv --python 3.12

source .venv/bin/activate

uv pip install -U light-the-torch
uv run ltt install torch torchaudio

uv pip install -U -r requirements.txt

# in development mode
uv pip install -r requirements-dev.txt
```

## Development

```
ruff check whisper-intel-optimized.ipynb
ruff format whisper-intel-optimized.ipynb
```
