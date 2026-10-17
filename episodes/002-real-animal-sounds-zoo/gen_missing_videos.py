#!/usr/bin/env python3
"""Generate the 6 missing episode-002 Veo clips (image-to-video) from the locked stills.

Runs gen_video.py sequentially per scene to respect Vertex concurrency limits.
Source still:  generated_images/{SCENE}_vertical.png
Output:        generated_videos/{SCENE}_veo.mp4
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PY = os.path.join(HERE, "venv_python_placeholder")  # replaced at runtime by caller
GEN = os.path.join(HERE, "gen_video.py")

SCENES = {
    "OPEN": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image of Pip in Pip's Meadow: "
        "Pip perks up his ears and breaks into a warm wave toward camera with one paw, gentle idle sway of the scarf in a light breeze, "
        "soft bounce on his feet, camera holds a static friendly medium shot, no camera shake, smooth toddler-paced motion, "
        "duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, "
        "simple rounded shapes, no sharp edges, consistent character design, no tall trees, "
        "keeping the same open meadow with only rolling hills and round bushes at the edges",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no trees, no forest, no new background elements, "
        "no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
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
    "MONKEY": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image: the cartoon monkey swings once on the branch "
        "and calls out a playful soft \"OOH OOH AH AH\" with a big happy open-mouth grin (friendly, not aggressive, no bared fangs), "
        "its tail curls and uncurls once, Pip perks up his ears and hops in place mimicking the rhythm, then turns to camera smiling, "
        "gentle leaf sway on the branch in background, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, "
        "soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, "
        "no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no bared fangs, no aggressive pose, no threatening posture, "
        "no cages, no metal bars, no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
    "SNAKE": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image: the cartoon snake lifts its head gently and "
        "gives a soft playful \"HISS\" with its mouth staying closed or in a small friendly closed-lip smile shape (no open mouth, no visible "
        "teeth or fangs), big round eyes staying warm and cheerful throughout, its coiled body sways slowly and gently side to side like a "
        "slow wave, no lunging or striking motion, Pip perks up his ears and sways playfully in the same slow gentle rhythm, then turns to "
        "camera smiling, static warm medium shot, smooth slow toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, "
        "warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, "
        "consistent character design, no cages, no metal bars, no concrete enclosure",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no aggressive pose, no bared fangs, no threatening posture, no striking motion, no lunging, "
        "no cages, no metal bars, no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
    "RECAP": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image: Pip points to the lion icon as \"roar\" is heard, "
        "then the elephant icon as \"toot\" is heard, then the monkey icon as \"ooh ooh ah ah\" is heard, then the snake icon as \"hiss\" is "
        "heard, each icon gently bounces once when pointed at (the snake icon stays coiled and calm, big round eyes, closed friendly mouth, "
        "no lunging), Pip's expression stays warm and encouraging throughout, camera holds a static friendly medium shot, "
        "smooth toddler-paced motion, duration 5-6 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, "
        "bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no tall trees, "
        "keeping the same open meadow with only rolling hills and round bushes at the edges",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no trees, no forest, no new background elements, no bared fangs, no aggressive pose, "
        "no threatening posture, no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
    "CLOSE": (
        "Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image of Pip in Pip's Meadow: Pip waves warmly at "
        "camera with one paw for about a second, eyes crinkling with a happy gentle smile, soft idle sway of the scarf in a light breeze, "
        "camera holds a static friendly medium shot, no camera shake, gentle fade-ready final frame, smooth toddler-paced motion, "
        "duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, "
        "simple rounded shapes, no sharp edges, consistent character design, no tall trees, "
        "keeping the same open meadow with only rolling hills and round bushes at the edges",
        "no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, "
        "no fast whip-pans, no strobing, no trees, no forest, no new background elements, "
        "no wide framing, no landscape orientation, no 16:9 aspect ratio",
    ),
}

if __name__ == "__main__":
    python = sys.argv[1] if len(sys.argv) > 1 else "python3"
    only = sys.argv[2:]  # optional scene filter
    for scene, (prompt, neg) in SCENES.items():
        if only and scene not in only:
            continue
        out = os.path.join(HERE, "generated_videos", f"{scene}_veo.mp4")
        cmd = [python, GEN, scene, "--prompt", prompt, "--neg", neg, "--seed", "7", "--out", out]
        print(f"\n===== {scene} =====", flush=True)
        rc = subprocess.run(cmd, cwd=HERE).returncode
        print(f"----- {scene} rc={rc} -----", flush=True)
