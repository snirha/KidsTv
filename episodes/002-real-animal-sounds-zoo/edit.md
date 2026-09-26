# edit — EDL: Episode 002 "Real Animal Sounds: Zoo Edition"

פורמט B | Pip | 16:9 | קול: Pip - Pip's Meadow (ElevenLabs, נעול — ראו narration.md)
מקור: script.md + narration.md (VO מדויק + [PAUSE] נשמרים כזמן טיימליין אמיתי — לא נחתכים) + prompts.md (קבצי AI) + footage.md (קבצי סטוק אמיתיים)

**⚠️ הערה חשובה — פוטג' אמיתי טרם נעול:** footage.md מסמן את כל 4 קליפי הפוטג' האמיתי (`01-lion-real.mp4`, `02-elephant-real.mp4`, `03-monkey-real.mp4`, `04-snake-real.mp4`) כ-⚠️ ממתינים לאישור המשתמש בצפייה בפועל (במיוחד הנחש — corn/garter/ball python בלבד, לא מין רעיל). ה-EDL הזה בנוי על ההנחה שהקליפים שיאושרו יהיו באורך דומה למה שמוצג כאן (3.9s/5.5s לכל שוט פוטג'); **משכי השוטים האמיתיים בטבלה למטה עלולים להזדקק לכיוון קל (±0.5-1s) כשהקליפים ייבחרו סופית** — לא לראות את הזמנים כאן כסופיים ל-100% עבור שוטי ה-`0X-*-real.mp4`, רק ל-VO/PAUSE שכבר נעולים.

**⚠️ הערה קריטית — בועות RECAP (לקח נעול מפרק 001, CLAUDE.md §5, גרסה 3):** קליפ ה-RECAP (`002-recap-pip-meadow.mp4`) חייב להיווצר ולהיאושר ב-Google Flow כ**וידאו נקי אחד**: Pip + 4 בועות אייקון (אריה/פיל/קוף/נחש) מסביבו, Pip מצביע על כל בועה בזה אחר זה — **בלי** שום מעורבות של שלב ה-lip-sync avatar-generation בשלב הזה. רק **בהרכבה בפועל (ffmpeg, אחרי אישור הקליפ הנקי)**:
1. לחתוך/להפיק מהתמונה המאושרת **רפרנס Pip-בלבד** (ללא הבועות בפריים, ואם אפשר גם ללא חפיפה גופנית לבועות — למלא את אזורי הבועות בגוון רקע שטוח לפי הפתרון-גרסה-3 שנעל בפרק 001, לא לחתוך/למסגר אותן).
2. לשלוח את הרפרנס Pip-בלבד ל-`fal-ai/kling-video/ai-avatar/v2` עם קובץ קריינות ה-RECAP.
3. לאחר קבלת הפלט המסונכרן, **להרכיב את 4 הבועות המקוריות מהקליפ הנקי המאושר בחזרה כ-overlay נפרד** (עם מסכת אלפא עגולה, ping-pong extend אם צריך) על גבי הפלט — לוודא קואורדינטות ידנית על הפלט בפועל, לא על הקלט.
**לעולם לא לשלוח את תמונת/קליפ הבועות המלא ל-avatar model** — זה בדיוק מה שגרם לבועת הכבשה לסטות לפרצוף דמוי-תינוק בפרק 001.

**חוקי בסיס שנאכפו בטבלה:**
- פתיח/סגיר ממותגים קבועים, ~5.2 שנ' כ"א (מדויק לפי VO, ראה narration.md).
- פורמט B: בכל פריט — AI clip → מילת מפתח → **מעבר** → פוטג' אמיתי, קריינות תמיד מתחילה עם תחילת השוט.
- אין שוט (ללא שינוי/זום/קאט) מעל ~6 שניות — כל שוט שה-VO+PAUSE שלו יחד עוברים 6s פוצל לשני שוטי-משנה (ראו פריט 3 — קוף, שני מקרים).
- **קליפי AI הם 4-5 שנ' (לפי prompts.md), אך כמה שוטים בטבלה דורשים כיסוי של 5.1-6.8 שנ'.** לכיסוי הפער: **לופ הלוך-ושוב (ping-pong: forward+reverse חלק via ffmpeg)** על קליפ ה-AI, **לא הקפאת פריים אחרון** (לקח נעול מפרק 001 — "לא מקצועי"). "slow-motion stretch" (`setpts`) מקובל רק לפערים קטנים (עד 1-2 שנ'). באף שוט כאן הפער אינו כפול-ומעלה מאורך הקליפ (מקסימום ~6.8s מתוך קליפ 4-5s, כ-40%-70% תוספת) — לא מזוהה כאן חריגה שדורשת דגל "תסריט ארוך מדי ביחס לנכסים"; ping-pong loop מספיק.
- כל [PAUSE 2-3s] מ-narration.md מופיע כשורה/חלק-שורה עם משך שקט אמיתי בטיימליין (ממוצע 2.5s בחישוב) — לא קוצץ.
- 3 טראקים נפרדים: **VO** (קריינות Pip), **Music** (מיטה, 15–20% מתחת ל-VO), **SFX-Animal** (צלילי חיה אמיתיים/סטייל-קרטון, מונחים בנפרד — ראו footage.md §5).

---

## טבלת עריכה

| # | זמן | וידאו (שם קובץ) | אודיו/קריינות (VO) | טקסט על המסך | מעבר |
|---|------|------------------|---------------------|----------------|------|
| 1 | 0:00.0–0:05.2 (5.2s) | `002-open-pip-meadow.mp4` | "Hi, hi! It's me, Pip! Today, we're going to explore zoo animals!" | (ללא — לוגו/Pip בלבד, ללא טקסט מסך בפתיח הממותג) | Hard cut |
| **ITEM 1 — LION** ||||||
| 2 | 0:05.2–0:08.2 (3.0s) | `002-item1-lion-ai.mp4` (AI clip, פועל במלואו — point + roar mouth) | "Look! A lion!" / "The lion says... ROAR!" | **ROAR!** (מופיע עם ההדגשה הקולית) | Hard cut |
| 3 | 0:08.2–0:13.3 (5.1s) | `002-item1-lion-ai.mp4` — המשך/זום-אין עדין (**ping-pong loop אם 5.1s ארוך מאורך ה-asset בפועל, לא הקפאה**) | "Roar! Roar! Can you say roar?" **[PAUSE 2-3s]** | **Can you say ROAR?** נשאר על המסך לאורך כל ה-PAUSE | Hard cut |
| 4 | 0:13.3–0:16.3 (3.0s) | `002-item1-lion-ai.mp4` — קלוז-אפ על Pip מרחרח (קרופ/זום על אותו asset) | "Sniff, sniff... let's see a REAL lion!" | (ללא טקסט — שורת מעבר) | **Gentle wipe** ל-פוטג' אמיתי (AI→Real, לפי פורמט B) |
| 5 | 0:16.3–0:20.2 (3.9s) | `01-lion-real.mp4` (טרים מהקליפ הגולמי — **⚠️ טרם נעול, ראה footage.md**) | "Yes! A real lion!" / "The lion says roar. Roar!" | **A REAL LION!** | Hard cut |
| 6 | 0:20.2–0:25.7 (5.5s) | `01-lion-real.mp4` המשך, או קאט-בק ל-PiP קטן של Pip מקשיב בפינה | "Did you hear the lion say roar?" **[PAUSE 2-3s]** | **Did you hear ROAR?** | Hard cut |
| **ITEM 2 — ELEPHANT** ||||||
| 7 | 0:25.7–0:28.7 (3.0s) | `002-item2-elephant-ai.mp4` | "Look! An elephant!" / "The elephant says... TOOT!" | **TOOT!** | Hard cut |
| 8 | 0:28.7–0:33.8 (5.1s) | `002-item2-elephant-ai.mp4` — זום-אין עדין (ping-pong loop אם צריך) | "Toot! Toot! Can you say toot?" **[PAUSE 2-3s]** | **Can you say TOOT?** | Hard cut |
| 9 | 0:33.8–0:36.8 (3.0s) | `002-item2-elephant-ai.mp4` קלוז-אפ Pip מרחרח | "Sniff, sniff... let's see a REAL elephant!" | (ללא) | Gentle wipe → Real |
| 10 | 0:36.8–0:40.7 (3.9s) | `02-elephant-real.mp4` (**⚠️ טרם נעול; ודא מין עקבי אחד לאורך כל הקליפ — לא מונטאז' של פיל אפריקאי+הודי**) | "Yes! A real elephant!" / "The elephant says toot. Toot!" | **A REAL ELEPHANT!** | Hard cut |
| 11 | 0:40.7–0:46.2 (5.5s) | `02-elephant-real.mp4` המשך | "Did you hear the elephant say toot?" **[PAUSE 2-3s]** | **Did you hear TOOT?** | Hard cut |
| 12 | 0:46.2–0:49.7 (3.5s) | `02-elephant-real.mp4` — קלוז-אפ ייעודי על האוזניים הגדולות (תואם לשורת האד-ליב) | "Whoa! Its ears are as big as a blanket!" *(giggle/gasp of wonder — spontaneous delivery, לא תבנית)* | (ללא טקסט — רגע ספונטני, לא לתייג) | Hard cut |
| **ITEM 3 — MONKEY** ||||||
| 13 | 0:49.7–0:53.6 (3.9s) | `002-item3-monkey-ai.mp4` | "Look! A monkey!" / "The monkey says... OOH OOH AH AH!" | **OOH OOH AH AH!** | Hard cut |
| 14a | 0:53.6–0:58.6 (5.0s) | `002-item3-monkey-ai.mp4` — זום-אין עדין (**ping-pong loop; אורך VO ל-4 ההברות דורש מלוא הזמן, לא להאיץ — ראה narration.md**) | "Ooh ooh! Ah ah! Can you say ooh ooh ah ah?" **[PAUSE 2-3s מתחיל]** | **Can you say OOH OOH AH AH?** | Hard cut |
| 14b | 0:58.6–1:00.4 (1.8s) | קאט-בק ל-Pip תקריב (קרופ אחר על אותו asset) — **שוט נפרד כדי לא לעבור 6s רצף** | *(המשך [PAUSE], שקט מלא)* | **Can you say OOH OOH AH AH?** (נשאר) | Hard cut באמצע ה-PAUSE, לשמור כל שוט מתחת ל-6s |
| 15 | 1:00.4–1:03.4 (3.0s) | `002-item3-monkey-ai.mp4` קלוז-אפ Pip מרחרח | "Sniff, sniff... let's see a REAL monkey!" | (ללא) | Gentle wipe → Real |
| 16 | 1:03.4–1:07.7 (4.3s) | `03-monkey-real.mp4` (**⚠️ טרם נעול; ודא בפועל ללא bared-teeth threat display, לא מריבה בין קופים — ראה footage.md**) | "Yes! A real monkey!" / "The monkey says ooh ooh ah ah!" | **A REAL MONKEY!** | Hard cut |
| 17a | 1:07.7–1:12.6 (4.9s) | `03-monkey-real.mp4` המשך | "Did you hear the monkey say ooh ooh ah ah?" **[PAUSE 2-3s מתחיל]** | **Did you hear OOH OOH AH AH?** | Hard cut |
| 17b | 1:12.6–1:14.1 (1.5s) | קאט-בק ל-PiP קטן של Pip מקשיב בפינה — **שוט נפרד כדי לא לעבור 6s רצף** | *(המשך [PAUSE], שקט מלא)* | **Did you hear OOH OOH AH AH?** (נשאר) | Hard cut באמצע ה-PAUSE |
| **ITEM 4 — SNAKE** ||||||
| 18 | 1:14.1–1:17.1 (3.0s) | `002-item4-snake-ai.mp4` (נחש AI ידידותי — עיניים גדולות/עגולות, פה סגור/חייכן, בלי שיניים — לפי prompts.md) | "Look! A snake!" / "The snake says... HISS!" | **HISS!** | Hard cut |
| 19 | 1:17.1–1:22.2 (5.1s) | `002-item4-snake-ai.mp4` — זום-אין עדין (ping-pong loop אם צריך) | "Hiss! Hiss! Can you say hiss?" **[PAUSE 2-3s]** | **Can you say HISS?** | Hard cut |
| 20 | 1:22.2–1:25.2 (3.0s) | `002-item4-snake-ai.mp4` קלוז-אפ Pip מרחרח | "Sniff, sniff... let's see a REAL snake!" | (ללא) | Gentle wipe → Real |
| 21 | 1:25.2–1:29.1 (3.9s) | `04-snake-real.mp4` (**⚠️ הכי לא-נעול/הכי קריטי — חובה corn snake / garter snake / ball python בלבד, מאומת מהכותרת/תגית של המקור, לא זיהוי חזותי בלבד; לפסול כל ראש משולש/רעלנים אזוריים — ראה footage.md §4**) | "Yes! A real snake!" / "The snake says hiss. Hiss!" | **A REAL SNAKE!** | Hard cut |
| 22 | 1:29.1–1:34.6 (5.5s) | `04-snake-real.mp4` המשך, תנועה איטית בלבד | "Did you hear the snake say hiss?" **[PAUSE 2-3s]** | **Did you hear HISS?** | Hard cut |
| **RECAP** ||||||
| 23 | 1:34.6–1:39.8 (5.2s) | `002-recap-pip-meadow.mp4` (קובץ נקי מאושר, Pip+4 בועות; ראו הערת lip-sync בראש הקובץ — הבועות **אינן** עוברות avatar-generation) | "We heard the lion say roar!" / "We heard the elephant say toot!" | אייקון אריה מהבהב → אייקון פיל מהבהב | Hard cut |
| 24 | 1:39.8–1:43.3 (3.5s) | `002-recap-pip-meadow.mp4` המשך | "We heard the monkey say ooh ooh ah ah!" | אייקון קוף מהבהב (מילת מפתח ארוכה — לא לדחוס) | Hard cut |
| 25 | 1:43.3–1:45.9 (2.6s) | `002-recap-pip-meadow.mp4` המשך | "We heard the snake say hiss!" | אייקון נחש מהבהב | Hard cut |
| 26 | 1:45.9–1:51.8 (5.9s) | `002-recap-pip-meadow.mp4` המשך, כל 4 האייקונים מוצגים יחד | "Roar, toot, ooh ooh ah ah, hiss!" **[PAUSE 2-3s]** | 4 האייקונים יחד + מילים מוקפצות | Hard cut |
| 27a | 1:51.8–1:57.5 (5.7s) | `002-recap-pip-meadow.mp4` + zoom-in קל | "Roar, toot, ooh ooh ah ah, hiss! Can you say them too?" | **Can you say them too?** | Hard cut |
| 27b | 1:57.5–2:00.0 (2.5s) | קאט-בק ל-Pip תקריב — **שוט נפרד כדי לא לעבור 6s רצף** | *(המשך [PAUSE], שקט מלא)* | **Can you say them too?** (נשאר) | Hard cut באמצע ה-PAUSE |
| **CLOSE** ||||||
| 28 | 2:00.0–2:05.2 (5.2s) | `002-close-pip-meadow.mp4` | "Great exploring today! Wiggle your nose... bye bye, see you next time!" | **See you next time!** + כרזת "Next episode" (thumbnail קטן) | Fade to logo/end-card |

**זמן ריצה משוער כולל: ≈ 2:05.2 (125.2 שניות).**
הערה: זהו זמן מדויק לפי VO + כל ה-[PAUSE] שנשמרו במלואם (ללא קיצוץ, ממוצע 2.5s ל-PAUSE), כאשר כל שוט מתחיל עם תחילת הקריינות שלו (לפי כלל פורמט B). תואם את אומדן narration.md (≈125.3s). קרוב לפרק 001 (1:56) אך ארוך ממנו בכ-9 שניות — בעיקר בזכות מילת המפתח הארוכה של הקוף ("Ooh ooh ah ah", 4 הברות) ושורת הפרט האישי של הפיל; שניהם עדיין בתוך יעד ~5 דק' לפרק (`toddler-content-pacing`), אין חריגה.

---

## טראקים אודיו נפרדים

1. **VO (קריינות Pip)** — כמפורט בטבלה, 0dB רפרנס.
2. **Music bed** — רץ ברציפות מהפתיח ועד הסגיר (מומלץ reuse ישיר של "Sweet Children Music Loop – Gentle Joy" (Sonican, Pixabay Music) שנעל בפרק 001 — ראו footage.md §6, משך ~2:04 קרוב מספיק ל-2:05.2 של הפרק הזה, לא צפוי seam נראה), עוצמה **15–20% מתחת ל-VO** לכל אורך הפרק; מותר לעלות מעט (עד ~10% מתחת) בזמן ה-[PAUSE] כדי שלא יהיה שקט מוחלט מדכא, אך לא לחזור לעוצמת VO-level.
3. **SFX-Animal (טראק נפרד מה-VO ומהמוזיקה)** — קריטי: פוטג' הסטוק כנראה דומם (footage-curator flag ב-footage.md), ולכן:
   - בשוטי ה-AI clip (roar/toot/ooh-ooh-ah-ah/hiss מצוירים) — שכבו SFX חיה **בסגנון קרטוני/רך** (עוצמה בינונית) בדיוק בסנכרון לפתיחת הפה/החדק/הזנב באנימציה.
   - בשוטי הפוטג' האמיתי (`01-lion-real.mp4` וכו') — שכבו SFX חיה **אמיתי** (מקורות מתועדים ב-footage.md §5: `sfx-lion-roar.mp3`, `sfx-elephant-trumpet.mp3`, `sfx-monkey-call.mp3`, `sfx-snake-hiss.mp3` — כולם Pixabay Content License, רישיון חופשי מסחרי, קרדיט לא נדרש) בדיוק ברגע "Yes! A real [animal]!" ובחזרה על מילת המפתח.
   - **דגש מיוחד ל-SFX הנחש וה-ROAR:** לפי footage.md §5a/§5d — לבחור roar קצר/גבוה-יותר (לא עמוק/מאיים) ו-hiss שנשמע "משחקי" לא "סרט אימה"; לוודא בהאזנה בפועל לפני נעילה (עדיין לא הושמעו/אושרו לפי status.md).
   - ודאו ש-SFX לא "צורח" מעל ה-VO — peak SFX כ-10-15% מתחת ל-VO peak, לא מעל.

---

## הצעות לקטעי Shorts (9:16, עד 60 שנ')

1. **"Real Lion Roar!"** — שוטים 2–6 (Item 1 המלא, פתיח מוקצר של Pip "Hi hi, it's Pip!" מ-2-3s בלבד + כל פריט האריה) → crop ל-9:16 ממורכז על Pip/החיה, ~23-25s. חזק כ-Short כי הוא יחידת AI→Real מלאה עם שאלה+פאוזה, ו-ROAR הוא hook קולי חד וברור.
2. **"Its Ears Are as Big as a Blanket!"** — שוטים 7–12 (Item 2 המלא, כולל שורת האד-ליב הספונטנית של הפיל) → ~24s; רגע ההתפעלות הבלתי-תבניתי מתפקד היטב כ-hook ויראלי ל-Short (משפט השוואה קליט + חיה גדולה = חזק ל-thumbnail).
3. **"Roar, Toot, Ooh Ooh Ah Ah, Hiss!"** — כל ה-RECAP (שוטים 23–27) + חצי-שנייה מהסגיר ("bye bye, see you next time!" כ-CTA לפרק המלא) → ~28-30s, כותרת/hook חזק לפורמט Shorts (מקהלת חזרה קצבית עם 4 צלילים שונים = variety חזותי/קולי גבוה מפרק 001).

כל שלושת ה-Shorts מתחת ל-60s, כל אחד עומד בפני עצמו (unit שלם: AI→Real→שאלה או recap שלם), ודורש רק re-crop ל-9:16 + הוספת כותרת/קאפשן מוגדל בראש הפריים (בטוח מ-safe zones של TikTok/Shorts UI).

---

## Checklist לפני exporting

- [ ] **סנכרון**: כל SFX-Animal מסונכרן פריים-מדויק לפתיחת הפה/חדק/זנב של החיה (AI ואמיתי כאחד); VO מתחיל בדיוק עם תחילת כל שוט (כלל פורמט B).
- [ ] **ווליום**: Music bed נבדק ונשאר 15–20% מתחת ל-VO לכל אורך הפרק (כולל תוך כדי SFX); אין peak של SFX מעל VO; loudness סופי עומד בתקן היעד של הערוץ (למשל -14 LUFS ליוטיוב).
- [ ] **אין מסך שחור**: אין פריימים שחורים/ריקים בין שוטים — כל המעברים הם hard cut או gentle wipe עם פריים תקין משני הצדדים; בדקו במיוחד את המעברים AI→Real (שוטים 4→5, 9→10, 15→16, 20→21) ואת שני הפיצולים בתוך ה-PAUSE (14a→14b, 17a→17b, 27a→27b).
- [ ] **סאב-טייטלים**: כתוביות נלוות (burned-in ו/או קובץ .srt) לכל שורת VO, כולל מילות המפתח המודגשות (ROAR/TOOT/OOH OOH AH AH/HISS/REAL) בסנכרון; אין כתובית שנשארת על המסך בזמן ה-[PAUSE] כטקסט חדש (כתובית מילת-השאלה יכולה להישאר).
- [ ] **[PAUSE] נשמרו**: אימות ידני שכל 8 ה-[PAUSE 2-3s] מ-narration.md אכן קיימים בטיימליין הסופי כשקט אמיתי (לא נחתכו כ"אוויר מת") — שורות 3, 8, 14a/14b, 19, 24 (אין — ראה הערה), 26, 27a/27b בטבלה. **הערה:** ל-item 3 ול-recap יש שני PAUSE כ"א מפוצלים לשני שוטים (14a/14b, 17a/17b, 27a/27b) — ודאו ששני החלקים יחד נותנים 2-3s שקט רצוף, לא כתובית/SFX חדש שקוטע.
- [ ] **ping-pong loop, לא הקפאה**: כל שוט שבו קליפ AI (4-5s) צריך לכסות VO ארוך יותר (שוטים 3, 8, 14a, 19 ודומיהם) — לוודא שהמימוש הוא **לופ הלוך-ושוב חלק (forward+reverse)**, לא frozen frame על הפריים האחרון (לקח נעול מפרק 001, ראה CLAUDE.md §5).
- [ ] **בועות RECAP**: אימות שקליפ ה-RECAP הורכב לפי התהליך המלא בהערה שבראש הקובץ הזה — Pip-בלבד נשלח ל-avatar-generation, 4 הבועות המקוריות (מהקליפ הנקי המאושר) הורכבו כ-overlay נפרד עם מסכת אלפא, אף בועה לא "דיברה" או סטתה לצורה אחרת.
- [ ] **בדיקת drift חזותי**: כל שוטי ה-AI תואמים ל-character Bible (לפי `ai-visual-consistency`) — אין סטייה בצבע/פרופורציה של Pip בין שוטים; הנחש ב-AI clip שומר על עיניים גדולות/עגולות ופה סגור/חייכן בכל פריים (בלי שיניים חשופות).
- [ ] **מין הנחש בפוטג' האמיתי**: אימות סופי (screenshot + תיעוד ב-footage.md) שהמין הוא corn snake / garter snake / ball python בלבד — לא רק לפי כותרת/תגית, גם ראש לא-משולש ובלי סימני רעלנים אזוריים, לפני נעילה. **חוסם — אל תמשיכו להרכבה עם snake placeholder.**
- [ ] **מין הפיל עקבי**: אימות שהפיל בפוטג' האמיתי הוא מין יחיד ועקבי (לא מונטאז' פיל אפריקאי+הודי) לאורך כל השוט הנבחר.
- [ ] **קוף לא-תוקפני**: אימות חזותי בפוטג' האמיתי שאין bared-teeth threat display ואין מריבה/רדיפה בין קופים (אם קליפ מרובה-קופים נבחר).
- [ ] **אריה לא-תקיפה**: אימות שהפוטג' האמיתי הוא אריה במנוחה/שמורה מוגנת — לא סצנת טרף/דם.
- [ ] **רישיונות SFX ופוטג'**: תיעוד סופי של מקור/רישיון כל קובצי הפוטג' וה-SFX שנבחרו (Pexels/Pixabay) ב-footage.md, כפי שההערות שם דורשות — כולל אישור בפועל שהמשתמש צפה וקיבל כל קליפ (רשת חסומה בסנדבוקס, ראה footage.md).
