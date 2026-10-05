import os, time, sys
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
from google import genai
from google.genai import types

PROJECT = "prefab-mapper-498617-m4"
LOC = "us-central1"
MODEL = "publishers/google/models/veo-3.1-generate-001"

EP = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo"
IMG = f"{EP}/generated_images/LION_vertical.png"
OUT = f"{EP}/generated_videos"
os.makedirs(OUT, exist_ok=True)

PROMPT = ("Vertical 9:16 portrait composition, tall vertical framing. Animate this exact image: "
"Pip points at the cartoon lion with one paw and leans forward, curious; the lion stays standing "
"naturally on all four legs the whole time (never rises up on its hind legs, never stands upright "
"like a person) and opens its mouth in a big playful-cute \"ROAR\" (exaggerated friendly mouth shape, "
"round eyes staying warm and gentle, not fierce), its puffy mane bounces softly once, Pip's ears perk "
"up and he nods along, then turns back to camera, gentle "
"grass sway in background, static warm medium shot, smooth toddler-paced motion, soft 3D cartoon "
"style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple "
"rounded shapes, no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure")

NEG = ("no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, "
"no weapons, no fast whip-pans, no strobing, no bared fangs, no aggressive pose, no cages, no metal bars, "
"no lion standing upright on two legs, no bipedal lion, no lion rearing up on hind legs, no humanoid lion "
"posture, no wide framing, no landscape orientation, no 16:9 aspect ratio")

client = genai.Client(vertexai=True, project=PROJECT, location=LOC)

with open(IMG, "rb") as f:
    img_bytes = f.read()

image = types.Image(image_bytes=img_bytes, mime_type="image/png")

print(f"Submitting image-to-video (Veo) for LION ...", flush=True)
op = client.models.generate_videos(
    model=MODEL,
    prompt=PROMPT,
    image=image,
    config=types.GenerateVideosConfig(
        aspect_ratio="9:16",
        negative_prompt=NEG,
    ),
)

print(f"Operation: {op.name}", flush=True)
t0 = time.time()
while not op.done:
    time.sleep(15)
    op = client.operations.get(op)
    print(f"  ... {int(time.time()-t0)}s done={op.done}", flush=True)
    if time.time() - t0 > 900:
        print("TIMEOUT", flush=True); sys.exit(1)

vid = op.response.generated_videos[0].video

out_path = f"{OUT}/LION_veo.mp4"
# Vertex AI client: video comes back as raw bytes on .video_bytes
with open(out_path, "wb") as f:
    f.write(vid.video_bytes)
print(f"Saved: {out_path}", flush=True)
