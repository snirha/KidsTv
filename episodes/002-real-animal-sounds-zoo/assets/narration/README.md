# קריינות פרק 002 — קבצים מבוקשים

הקול הנעול: **"Pip - Pip's Meadow"** (פרופיל מותאם ב-ElevenLabs).
הטקסט המדויק + הנחיות הביצוע: `../../narration.md`.

## 7 הקבצים (שמות מדויקים)

| קובץ | מקור ב-narration.md | זמן דיבור | סה"כ כולל [PAUSE] |
|---|---|---|---|
| `open.mp3` | §OPEN | 5.2s | 5.2s |
| `lion.mp3` | §ITEM 1 — LION | 15.5s | ~20.5s |
| `elephant.mp3` | §ITEM 2 — ELEPHANT | 19.0s | ~24.0s |
| `monkey.mp3` | §ITEM 3 — MONKEY | 19.5s | ~24.5s |
| `snake.mp3` | §ITEM 4 — SNAKE | 15.5s | ~20.5s |
| `recap.mp3` | §RECAP | 20.4s | ~25.4s |
| `close.mp3` | §CLOSE | 5.2s | 5.2s |

**סה"כ ≈ 125.3s (~2:05).**

## כללים (מ-narration.md §"הערות ביצוע")

- כל שורת `[PAUSE 2-3s]` חייבת להישאר **שקט מלא** בקובץ — לא לקצץ ב-post.
- "motherese": משפטים קצרים, קצב איטי במעט, הפסקות ברורות.
- הדגשות (ROAR / TOOT / OOH OOH AH AH / HISS / REAL) — להעלות טון ואנרגיה **קלות**, לא צעקה. ROAR = מוקצן-חמוד, לא עמוק/מאיים. HISS = משחקי, לא מלחישני.
- שורת הפרט האישי של הפיל ("Whoa! Its ears are as big as a blanket!") — delivery ספונטני/נלהב, **פעם אחת בלבד** בפרק.

## הפקה אוטומטית (Claude)

אם יסופק ה-`voice_id` של "Pip - Pip's Meadow", ההפקה אוטומטית:
`POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}` עם `eleven_multilingual_v2`.
(המפתח הקיים מאפשר `text_to_speech` — אומת. חסר רק ה-ID.)

## לאחר ההפקה

הקבצים נצרכים ע"י שלב ה-lip-sync (`fal-ai/kling-video/ai-avatar/v2`) — רפרנס Pip-בלבד מ-
`../../generated_images/{SCENE}_vertical_pip-only.png`, אודיו = קובץ הקריינות המתאים.
