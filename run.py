import os

import numpy as np

from transformers import WhisperProcessor, PretrainedConfig
from optimum.onnxruntime import ORTModelForSpeechSeq2Seq

from pydub import AudioSegment


def audiosegment_to_librosawav(audiosegment):
    channel_sounds = audiosegment.split_to_mono()[:1]  # only select the first channel
    samples = [s.get_array_of_samples() for s in channel_sounds]

    fp_arr = np.array(samples).T.astype(np.float32)
    fp_arr /= np.iinfo(samples[0].typecode).max
    fp_arr = fp_arr.reshape(-1)

    return fp_arr


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

sr = 16_000
waveform = AudioSegment.from_file("short_1_16k.wav").set_frame_rate(sr)
waveform = audiosegment_to_librosawav(waveform)

print("audio_data shape:", waveform.shape)

inputs = processor(
    waveform,
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
