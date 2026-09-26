---
name: ai-visual-consistency
description: Techniques for keeping an AI-generated character and world visually consistent across many separate generations (Google Flow Ingredients, OpenArt Character/Director/Image/Video, or similar tools). Use whenever writing prompts for a KidsTv episode, or reviewing generated images/video for drift from the character Bible.
---

# AI Visual Consistency Across Generations

Load this before writing `episodes/<id>/prompts.md`.

## The core problem
Every separate AI generation is a fresh roll of the dice on appearance unless you actively constrain it. Drift shows up as: color shifting, proportions changing, a marking disappearing, style shifting from "3D" to "flat" mid-episode. Toddlers and parents *will* notice a character "changing" between shots — more than any other viewer group, because they rewatch obsessively.

## Techniques, in order of reliability
1. **Use a saved/reference character asset whenever the tool supports it** (e.g. OpenArt's Character tool, an uploaded reference image, or Google Flow's **Ingredients** — up to 3 reference images per prompt, added via "Add" under the prompt box or referenced with `@` once uploaded to the project) instead of re-describing the character from scratch every time. This is always the strongest lock on identity. In Flow specifically: keep the character reference on a plain/clean background (not a full scene) — character ingredients work best isolated; use a *separate* ingredient for a recurring location/background (also on its own, without the character in it), then combine both ingredients + a text prompt describing the action for scenes where the character is in that location.
   - **Flow's 3-ingredient limit workaround: combine multiple references into one collage image first.** If a shot needs more reference images than the tool allows per prompt (e.g. Flow's 3-ingredient cap), build a single composite/collage image containing all the extra references (e.g. one image with 4 previously-approved animal stills stacked or tiled), and upload that collage as a single ingredient. This worked well in practice: a Pip + "4-animal collage" (2 ingredients total) produced a recap scene with all 4 animals correctly matching their individually-approved designs, without hitting the 3-ingredient ceiling.
   - **Flow: "Ingredients to Video" vs "Frames to Video" — these are not interchangeable.** Ingredients to Video treats your reference images as *flexible* elements the model may reinterpret/recompose (good for generating a *new* composition from separate character + location references; Veo 2 only as of 2026, not yet Veo 3). Frames to Video *locks* your image as the exact starting frame and animates from it (good for animating a composition you've already approved and don't want reinterpreted). Once you have an approved still you like, always animate it with Frames to Video, not Ingredients to Video — the latter can silently redesign the shot.
   - **Frames to Video can still invent content at the frame edges.** As the camera/scene "continues" beyond the locked starting frame, the model may add elements that violate the location Bible (e.g. trees appearing at the sides of a shot whose Bible explicitly says "no tall trees") even though the starting image itself was correct. The motion/video prompt must restate the full environment negative-prompt block (not just the location's name) — don't assume constraints from the image prompt carry over silently into the video generation step.
2. **Single continuous generation over stitched clips**, when the tool allows it (e.g. OpenArt Director generating a full multi-minute scene in one pass). Consistency degrades every time you start a new generation from a blank context.
3. **Fixed base prompt string, reused verbatim.** Never paraphrase the character description between shots — copy-paste the exact string from `bible/characters/<name>.md`. Only the action/pose/scene clause should change.
4. **Fixed style suffix** appended to every prompt in an episode: e.g. `", soft 3D cartoon style, warm pastel palette, toddler animation style, consistent character design"`. This anchors render style, not just character identity.
5. **Negative prompts** to suppress common drift/safety issues: `no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons`. Also add explicit anti-distortion terms for faces/features that have drifted before (e.g. `no distorted nose, no deformed face, no asymmetrical features`) — once a specific failure mode shows up for a character, bake its negation into every future prompt for that character, not just that one retry.
6. **Seed reuse** if the tool exposes a seed value — reusing a seed across a shot sequence reduces stylistic jumps even when content changes.
7. **Image-to-video over text-to-video** for hybrid (format B) shots: generate one still that nails the character/style, then animate that exact image, rather than generating video directly from text each time.

## Re-running the same prompt is not reproducible
Unlike animating an already-approved image (Frames to Video, or any true image-to-image/image-to-video step), generating fresh from a text prompt — even the exact same text — can produce a meaningfully different result each time (different color pattern, added props, different background elements). Episode 001 saw this directly: the same cow-scene prompt produced one clean on-spec result and, on a separate generation, a version with an unrequested tractor, hay bales, and a bell/rope collar. Once a specific generation is approved, treat *that file* as the locked asset — don't assume re-running "the same prompt" later will reproduce it, and don't discard an approved result in favor of a fresh regeneration just to "double check," since the fresh one is a new roll of the dice, not a more reliable copy.

## Reviewing outputs for drift
When checking generated assets against the Bible, compare against this checklist:
- [ ] Signature color(s) match Bible hex values (close enough to read as "the same")
- [ ] Signature prop/marking is present and in the right place
- [ ] Proportions (head:body ratio, eye size) match prior episodes
- [ ] Render style (3D vs 2D, lighting warmth) matches the rest of the episode and prior episodes
- [ ] No extraneous limbs/fingers/artifacts (common AI failure mode — toddlers' pattern-matching parents will spot this instantly)
- [ ] No unrequested added elements in a locked environment (models sometimes "helpfully" add structures/props like a house, bench, or path that were never in the brief) — check the generation against the location's Bible page, not just against how nice it looks

## Model adds elements you didn't ask for
This is a real, recurring failure mode, not a one-off: an image/video model may embellish a locked environment with extra props (a house, furniture, a path, flowers) that read as charming but were never specified. Treat this exactly like character drift: compare against the location's Bible doc, and if elements were invented, either (a) explicitly negative-prompt them out and regenerate, or (b) if the team genuinely likes the addition, treat it as a deliberate scope decision — update the Bible doc with the new fixed element before accepting it as canon, so every future generation includes it too. Never let an "accidental improvement" become inconsistent canon by accepting it once without documenting it.

If a generation drifts, regenerate with the fixed base prompt restored rather than trying to prompt-patch a broken result — patching compounds drift.

## Lip-sync: dubbing models vs. avatar-generation models are not interchangeable
If a character's mouth needs to move in sync with separately-recorded narration (not audio the video tool generated itself), check which category a candidate model actually falls into before testing it — the two categories look similar in marketing copy but solve different problems:
- **Video-to-video "lip-resync"/dubbing models** (e.g. fal.ai's `latentsync`, `sync-lipsync`, `veed/lipsync`) re-time mouth motion that is *already present and continuous* in the source video onto new audio. They do not generate mouth motion from nothing. If the source AI clip only has a brief non-speech mouth gesture (e.g. one "hi!" burst then an idle closed mouth — typical of a short Google Flow/Veo clip that wasn't built as a talking performance), these models will pass the clip through nearly unchanged regardless of the new audio's content. This failure is silent: the job completes successfully and returns a valid video, so verify with a pixel diff between source and output frames (mean per-pixel diff in the single digits out of 255 = no real edit happened) rather than trusting a "COMPLETED" status. A tighter crop on the face does not fix this category mismatch — it's not a framing problem.
- **Image-to-video audio-driven avatar-generation models** (e.g. fal.ai's `kling-video/ai-avatar`) build the entire performance from scratch from a still reference image + an audio file. This is the right category when the source has no continuous talking motion to re-time. Sanity-check: output duration should match the *audio's* length, not any pre-existing video's length — if it does, the model is generating fresh rather than editing a fixed-length clip.
- Because avatar-generation models regenerate the whole frame on every run (not just the mouth region), treat their output like any other fresh AI generation for consistency review — check it against the character Bible using the drift checklist above (fur color/shade and ear shape are worth a specific look; minor frame-to-frame flicker in these has been observed even when the overall likeness holds).

## Prompt template to hand to visual-prompter output
```
[BASE CHARACTER PROMPT — verbatim from bible/characters/<name>.md]
+ [scene action clause, present tense, concrete: "sits by a campfire looking up at fireflies"]
+ [FIXED STYLE SUFFIX from bible/style-bible.md]
+ [negative prompt block]
```
