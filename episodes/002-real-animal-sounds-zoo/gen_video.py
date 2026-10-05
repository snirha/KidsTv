import os, time, sys, json, argparse
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
from google import genai
from google.genai import types

PROJECT = "prefab-mapper-498617-m4"
LOC = "us-central1"
MODEL = "publishers/google/models/veo-3.1-generate-001"
EP = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo"

ap = argparse.ArgumentParser()
ap.add_argument("scene", help="scene id, e.g. LION")
ap.add_argument("--prompt", required=True)
ap.add_argument("--neg", default="")
ap.add_argument("--seed", type=int, default=7)
ap.add_argument("--lock-end", action="store_true",
                help="feed the reference as last_frame to kill end-of-clip zoom/drift")
ap.add_argument("--out", default=None)
a = ap.parse_args()

scene = a.scene
img_path = f"{EP}/generated_images/{scene}_vertical.png"
out_dir = f"{EP}/generated_videos"; os.makedirs(out_dir, exist_ok=True)
out_path = a.out or f"{out_dir}/{scene}_veo_v2.mp4"

CAMERA_NEG = ("no camera movement, no zoom, no zoom-in, no push-in, no dolly-in, no pan, no tilt, "
"no tracking shot, no moving camera, no crop-in, no framing change, no close-up transition, "
"no camera shake, locked static camera")

NEG = ", ".join(x for x in [a.neg, CAMERA_NEG] if x)

client = genai.Client(vertexai=True, project=PROJECT, location=LOC)
with open(img_path, "rb") as f:
    img_bytes = f.read()
image = types.Image(image_bytes=img_bytes, mime_type="image/png")

cfg_kwargs = dict(
    aspect_ratio="9:16",
    negative_prompt=NEG,
    seed=a.seed,
    generate_audio=False,
)
if a.lock_end:
    cfg_kwargs["last_frame"] = image  # force final frame back to the locked reference

print(f"[{scene}] submitting Veo image-to-video (lock_end={a.lock_end}, seed={a.seed}) ...", flush=True)
op = client.models.generate_videos(
    model=MODEL, prompt=a.prompt, image=image,
    config=types.GenerateVideosConfig(**cfg_kwargs),
)
print(f"[{scene}] operation: {op.name}", flush=True)

t0 = time.time()
while not op.done:
    time.sleep(15)
    op = client.operations.get(op)
    print(f"[{scene}]   ... {int(time.time()-t0)}s done={op.done}", flush=True)
    if time.time() - t0 > 900:
        print("TIMEOUT", flush=True); sys.exit(1)

vid = op.response.generated_videos[0].video
with open(out_path, "wb") as f:
    f.write(vid.video_bytes)
print(f"[{scene}] Saved: {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)
