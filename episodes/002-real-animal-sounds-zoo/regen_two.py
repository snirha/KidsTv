#!/usr/bin/env python3
"""Re-generate only ELEPHANT + RECAP Veo clips after the still fixes.
ELEPHANT: new quadruped still. RECAP: new clean Pip-only still (no icons; icons overlaid later in edit).
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "gen_video.py")

SCENES = {
    "ELEPHANT": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image: the cartoon elephant stays standing "
        "naturally on all four legs the whole time (never rises up on its hind legs) and lifts its trunk upward, giving a cheerful soft "
        "\"TOOT\" like a small round horn — the trunk stays raised for the rest of the clip, it does not lower again; its big floppy ears "
        "flap gently once while the trunk is still up; at the same time as the trunk is raised, Pip perks up his ears, then tilts his head "
        "back in wide-eyed wonder looking up at the elephant's still-raised trunk and big ears, gasping softly (\"Whoa!\") and gesturing "
        "with both paws to show how big they are, camera holds a static warm medium shot, gentle grass sway in background, "
        "smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, "
        "bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, "
        "no cages, no metal bars, no concrete enclosure",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no cages, no metal bars, no elephant standing upright on two legs, no bipedal elephant, "
        "no elephant rearing up on hind legs, no humanoid elephant posture, no trunk lowering before Pip's reaction, "
        "no trunk lowering mid-clip, no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
    "RECAP": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image of Pip in Pip's Meadow: Pip enthusiastically "
        "points outward to one side, then to the other side, then up, then down — as if presenting four different animals around him in "
        "sequence, holding each point briefly with a warm encouraging smile toward camera between points; his scarf sways gently in a light "
        "breeze; NO floating icons or bubbles appear anywhere in the frame, the background stays the same clean open meadow with only "
        "rolling hills and round bushes at the edges, camera holds a static friendly medium shot, smooth toddler-paced motion, "
        "duration 5-6 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, "
        "simple rounded shapes, no sharp edges, consistent character design, no tall trees, "
        "keeping the same open meadow with only rolling hills and round bushes at the edges",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no trees, no forest, no new background elements, no floating icons, no bubbles, "
        "no animals in frame, no bared fangs, no aggressive pose, no threatening posture, "
        "no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
}

if __name__ == "__main__":
    python = sys.argv[1] if len(sys.argv) > 1 else "python3"
    for scene, (prompt, neg) in SCENES.items():
        out = os.path.join(HERE, "generated_videos", f"{scene}_veo.mp4")
        cmd = [python, GEN, scene, "--prompt", prompt, "--neg", neg, "--seed", "7", "--out", out]
        print(f"\n===== {scene} =====  -> {out}", flush=True)
        rc = subprocess.run(cmd, cwd=HERE).returncode
        print(f"----- {scene} rc={rc} -----", flush=True)
