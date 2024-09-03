import os
import sys

import sphn
from transformers import WhisperProcessor, PretrainedConfig
from optimum.onnxruntime import ORTModelForSpeechSeq2Seq


if len(sys.argv) != 4:
    print("Usage: python run.py <model_name> <model_path> <speech_file>")
    exit(1)


model_name = sys.argv[1]
model_path = sys.argv[2]
filename = sys.argv[3]

processor = WhisperProcessor.from_pretrained(model_name)

model_config = PretrainedConfig.from_pretrained(model_name)

sessions = ORTModelForSpeechSeq2Seq.load_model(
    os.path.join(model_path, "encoder_model.onnx"),
    os.path.join(model_path, "decoder_model.onnx"),
    os.path.join(model_path, "decoder_with_past_model.onnx"),
    provider="CUDAExecutionProvider",
)

model = ORTModelForSpeechSeq2Seq(
    sessions[0], sessions[1], model_config, model_path, sessions[2]
)

waveform, sr = sphn.read(filename)

print("audio_data shape:", waveform.shape)

inputs = processor(
    waveform[0],
    sampling_rate=sr,
    return_attention_mask=True,
    return_tensors="pt",
)

generated_ids = model.generate(
    input_features=inputs.input_features,
    attention_mask=inputs.attention_mask,
)

transcriptions = processor.batch_decode(generated_ids, skip_special_tokens=True)

for transcription in transcriptions:
    print(transcription.strip())
