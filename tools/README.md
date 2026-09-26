# tools/fal_video.py — יצירת וידאו דרך fal.ai

סקריפט CLI ליצירת קליפי וידאו (text-to-video או image-to-video) דרך fal.ai, לשימוש בהפקת פרקי KidsTv.

## התקנה

```bash
pip install fal-client python-dotenv
cp tools/.env.example tools/.env
```

ואז לערוך את `tools/.env` ולמלא את המפתח (ראה הוראות למטה).

## שימוש

```bash
# טקסט לווידאו
python tools/fal_video.py --prompt "a friendly cartoon fox waving, kids animation style" \
    --output episodes/ep001/assets/fox_wave.mp4

# תמונה לווידאו (הנפשת תמונה קיימת)
python tools/fal_video.py --prompt "the fox slowly blinks and smiles" \
    --image-url https://example.com/fox.png \
    --output episodes/ep001/assets/fox_blink.mp4

# מודל אחר של fal.ai
python tools/fal_video.py --model fal-ai/kling-video/v2/master/image-to-video \
    --prompt "..." --image-url https://... --output out.mp4
```

`tools/.env` לא נכנס ל-git (מוגדר ב-`.gitignore`).
