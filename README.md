## Install

```
apt install python3.12-venv
```

```
git clone https://github.com/egorsmkv/whisper-intel-optimized

cd whisper-intel-optimized

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install -U light-the-torch
ltt install torch torchaudio

pip install -U -r requirements.txt

# in development mode
pip install -r requirements-dev.txt
```

## Run

```
wget -O short_1_16k.wav https://github.com/egorsmkv/wav2vec2-uk-demo/raw/master/short_1_16k.wav

python run.py
```

## Development

```
ruff check
ruff format
```
