# `whisper-intel-optimized`

## Open Issues

- https://huggingface.co/Intel/whisper-large-v2-onnx-int4-inc/discussions/3

## Install requirements

```
apt install python3.12-venv git-lfs
```

## Install

```
git clone https://github.com/egorsmkv/whisper-intel-optimized

cd whisper-intel-optimized

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install -U light-the-torch
ltt install torch torchaudio

pip install -U -r requirements.txt
pip install -U -r requirements-dev.txt
```

## Run

```
huggingface-cli download Intel/whisper-large-v2-onnx-int4-inc --local-dir-use-symlinks False --local-dir ./whisper-large-v2-onnx-int4-inc

wget -O short_1_16k.wav https://github.com/egorsmkv/wav2vec2-uk-demo/raw/master/short_1_16k.wav

python run.py
```


## Development

```
ruff check
ruff format
```
