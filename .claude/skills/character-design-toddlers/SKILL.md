---
name: character-design-toddlers
description: Character design principles for toddler (2-4) animated video. Use whenever designing a new KidsTv character, drawing a reference sheet prompt, or judging whether a generated character design is appropriate for the target age.
---

# Character Design for Toddlers (2–4)

Load this before writing any `bible/characters/<name>.md` entry or its base prompt.

## Silhouette and shape
- Build the character from simple geometric primitives (circle head, oval body). Toddlers recognize shape and silhouette before detail.
- Avoid sharp angles, spikes, or jagged features — they read as threatening even at low intensity.
- Head-to-body ratio should be "baby schema" (large head, big eyes, small nose/mouth) — this is what reads as cute and non-threatening to very young viewers and adults alike.

## Color
- 2–3 saturated, high-contrast primary/secondary colors max per character. Toddlers process bold, simple color blocking far better than gradients or muted palettes.
- Reserve one unmistakable "signature color" per character (e.g. "the orange fox", "the blue bear") so it can be named and recognized instantly, including at thumbnail size.
- Background/scene colors must contrast with the character so it never blends into the scene.

## Face and expression
- Eyes large, high on the head, spaced wide — the single strongest driver of perceived friendliness.
- Expressions must be exaggerated and unambiguous: one clear emotion per shot, readable from a still frame. No subtle/mixed expressions — toddlers cannot parse them.
- Mouth shape should support clear, exaggerated "visemes" (mouth shapes) if the character talks — this also helps with lip-sync tools.

## Consistency requirements (write these into the character's Bible page)
- One fixed, unchanging identifying prop or marking (a scarf, a spot pattern, ear shape) that must appear in literally every generation — this is often the first thing that drifts across AI generations.
- Never let a character's core silhouette or color change between episodes, even if the pose or outfit changes for a seasonal episode.

## Safety and appeal checklist before approving a character
- [ ] Readable and identifiable at 120×90px (thumbnail scale)
- [ ] No resemblance to existing protected IP (no recognizable ears/color combos from major studios — check explicitly)
- [ ] Passes a "scary test": no exposed teeth in a snarl, no red glowing eyes, no dark heavy shadows on the face
- [ ] Works in both a "happy" and a "worried-then-resolved" expression without redesign
- [ ] Genuinely likeable to an adult too (parents rewatch these hundreds of times)

## Output format for a character prompt
Always produce the base prompt as a fixed, reusable string, e.g.:
`"small round orange fox character, big round eyes, white belly patch, red scarf, soft 3D cartoon style, warm rim lighting, toddler-friendly, simple shapes, no sharp edges"`
Every future generation of this character must reuse this string verbatim as a prefix, only appending the scene-specific action/pose.
