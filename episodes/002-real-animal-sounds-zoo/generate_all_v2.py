import os
import json
import time
from google import genai
from google.genai import types
from PIL import Image

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
client = genai.Client(vertexai=True, project="prefab-mapper-498617-m4", location="us-central1")

model_id = "publishers/google/models/gemini-2.5-flash-image"
base = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo"
manifest_path = f"{base}/prompts.json"
output_dir = f"{base}/generated_images"
reference_image_path = "/mnt/c/AI/Github/KidsTv/bible/characters/assets/pip-reference.jpg"

os.makedirs(output_dir, exist_ok=True)
ref_image = Image.open(reference_image_path)

with open(manifest_path, 'r') as f:
    prompts = json.load(f)

print(f"Starting generation for {len(prompts)} scenes with Pip reference...")

for scene in prompts:
    scene_id = scene["id"]
    prompt = scene["image_prompt"]
    output_path = os.path.join(output_dir, f"{scene_id}_vertical.png")
    if os.path.exists(output_path):
        print(f"Skipping {scene_id} (already exists)")
        continue

    neg = scene.get("negative_prompt", "")
    instruction = (
        "Keep the quokka character EXACTLY consistent with the Pip reference image: "
        "same fur colors, same teal scarf with white star patch, same body proportions, "
        "same face and eye shape, same soft 3D cartoon style. Do not redesign the character.\n\n"
        f"Scene: {prompt}\n\nAvoid: {neg}"
    )

    print(f"Generating scene: {scene_id}...")
    response = None
    for attempt in range(1, 7):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=[ref_image, instruction],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(aspect_ratio="9:16"),
                ),
            )
            break
        except Exception as e:
            msg = str(e)
            if "429" in msg or "RESOURCE_EXHAUSTED" in msg or "503" in msg:
                wait = min(60, 5 * attempt)
                print(f"  rate-limited on {scene_id}, retry {attempt}/6 in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  error on {scene_id}: {msg[:200]}")
                break

    if response is None:
        print(f"Failed to generate {scene_id}")
        continue

    saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            print(f"Saved {scene_id} to {output_path}")
            saved = True
            break

    if not saved:
        print(f"Failed to save {scene_id}")

print("Generation complete.")
