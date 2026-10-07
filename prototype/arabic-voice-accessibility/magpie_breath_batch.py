from pathlib import Path

import soundfile as sf
import torch

from nemo.collections.tts.modules.magpietts_inference.utils import (
    ModelLoadConfig,
    load_magpie_model,
)
from nemo.collections.tts.parts.utils.tts_dataset_utils import (
    LANGUAGE_TOKENIZER_MAP,
)

MODEL = Path(
    "/mnt/d/LocalTTS/models/Magpie-TTS-Saudi-Arabic/"
    "Magpie-TTS-Saudi-Female.nemo"
)

CODEC = Path(
    "/mnt/d/LocalTTS/models/Nemo-NanoCodec/"
    "nemo-nano-codec-22khz-1.89kbps-21.5fps.nemo"
)

OUT_DIR = Path("/mnt/d/LocalTTS/outputs/breath-magpie-saudi")
OUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS = [
    ("ready", "ابدأ بهدوء."),
    ("natural_breath", "تنفس بشكل طبيعي."),
    ("take_time", "خذ وقتك."),
    ("pause", "تقدر توقف في أي وقت."),
    ("continue", "إذا كنت جاهز، اضغط ونكمل."),
]

assert MODEL.is_file(), MODEL
assert CODEC.is_file(), CODEC
assert torch.cuda.is_available(), "CUDA unavailable"

print("GPU   =", torch.cuda.get_device_name(0))
print("MODEL =", MODEL)
print("CODEC =", CODEC)

cfg = ModelLoadConfig(
    nemo_file=str(MODEL),
    codecmodel_path=str(CODEC),
)

model, checkpoint_name = load_magpie_model(cfg, device="cuda")

print("CHECKPOINT =", checkpoint_name)
print("SAMPLE_RATE =", model.sample_rate)

available = list(model.tokenizer.tokenizers.keys())
print("TOKENIZERS =", available)

SA_TOKENIZER = "arabic_SA_chartokenizer"

if SA_TOKENIZER not in available:
    raise RuntimeError(
        f"Saudi Arabic tokenizer not found. Available: {available}"
    )

LANGUAGE_TOKENIZER_MAP["ar"] = [SA_TOKENIZER]
print("ARABIC_TOKENIZER =", SA_TOKENIZER)

for name, text in PROMPTS:
    print()
    print("SYNTH_START", name, text)

    with torch.inference_mode():
        audio, audio_len = model.do_tts(
            transcript=text,
            language="ar",
            apply_TN=False,
        )

    n = int(audio_len[0].item())
    wav = audio[0, :n].detach().float().cpu().numpy()
    out = OUT_DIR / f"{name}.wav"

    sf.write(str(out), wav, int(model.sample_rate))

    print(
        "SYNTH_OK",
        name,
        "samples=",
        n,
        "bytes=",
        out.stat().st_size,
        "path=",
        out,
    )

print()
print("MAGPIE_BREATH_BATCH_PASS")
