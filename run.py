import os

import torchaudio

from transformers import WhisperProcessor, PretrainedConfig
from optimum.onnxruntime import ORTModelForSpeechSeq2Seq

model_name = "openai/whisper-large-v2"
model_path = "whisper-large-v2-onnx-int4-inc"

processor = WhisperProcessor.from_pretrained(model_name)

model_config = PretrainedConfig.from_pretrained(model_name)

sessions = ORTModelForSpeechSeq2Seq.load_model(
    os.path.join(model_path, "encoder_model.onnx"),
    os.path.join(model_path, "decoder_model.onnx"),
    os.path.join(model_path, "decoder_with_past_model.onnx"),
)

model = ORTModelForSpeechSeq2Seq(
    sessions[0], sessions[1], model_config, model_path, sessions[2]
)


audio_data, sr = torchaudio.load("short_1_16k.wav")

print(audio_data.shape, sr)

input_features = processor(
    audio_data, sampling_rate=sr, return_tensors="pt"
).input_features

predicted_ids = model.generate(input_features)[0]
transcription = processor.decode(predicted_ids)

print(transcription)
