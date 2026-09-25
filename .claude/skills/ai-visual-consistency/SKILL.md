---
name: ai-visual-consistency
description: Techniques for keeping an AI-generated character and world visually consistent across many separate generations (OpenArt Character/Director/Image/Video, or similar tools). Use whenever writing prompts for a KidsTv episode, or reviewing generated images/video for drift from the character Bible.
---

# AI Visual Consistency Across Generations

Load this before writing `episodes/<id>/prompts.md`.

## The core problem
Every separate AI generation is a fresh roll of the dice on appearance unless you actively constrain it. Drift shows up as: color shifting, proportions changing, a marking disappearing, style shifting from "3D" to "flat" mid-episode. Toddlers and parents *will* notice a character "changing" between shots — more than any other viewer group, because they rewatch obsessively.

## Techniques, in order of reliability
1. **Use a saved/reference character asset whenever the tool supports it** (e.g. OpenArt's Character tool, or an uploaded reference image) instead of re-describing the character from scratch every time. This is always the strongest lock on identity.
2. **Single continuous generation over stitched clips**, when the tool allows it (e.g. OpenArt Director generating a full multi-minute scene in one pass). Consistency degrades every time you start a new generation from a blank context.
3. **Fixed base prompt string, reused verbatim.** Never paraphrase the character description between shots — copy-paste the exact string from `bible/characters/<name>.md`. Only the action/pose/scene clause should change.
4. **Fixed style suffix** appended to every prompt in an episode: e.g. `", soft 3D cartoon style, warm pastel palette, toddler animation style, consistent character design"`. This anchors render style, not just character identity.
5. **Negative prompts** to suppress common drift/safety issues: `no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons`.
6. **Seed reuse** if the tool exposes a seed value — reusing a seed across a shot sequence reduces stylistic jumps even when content changes.
7. **Image-to-video over text-to-video** for hybrid (format B) shots: generate one still that nails the character/style, then animate that exact image, rather than generating video directly from text each time.

## Reviewing outputs for drift
When checking generated assets against the Bible, compare against this checklist:
- [ ] Signature color(s) match Bible hex values (close enough to read as "the same")
- [ ] Signature prop/marking is present and in the right place
- [ ] Proportions (head:body ratio, eye size) match prior episodes
- [ ] Render style (3D vs 2D, lighting warmth) matches the rest of the episode and prior episodes
- [ ] No extraneous limbs/fingers/artifacts (common AI failure mode — toddlers' pattern-matching parents will spot this instantly)

If a generation drifts, regenerate with the fixed base prompt restored rather than trying to prompt-patch a broken result — patching compounds drift.

## Prompt template to hand to visual-prompter output
```
[BASE CHARACTER PROMPT — verbatim from bible/characters/<name>.md]
+ [scene action clause, present tense, concrete: "sits by a campfire looking up at fireflies"]
+ [FIXED STYLE SUFFIX from bible/style-bible.md]
+ [negative prompt block]
```
