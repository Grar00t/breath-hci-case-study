# Local TTS Evidence

Evidence boundary: **NO CLAIM BEYOND THE RECORDED LOCAL RUN.**

## Recorded environment

- Date: 2026-10-07
- GPU: NVIDIA GeForce RTX 3060
- NeMo: 2.8.0rc0
- NeMo source commit after tokenizer compatibility fix:
  `78694d56d262ebb960101d2155b272811854e612`
- Checkpoint: `Magpie-TTS-Saudi-Female.nemo`
- Codec: `nemo-nano-codec-22khz-1.89kbps-21.5fps.nemo`
- Sample rate: 22050 Hz
- Selected tokenizer: `arabic_SA_chartokenizer`
- Local transformer type reported by NeMo: `autoregressive`
- Baked context embeddings reported: 5 speakers

## Batch result

| id | text | samples | wav bytes |
| --- | --- | ---: | ---: |
| ready | ابدأ بهدوء. | 30720 | 61484 |
| natural_breath | تنفس بشكل طبيعي. | 34816 | 69676 |
| take_time | خذ وقتك. | 26624 | 53292 |
| pause | تقدر توقف في أي وقت. | 37888 | 75820 |
| continue | إذا كنت جاهز، اضغط ونكمل. | 53248 | 106540 |

Terminal completion marker:

```text
MAGPIE_BREATH_BATCH_PASS
```

## What this proves

This run proves only that the five listed prompts were synthesized locally
with the recorded model/configuration and produced non-empty WAV outputs.

It does **not** establish speech quality, user preference, accessibility
benefit, therapeutic benefit, or any clinical outcome.

Model files and generated WAV files are not included in this repository.
