import os, time
from google import genai
from google.genai import types
from PIL import Image

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
client = genai.Client(vertexai=True, project="prefab-mapper-498617-m4", location="us-central1")
MODEL = "publishers/google/models/gemini-2.5-flash-image"
IMG_DIR = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo/generated_images"

KEEP = ("Keep Pip the quokka EXACTLY as he is — same position, same pose, same face, same teal scarf, unchanged — and keep the "
        "grass, the low wooden viewing fence, the sky, the sun, the clouds, the rocks and the bushes exactly the same. ")

JOBS = [
    ("LION", "the cartoon lion"),
    ("ELEPHANT", "the cartoon elephant"),
    ("MONKEY", "the cartoon monkey (including the tree branch it sits on)"),
    ("SNAKE", "the cartoon snake"),
]

def build(scene, animal):
    return ("Edit this image. Remove " + animal + " competely and entirely from the frame — it must be gone, not faded, not "
            "ghosted. Fill the area it occupied with the natural background that belongs there (green grass, blue sky, or the "
            "wooden fence, whichever fits seamlessly). " + KEEP +
            " The result must show ONLY Pip in the zoo habitat clearing, with a clean natural background where the animal used "
            "to be, and no trace of the animal at all. Do not add anything new. Do not move Pip. Do not change the framing, "
            "the lighting, or the art style.")

def gen(scene, instruction):
    src = os.path.join(IMG_DIR, f"{scene}_vertical.png")
    dst = os.path.join(IMG_DIR, f"{scene}_vertical_pip-only.png")
    print(f"[{scene}] ...", flush=True)
    resp = None
    for attempt in range(1, 7):
        try:
            resp = client.models.generate_content(
                model=MODEL, contents=[Image.open(src), instruction],
                config=types.GenerateContentConfig(response_modalities=["IMAGE"],
                                                   image_config=types.ImageConfig(aspect_ratio="9:16")))
            break
        except Exception as e:
            m = str(e)
            if any(k in m for k in ("429", "RESOURCE_EXHAUSTED", "503")):
                w = min(60, 5 * attempt); print(f"  retry {attempt}/6 in {w}s", flush=True); time.sleep(w)
            else:
                print(f"  err: {m[:250]}", flush=True); break
    if resp is None:
        print(f"[{scene}] FAILED"); return
    for part in resp.candidates[0].content.parts:
        if part.inline_data:
            open(dst, "wb").write(part.inline_data.data); print(f"[{scene}] saved {dst}", flush=True); return
    print(f"[{scene}] no image")

for scene, animal in JOBS:
    gen(scene, build(scene, animal))
print("done")
