import os, time
from google import genai
from google.genai import types
from PIL import Image

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
client = genai.Client(vertexai=True, project="prefab-mapper-498617-m4", location="us-central1")
MODEL = "publishers/google/models/gemini-2.5-flash-image"
EP = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo"
IMG_DIR = f"{EP}/generated_images"

JOBS = [
    ("ELEPHANT", "ELEPHANT_vertical.png", "ELEPHANT_vertical_fix.png",
     "Edit this image. CRITICAL ANATOMY FIX: the grey cartoon elephant is currently standing upright "
     "on its hind legs like a person. Redraw ONLY the elephant so it stands naturally on ALL FOUR legs "
     "like a real quadruped elephant (two front legs and two hind legs, all four feet flat on the ground), "
     "with no upright humanoid posture and no arm-like forelimbs. Keep EVERYTHING ELSE in the image exactly "
     "the same: Pip the quokka unchanged in the same position and pose, the same grass, the same low wooden "
     "viewing fence, the same sky, the same sun and clouds, the same rocks and bushes, the same framing and "
     "lighting. Change only the elephant's stance from two legs to four legs. Make the elephant a bit shorter "
     "and wider so its four legs rest on the same ground line."),
    ("RECAP", "RECAP_vertical.png", "RECAP_vertical_clean.png",
     "Edit this image. Remove ALL of the small floating cartoon animal icons (the floating elephant head, "
     "lion, monkeys, and snakes that hover in the sky around Pip) completely, leaving clean empty background "
     "(sky or grass as appropriate) where they were. Keep Pip the quokka EXACTLY as he is: same position, "
     "same pose with both arms/legs out pointing, same face, same teal scarf, same body, unchanged. Keep the "
     "meadow, the green rolling hills, the soft green bushes, the blue sky, the sun and clouds, the framing, "
     "and the lighting exactly the same. The result should show only Pip standing alone in the meadow with a "
     "clean background and no floating icons at all."),
]

for scene, src, dst, instruction in JOBS:
    src_path = os.path.join(IMG_DIR, src)
    dst_path = os.path.join(IMG_DIR, dst)
    img = Image.open(src_path)
    print(f"[{scene}] editing {src} -> {dst} ...", flush=True)
    resp = None
    for attempt in range(1, 7):
        try:
            resp = client.models.generate_content(
                model=MODEL,
                contents=[img, instruction],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio="9:16"),
                ),
            )
            break
        except Exception as e:
            msg = str(e)
            if any(k in msg for k in ("429", "RESOURCE_EXHAUSTED", "503")):
                w = min(60, 5 * attempt)
                print(f"  rate-limited retry {attempt}/6 in {w}s", flush=True)
                time.sleep(w)
            else:
                print(f"  error: {msg[:300]}", flush=True)
                break
    if resp is None:
        print(f"[{scene}] FAILED")
        continue
    saved = False
    for part in resp.candidates[0].content.parts:
        if part.inline_data:
            open(dst_path, "wb").write(part.inline_data.data)
            print(f"[{scene}] saved {dst_path}", flush=True)
            saved = True
            break
    if not saved:
        print(f"[{scene}] no image returned")
print("done")
