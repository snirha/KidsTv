#!/usr/bin/env python3
"""
CLI to generate video clips via fal.ai for KidsTv episodes.

Setup:
  pip install fal-client python-dotenv
  cp tools/.env.example tools/.env   # then fill in FAL_KEY

Usage:
  python tools/fal_video.py --prompt "a friendly cartoon fox waving, kids animation style" \
      --output episodes/ep001/assets/fox_wave.mp4

  # image-to-video
  python tools/fal_video.py --prompt "the fox slowly blinks and smiles" \
      --image-url https://example.com/fox.png \
      --output episodes/ep001/assets/fox_blink.mp4

  # different fal model
  python tools/fal_video.py --model fal-ai/kling-video/v2/master/image-to-video \
      --prompt "..." --image-url https://... --output out.mp4
"""

import argparse
import os
import sys
import urllib.request

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

import fal_client  # noqa: E402  (import after env vars are loaded)

DEFAULT_TEXT_TO_VIDEO_MODEL = "fal-ai/luma-dream-machine"
DEFAULT_IMAGE_TO_VIDEO_MODEL = "fal-ai/luma-dream-machine/image-to-video"


def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"[fal] {log['message']}", file=sys.stderr)


def download(url: str, dest: str):
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    urllib.request.urlretrieve(url, dest)


def main():
    parser = argparse.ArgumentParser(description="Generate a video clip via fal.ai")
    parser.add_argument("--prompt", required=True, help="Text prompt describing the video")
    parser.add_argument("--image-url", help="Source image URL for image-to-video models")
    parser.add_argument(
        "--model",
        help="fal.ai model id (defaults to a text-to-video or image-to-video model "
        "depending on whether --image-url is set)",
    )
    parser.add_argument("--output", required=True, help="Local path to save the resulting video")
    parser.add_argument(
        "--extra",
        action="append",
        default=[],
        help="Extra model argument as key=value (repeatable), e.g. --extra duration=5",
    )
    args = parser.parse_args()

    if not os.environ.get("FAL_KEY"):
        print(
            "Missing FAL_KEY. Copy tools/.env.example to tools/.env and set your fal.ai API key.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = args.model or (
        DEFAULT_IMAGE_TO_VIDEO_MODEL if args.image_url else DEFAULT_TEXT_TO_VIDEO_MODEL
    )

    arguments = {"prompt": args.prompt}
    if args.image_url:
        arguments["image_url"] = args.image_url
    for item in args.extra:
        key, _, value = item.partition("=")
        arguments[key] = value

    print(f"[fal] submitting to {model}...", file=sys.stderr)
    result = fal_client.subscribe(
        model,
        arguments=arguments,
        with_logs=True,
        on_queue_update=on_queue_update,
    )

    video_url = result.get("video", {}).get("url") or result.get("video_url")
    if not video_url:
        print(f"[fal] unexpected response, no video URL found: {result}", file=sys.stderr)
        sys.exit(1)

    print(f"[fal] downloading {video_url} -> {args.output}", file=sys.stderr)
    download(video_url, args.output)
    print(f"[fal] done: {args.output}")


if __name__ == "__main__":
    main()
