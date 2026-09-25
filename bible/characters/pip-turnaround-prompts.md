# Pip — פרומפטים ליצירת דף רפרנס מלא (Turnaround Sheet)

שימוש: הדבק ב-OpenArt (או כל כלי תמונות) יחד עם `pip-reference.jpg` כתמונת רפרנס אם אפשר. כל הפרומפטים בנויים מ: **[פרומפט בסיס קבוע]** + **[סעיף זווית/פריט]** + **[סיומת סגנון]** + **[negative prompt]** — בדיוק לפי עקרון `ai-visual-consistency`. אין לשנות את פרומפט הבסיס בין הזוויות.

---

## A. דף Turnaround מלא — תמונה אחת עם כל הזוויות (הכי מומלץ להתחיל בזה)

```
Character turnaround reference sheet, same character shown from multiple angles in a row: front view, 3/4 view, side profile view, back view — Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft pastel lighting, bright saturated primary colors, simple rounded shapes, no sharp edges, toddler animation style, consistent character design across all views, neutral standing pose, arms at sides, clean flat cream background (#F5E6D3), even studio lighting, orthographic-style character model sheet, high detail, centered composition
```

**Negative prompt:**
```
no text, no watermark, no labels, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no sharp teeth, no dark shadows on face, no inconsistent proportions between views, no color variation between views
```

אם התוצאה לא באמת מציגה 4 זוויות ברורות בתמונה אחת (כלים רבים מתקשים עם זה), עברו לסעיף B — לבקש כל זווית בנפרד.

---

## B. כל זווית בנפרד (מומלץ אם A לא הצליח, או לדיוק מקסימלי)

לכל אחד מהפרומפטים הבאים: התחל תמיד באותו **פרומפט בסיס** (הבלוק הקבוע), החלף רק את שורת הזווית המודגשת.

**פרומפט בסיס קבוע (זהה בכל זווית):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft pastel lighting, bright saturated primary colors, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, clean flat cream background (#F5E6D3), even studio lighting, full body, character model sheet style
```

1. **חזית (Front view):**
   `..., front view, facing camera directly, arms relaxed at sides, neutral standing pose`

2. **פרופיל צד (Side view — right):**
   `..., side profile view facing right, full body silhouette clearly visible, standing pose`

3. **פרופיל צד (Side view — left):**
   `..., side profile view facing left, full body silhouette clearly visible, standing pose`

4. **מבט 3/4 (3/4 view):**
   `..., 3/4 view angle, slightly turned toward camera, standing pose`

5. **גב (Back view):**
   `..., back view, facing away from camera, scarf knot visible on back of neck, standing pose`

(הוסף את ה-negative prompt מסעיף A לכל אחת מהן.)

---

## C. הבגד/אביזר בנפרד — "Prop Sheet" של הצעיף

חשוב לשמור את הצעיף כ"נכס" נפרד — כך שגם אם דמות אחרת/עונה מיוחדת דורשת וריאציה, הצבע/מרקם המדויקים נשמרים.

```
Product-style flat lay illustration of a single scarf, isolated on a plain white background, bright teal fabric (#2EC4B6) with a small white star-shaped patch sewn near one end, soft cartoon material texture, simple rounded shape, no character wearing it, studio product photography style, centered, high detail, toddler animation style asset
```

**Negative prompt:** `no character, no body, no background scene, no text, no watermark`

---

## D. דף הבעות (Expression Sheet) — לשימוש בפרקי A (רגשות)

```
Character expression sheet, same character shown in a grid with 4 different facial expressions: happy smiling, curious wide-eyed, gently worried/scared (eyes squeezed shut, ears flattened, no dark shadows, not terrified), excited/surprised — Pip the quokka, small round toddler-friendly 3D cartoon character, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, consistent character design across all expressions, head and shoulders only, clean flat cream background (#F5E6D3)
```

**Negative prompt:** same as section A, plus `no extreme fear, no crying with tears streaming, no aggressive expression`

---

## הוראות שימוש בפועל

1. שמור את כל הפלטים (turnaround + prop sheet + expression sheet) בתיקייה `bible/characters/assets/` עם שמות ברורים: `pip-front.jpg`, `pip-side-right.jpg`, `pip-back.jpg`, `pip-scarf-prop.jpg`, `pip-expressions.jpg` וכו'.
2. בכלים שתומכים בזה (כמו OpenArt Character) — העלה את כל הסט הזה יחד בתור "reference images" לדמות השמורה, לא רק תמונה אחת. ככל שיש יותר זוויות מאושרות, כלי הווידאו ישמור על עקביות טובה יותר בסצנות תנועה.
3. לעולם אל תיצור זווית חדשה על ידי "לתאר מזיכרון" — תמיד הדבק את פרומפט הבסיס הקבוע מהמסמך הזה, לא ניסוח חדש.
