# prompts

**פרק 001 — Real Animal Sounds: Farm Edition** | פורמט B | יחס תמונה: 16:9 (פרק מלא, לא Short)

## קבועים (לשימוש מילולי בכל פרומפט למטה — לפי `ai-visual-consistency`)

**Pip base prompt (verbatim, `bible/characters/pip.md` §4):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design
```

**Style suffix (verbatim, `bible/style-bible.md`):**
```
, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
```

**Negative prompt block (verbatim, `bible/style-bible.md`):**
```
no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**Pip's Meadow home-base environment prompt (verbatim, `bible/locations/pips-meadow.md`) — לשימוש בכל סצנה שבה Pip "בבית" (OPEN/RECAP/CLOSE):**
```
Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated colors, simple rounded shapes, consistent background design
```

כל פרומפט למטה בנוי לפי התבנית: `[Pip base prompt] + [action/scene clause] + [style suffix] + Negative prompt: [negative block]`. עבור סצנות "בית" — [action/scene clause] כולל את מחרוזת הסביבה הקבועה למעלה, מילה במילה, לא ניסוח חופשי. השתמשו ב-Character asset שמור של Pip (OpenArt Character) במקום להקליד את התיאור מחדש, כשהכלי תומך בכך — הטקסט המלא נשמר כאן כגיבוי/פולבק ולבדיקת עקביות.

**הערה על תמונת רפרנס לסביבה:** לפי `bible/locations/pips-meadow.md`, עדיין לא אושרה תמונת רפרנס נעולה לסביבה (רק פרומפט טקסטואלי). מומלץ להריץ קודם את פרומפט ה-OPEN למטה, לאשר את התוצאה, ולשמור אותה כרפרנס/Character-asset-נלווה לפני שממשיכים ל-RECAP ו-CLOSE — כדי שכל שלוש הסצנות "בבית" יתבססו על אותה תמונה מאושרת, לא רק על אותו טקסט.

---

## OPEN — Pip's Meadow, home base

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, wiggling his nose three times, big excited eyes looking straight at camera, welcoming pose, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest
```

**⚠️ זו הפעם הראשונה שהסביבה נוצרת — שמור את התוצאה כתמונת הרפרנס הרשמית של "Pip's Meadow" ב-`bible/locations/assets/` ועדכן את הסטטוס ב-`pips-meadow.md`, לפני שממשיכים ל-RECAP ו-CLOSE, כדי ששלושתם יתבססו על אותה סביבה מאושרת.**

**(2) Image→Video prompt (motion: signature nose-wiggle x3, then wave):**
```
Animate this exact image of Pip in Pip's Meadow: Pip wiggles his nose three quick times (signature gesture), eyes widening with excitement on each wiggle, then breaks into a warm wave toward camera with one paw, gentle idle sway of the scarf in a light breeze, soft bounce on his feet, camera holds a static friendly medium shot, no camera shake, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-open-pip-meadow.png` / `001-open-pip-meadow.mp4`

---

## ITEM 1 — COW

**(1) Image prompt (Pip + AI-cartoon cow together):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a cheerful cartoon farm field with a wooden fence and soft green grass, pointing excitedly at a friendly round cartoon cow beside him — the cow has big gentle eyes, black-and-white patches, a soft rounded 3D-cartoon body matching Pip's art style, both characters facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**(2) Image→Video prompt (motion: point, cow moos, Pip reacts):**
```
Animate this exact image: Pip points at the cartoon cow with one paw and leans forward, curious; the cow tilts its head and opens its mouth in a big friendly "MOO" (mouth shape, no audio needed in prompt), Pip's ears perk up and he nods along, then Pip wiggles his nose three times before turning back to camera, gentle grass sway in background, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-item1-cow-ai.png` / `001-item1-cow-ai.mp4`

**חלופה לתיקון בטיימליין (alt, לשימוש אם התוצאה הראשונה לא עומדת בבדיקת drift):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, sitting on a round hay bale next to a small round cartoon cow with big friendly eyes and soft black-and-white patches, both smiling at camera, simple wooden barn silhouette softly blurred in background, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

---

## ITEM 2 — SHEEP

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a soft green cartoon pasture with round fluffy clouds in the sky, next to a friendly round cartoon sheep with a thick fluffy cotton-like wool coat, gentle eyes, small dark hooves, soft rounded 3D-cartoon body matching Pip's art style, both facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**(2) Image→Video prompt (motion: sheep bleats, Pip giggles at wool-cloud detail):**
```
Animate this exact image: the fluffy cartoon sheep bounces gently in place and opens its mouth in a soft "BAA", Pip wiggles his nose three times, tilts his head toward the sheep's wool, giggles softly and points up comparing the wool to the fluffy clouds overhead, camera holds a static warm medium shot, gentle cloud drift in background, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-item2-sheep-ai.png` / `001-item2-sheep-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, walking beside a small round fluffy cartoon sheep on a grassy hill, low wooden fence in the background, warm afternoon light, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

---

## ITEM 3 — CHICKEN

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a sunny cartoon farmyard with soft dirt ground and a few scattered seeds, beside a friendly round cartoon hen (chicken) with soft white and brown feathers, a small rounded comb, gentle eyes, pecking at the ground, soft rounded 3D-cartoon body matching Pip's art style, both facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**(2) Image→Video prompt (motion: chicken pecks and clucks, Pip mimics rhythm):**
```
Animate this exact image: the cartoon hen pecks the ground twice in a gentle rhythmic bob and opens its beak in a soft "CLUCK", Pip wiggles his nose three times and bobs his head playfully in the same rhythm as the hen, then turns to camera smiling, a couple of loose feathers drift softly in the background, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-item3-chicken-ai.png` / `001-item3-chicken-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, crouching down to look at a small round cartoon hen pecking near a wooden coop, soft morning light, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

---

## ITEM 4 — PIG

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing at the edge of a clean cartoon pen with a small patch of soft rounded mud, next to a friendly round cartoon pig with pink skin, a curly tail, a round snout, gentle eyes, soft rounded 3D-cartoon body matching Pip's art style, both facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**(2) Image→Video prompt (motion: pig wiggles snout and oinks, tail curls):**
```
Animate this exact image: the cartoon pig wiggles its round snout and curly tail spins playfully once while it opens its mouth in a soft "OINK", a few small soft mud bubbles pop gently nearby, Pip wiggles his nose three times back at the pig, then laughs softly and turns to camera, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-item4-pig-ai.png` / `001-item4-pig-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, leaning on a low wooden pen fence looking at a small round pink cartoon pig sitting in a clean soft mud patch, warm afternoon light, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

---

## RECAP — Pip's Meadow, home base, with 4 animal icons

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, four small simple round cartoon icons floating gently around Pip at chest height — a cow, a sheep, a chicken, and a pig, each matching the art style of their earlier scenes, evenly spaced, Pip smiling at camera pointing at the icons one by one, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest
```

**(2) Image→Video prompt (motion: Pip points to each icon in turn as its sound is said):**
```
Animate this exact image: Pip points to the cow icon as "moo" is heard, then the sheep icon as "baa" is heard, then the chicken icon as "cluck" is heard, then the pig icon as "oink" is heard, each icon gently bounces once when pointed at, Pip's expression stays warm and encouraging throughout, camera holds a static friendly medium shot, smooth toddler-paced motion, duration 5-6 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-recap-pip-meadow.png` / `001-recap-pip-meadow.mp4`

---

## CLOSE — Pip's Meadow, home base

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, waving one paw at camera, warm happy closing expression, golden late-afternoon light, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest
```

**(2) Image→Video prompt (motion: wave + nose-wiggle x3 sign-off):**
```
Animate this exact image of Pip in Pip's Meadow: Pip waves warmly at camera with one paw for about a second, then wiggles his nose three quick times (signature closing gesture), eyes crinkling with a happy gentle smile, soft idle sway of the scarf in a light breeze, camera holds a static friendly medium shot, no camera shake, gentle fade-ready final frame, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing
```

**(3) קובץ:** `001-close-pip-meadow.png` / `001-close-pip-meadow.mp4`

---

## הערות למפיק/עורך

- כל 6 הפריטים (open, cow, sheep, chicken, pig, close) משתמשים במחרוזת הבסיס המדויקת של Pip מ-`bible/characters/pip.md` §4, ללא כל שינוי מילה — לפי כלל 3 ב-`ai-visual-consistency`. מומלץ להשתמש ב-Character asset שמור של Pip ב-OpenArt (כלל 1 בסקיל) כשמפיקים בפועל, ולא רק בתיאור הטקסטואלי.
- כל וידאו הוא image-to-video (כלל 7 בסקיל) מהתמונה הנעולה של אותה סצנה, לא text-to-video עצמאי.
- משך כל שוט ≤6 שניות (4-5s כאן), בהתאם לחוקי הקצב ל-toddlers.
- אם תוצאה סוטה מה-Bible (צבע, יחס ראש-גוף, צעיף חסר) — יש להשתמש בפרומפט החלופי ולהתחיל מחדש מהבסיס הקבוע, לא "לתקן" תוצאה שגויה (regenerate, not patch — לפי הסקיל).
