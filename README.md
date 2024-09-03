# Optimized Whisper for Intel

🚨🚨🚨 ATTENTION 🚨🚨🚨:

> Your CPU must have AVX512 support to run this model, run `lscpu` to check it.


## Install requirements

```
curl -LsSf https://astral.sh/uv/install.sh | sh

apt install git-lfs ffmpeg
```

## Install

```
git clone https://github.com/egorsmkv/whisper-intel-optimized

cd whisper-intel-optimized

uv venv --python 3.12 && source .venv/bin/activate

uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
```

## Run

### Download an audio file

```
wget -O ukrainian_speech.wav https://github.com/egorsmkv/wav2vec2-uk-demo/raw/master/short_1_16k.wav
```

### Download quantized models

```
huggingface-cli download Intel/whisper-large-v2-onnx-int4-inc --local-dir-use-symlinks False --local-dir ./whisper-large-v2-onnx-int4-inc

huggingface-cli download Intel/whisper-medium-onnx-int4-inc --local-dir-use-symlinks False --local-dir ./whisper-medium-onnx-int4-inc

huggingface-cli download Intel/whisper-small-onnx-int4-inc --local-dir-use-symlinks False --local-dir ./whisper-small-onnx-int4-inc
```

### Run the model

```
python run.py "openai/whisper-large-v2" "whisper-large-v2-onnx-int4-inc" "ukrainian_speech.wav"

python run.py "openai/whisper-medium" "whisper-medium-onnx-int4-inc" "ukrainian_speech.wav"

python run.py "openai/whisper-small" "whisper-small-onnx-int4-inc" "ukrainian_speech.wav"

python run.py "openai/whisper-small" "whisper-small-onnx-int4-inc" "sample_english.wav"
```

### Outputs

**whisper-large-v2-onnx-int4-inc**:

```
Taiwan and the United States are important strategic partners. But there is a difference. The United States has a special law that stipulates that if China attacks Taiwan, the American military must protect it.
```

**whisper-medium-onnx-int4-inc**:

```
Taiwan is a strategic partner, but there is a difference. The US has a special law that provides that if China attacks Taiwan, the US military must protect it.
```

**whisper-small-onnx-int4-inc**:

```
That we've had a
```

> **Note**: It didn't recognize the Ukrainian speech at all, only English speech at the end of the audio.

## Development

```
ruff check
ruff format
```
