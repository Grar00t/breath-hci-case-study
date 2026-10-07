# Arabic Voice Accessibility Prototype

Experimental accessibility concept for the Breath HCI case study.

## Goal

Explore whether optional Arabic spoken UI cues could improve accessibility
and reduce the amount of visual attention required during the interaction.

This prototype is intentionally separate from the original case-study
artifact.

## Proposed interaction

Examples of short interface cues:

- "ابدأ بهدوء."
- "خذ وقتك."
- "تنفس بشكل طبيعي."
- "يمكنك التوقف في أي وقت."
- "اضغط للمتابعة عندما تكون جاهزاً."

The language is intentionally neutral and non-diagnostic.

## Accessibility ideas

- Arabic spoken navigation cues
- Adjustable speech rate
- Optional subtitles
- Independent speech-volume control
- Replay last instruction
- Visual-only mode
- Audio-only assistance where appropriate
- RTL-aware text paired with speech

## Engineering direction

A future implementation could expose a tiny engine-neutral interface:

    speak(text, locale, rate)
    stop()
    replay()
    set_enabled(bool)

The HCI layer should not depend directly on a particular TTS provider.

## Boundary

NO CLAIM BEYOND THE PROTOTYPE.

This is an accessibility and interaction-design experiment.

It does not claim to:
- diagnose OCD or any mental-health condition;
- provide psychotherapy;
- replace exposure and response prevention or other clinical treatment;
- demonstrate therapeutic effectiveness;
- establish that voice guidance improves clinical outcomes.

Any therapeutic wording or clinical deployment would require appropriate
domain review, participant safeguards, and evaluation.

No participant data is used by this prototype.
