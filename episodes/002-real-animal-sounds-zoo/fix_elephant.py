import os, time
from google import genai
from google.genai import types
from PIL import Image

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
client = genai.Client(vertexai=True, project="prefab-mapper-498617-m4", location="us-central1")
MODEL = "publishers/google/models/gemini-2.5-flash-image"
EP = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo"
IMG_DIR = f"{EP}/generated_images"

PIP = ("Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, "
       "warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide "
       "apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny "
       "white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, "
       "toddler animation style, consistent character design")
ENV = ("cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft "
       "green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm "
       "bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no "
       "zoo visitors, no crowds, no signage")

# 1) retry the edit with much more forceful, spatial wording
EDIT_INSTRUCTION = (
    "You MUST physically redraw the grey elephant in this image so that it is a NORMAL FOUR-LEGGED ELEPHANT. "
    "Right now it is incorrectly standing upright on two hind legs like a teddy bear, with two arm-like stubs. "
    "That is wrong. Replace its body with a proper quadruped elephant body: a long horizontal barrel-shaped "
    "torso lying sideways, with FOUR straight pill-shaped legs going down to the ground (two front legs beneath "
    "its head and trunk, two hind legs beneath its rear), all four flat feet resting on the same ground line, "
    "no arms, no upright posture, no belly facing the camera. Its head, trunk, big floppy ears and gentle face "
    "should stay the same style. Do not keep the old two-legged body. Everything else (Pip, fence, grass, sky, "
    "sun, clouds, rocks, framing, lighting) stays exactly as it is. This is the entire point of the edit: the "
    "elephant must end up with four legs on the ground."
)

# 2) fresh generation variant, front-on but emphatically quadruped
FRESH_PROMPT = (
    "Vertical 9:16 portrait composition, tall vertical framing, " + PIP + ", standing in a " + ENV + ", "
    "standing next to a friendly round cartoon elephant with soft grey rounded skin, big floppy rounded ears, "
    "a gently curled trunk, big gentle eyes, soft rounded 3D-cartoon body matching Pip's art style. THE "
    "ELEPHANT IS A NORMAL QUADRUPED: it stands flat on FOUR legs, its body is low and wide and horizontal, "
    "with four short thick legs planted on the ground and two small white toenails on each foot; it does NOT "
    "stand upright, it has NO arms, NO humanoid posture, NO belly facing the camera, NO sitting pose. Both Pip "
    "and the elephant face the camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler "
    "animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent "
    "character design"
)
FRESH_NEG = ("no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, "
             "no weapons, no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no "
             "signage, no vehicles, no elephant standing upright on two legs, no bipedal elephant, no elephant "
             "with arms, no humanoid elephant posture, no teddy-bear elephant, no wide framing, no landscape "
             "orientation, no 16:9 aspect ratio")

def gen(contents, out_path, tag):
    print(f"[{tag}] ...", flush=True)
    resp = None
    for attempt in range(1, 7):
        try:
            resp = client.models.generate_content(
                model=MODEL, contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio="9:16"),
                ),
            )
            break
        except Exception as e:
            msg = str(e)
            if any(k in msg for k in ("429", "RESOURCE_EXHAUSTED", "503")):
                w = min(60, 5 * attempt); print(f"  rate-limited retry {attempt}/6 in {w}s", flush=True); time.sleep(w)
            else:
                print(f"  error: {msg[:300]}", flush=True); break
    if resp is None:
        print(f"[{tag}] FAILED"); return
    for part in resp.candidates[0].content.parts:
        if part.inline_data:
            open(out_path, "wb").write(part.inline_data.data)
            print(f"[{tag}] saved {out_path}", flush=True); return
    print(f"[{tag}] no image returned")

# retry edit
src = Image.open(os.path.join(IMG_DIR, "ELEPHANT_vertical.png"))
gen([src, EDIT_INSTRUCTION], os.path.join(IMG_DIR, "ELEPHANT_vertical_fix2.png"), "edit-retry")
# fresh variant
gen([Image.open("/mnt/c/AI/Github/KidsTv/bible/characters/assets/pip-reference.jpg"),
     FRESH_PROMPT + "\n\nAvoid: " + FRESH_NEG],
    os.path.join(IMG_DIR, "ELEPHANT_vertical_fresh.png"), "fresh")
print("done")
