---
name: youtube-kids-compliance
description: YouTube policy, COPPA/"Made for Kids", and AI-disclosure compliance rules for children's content. Use before uploading any episode, when writing the compliance-qa checklist, or when writing a title/description/thumbnail for a kids channel.
---

# YouTube Kids Content Compliance

Load this before finalizing any `episodes/<id>/qa.md` or `episodes/<id>/publish.md`.

## "Made for Kids" (COPPA) — non-negotiable
- Every video must be marked "Made for Kids" in YouTube Studio if it's primarily directed at children under 13 (this channel's entire output qualifies).
- Consequences of Made for Kids: personalized ads are disabled (lower CPM — already priced into this project's economics), comments are disabled, live chat/notifications are limited, and the "save to playlist"/end-screen features are restricted.
- Never design content or CTAs around comments, likes-for-engagement gimmicks, or personalized-ad-dependent features — they won't function.

## AI-content disclosure — non-negotiable
- Every video with AI-generated or AI-altered visuals/audio must have the "Altered or synthetic content" box checked under Attributes in YouTube Studio at upload time.
- This does NOT hurt monetization, reach, or recommendation eligibility on its own. Do not skip it to "avoid the label" — misrepresenting this is a policy violation, and the current regulatory climate (2026 Fairplay for Kids campaign) makes enforcement risk real and rising.

## "Inauthentic content" / "AI slop" — the deletion risk
YouTube has been actively removing channels showing these signals; avoid triggering them:
- Multiple uploads per day, or a rigid template repeated across every single video with no real variation.
- Plotless, "mesmerizing" content with no structure (endless colors/shapes/vehicles loop) and no human curation signal.
- No verifiable authorship touch: no real footage, no original narration, no human-written detail unique to that episode.
**Mitigations already built into this project:** format B's real stock footage IS the authenticity signal; keep upload cadence at or under 3/week; every script must include one non-templated original detail (see `story-writer` agent instructions).

## Child safety content rules
- No depiction of dangerous-to-imitate behavior (real slop channels have been caught showing unsafe eating — whole grapes, honey for infants — never repeat unverified "facts" or behaviors; route all such claims through `fact-checker`).
- No violence, no real fear without swift, clear resolution within the same video, no content that could function as a jump-scare.
- No commercial content disguised as an episode (no undisclosed product placement; no fake "unboxing" structure).
- Thumbnail and title must accurately represent the content — no bait mismatched with the actual video (this is both a policy risk and erodes the "responsible alternative" positioning from `research/2026-09-toddler-niche.md`).

## Footage and asset licensing
- Real stock footage must be commercially licensed (Pexels/Pixabay/Mixkit/Dareful per GUIDE.md) — verify each clip's specific license, not just the site's general policy, and record it in `episodes/<id>/footage.md`.
- Music must be licensed for commercial YouTube use (OpenArt-generated audio, or a cleared library) — never use unlicensed popular children's songs.
- Do not imitate the specific character design, color palette, or name of existing protected children's IP (Cocomelon, Ms. Rachel, Paw Patrol, etc.) — resemblance risk is both a takedown risk and a trust risk with parents.

## Pre-upload gate (what compliance-qa must verify)
1. Made for Kids ✅
2. Altered/synthetic content box checked (if any AI content) ✅
3. Upload cadence this week ≤ 3
4. At least one non-templated human-authored element identifiable
5. No unsafe-behavior depiction; all factual claims verified
6. Title/thumbnail accurately represent content
7. All footage/music licensing documented
