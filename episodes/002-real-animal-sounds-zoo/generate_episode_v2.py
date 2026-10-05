import os
import json
from google import genai
from PIL import Image
import io

# Setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/mnt/c/AI/Github/KidsTv/service-account.json"
client = genai.Client(vertexai=True, project="prefab-mapper-498617-m4", location="us-central1")

model_id = "publishers/google/models/gemini-2.5-flash-image"
manifest_path = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo/prompts.json"
output_dir = "/mnt/c/AI/Github/KidsTv/episodes/002-real-animal-sounds-zoo/generated_images"
reference_image_path = "/mnt/c/AI/Github/KidsTv/bible/characters/assets/pip-reference.jpg"

# Create output dir
os.makedirs(output_dir, exist_ok=True)

# Load reference image
ref_image = Image.open(reference_image_path)

# Load prompts
with open(manifest_path, 'r') as f:
    prompts = json.load(f)

print(f"Starting generation for {len(prompts)} scenes with Pip reference...")

for scene in prompts:
    scene_id = scene["id"]
    prompt = scene["image_prompt"]
    print(f"Generating scene: {scene_id}...")
    
    # Send both the reference image and the text prompt
    response = client.models.generate_content(
        model=model_id,
        contents=[ref_image, f"Keep character consistency with Pip from the reference image: {prompt}"]
    )
    
    # Save image
    saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            image_bytes = part.inline_data.data
            output_path = os.path.join(output_dir, f"{scene_id}_v2.png")
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"Saved {scene_id} to {output_path}")
            saved = True
            break
    
    if not saved:
        print(f"Failed to save {scene_id}")

print("Generation complete.")
