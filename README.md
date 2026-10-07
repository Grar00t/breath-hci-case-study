# Breath | تـنـفـــس — Design Case Study

A mobile interaction concept for adolescents (13–17) that uses microphone-detected breathing as a game input. In the prototype, exhaling starts play, inhaling moves the balloon away from the needle, and steady breathing drives the core interaction.

This repository documents an HCI design case study: interface screens, interaction rationale, and a high-fidelity prototype concept. It does **not** contain a production application, clinical intervention, medical device, or evidence that the design treats OCD.

![Navigation flow map](figures/flow-map.png)

## Repository contents

| Artifact | Purpose |
| --- | --- |
| `figures/flow-map.png` | Navigation and task-flow overview |
| `figures/game-start.png` | Start-state interaction |
| `figures/game-balloon-needle.png` | Core balloon/needle game state |
| `figures/settings-accessibility.png` | Accessibility/settings concept |
| `figures/splash.png` | Splash/entry screen |

## Core interaction

| Start by exhaling | Breath-controlled balloon | Accessibility settings |
|---|---|---|
| ![game start](figures/game-start.png) | ![balloon and needle](figures/game-balloon-needle.png) | ![settings](figures/settings-accessibility.png) |

The design explores whether breathing can be used as an embodied input mechanism in a calming game. That is a **design hypothesis**, not a clinical efficacy claim.

## Design process

- **Lo-fi → hi-fi**: paper concepts → Figma → an interactive **Proto.io** prototype.
- **Focused slice**: the prototype concentrates on the first-session path — onboarding, tutorial, and first game — instead of attempting production completeness.
- **HCI rationale**: the project applies usability principles such as visible system status, recognition over recall, error prevention, and a deliberately simple visual language.
- **Accessibility concepts**: the screens include color-blind/high-contrast options, audio descriptions, adjustable microphone sensitivity, and customizable avatars.

## Evaluation boundary

The original project describes two evaluation tracks:

1. task-based user testing reported as involving adolescents diagnosed with OCD, with participant/guardian consent and anonymized feedback;
2. expert review using Nielsen-style usability heuristics.

The public repository currently contains the design artifacts shown above, but it does **not** include participant-level data, consent records, study instruments, reviewer notes, raw observations, or a results dataset. Those evaluation claims therefore cannot be independently reproduced from this repository alone.

No clinical outcome, treatment efficacy, safety, diagnosis, or reduction in barriers to care is established by the files in this repository.

## What this repository supports

The committed artifacts support inspection of the prototype's visual design, navigation concept, game interaction, and accessibility concepts. They do not support claims about therapeutic effectiveness or clinical validation.

## Credits

SE365 Human–Computer Interaction, Prince Sultan University — supervised by **Dr. Sofianiza Abd Malik**. Team: **Rasha AlNaji**, Noora Alsarhan, Reema Alkuaik, Hallah Alfaraj.
