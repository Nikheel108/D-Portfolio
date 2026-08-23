# Nikheel C K — Google Sites Portfolio (Notebook / Kernel edition)

Your portfolio, rebuilt around one idea: **it's a running notebook.** Every section is a
numbered `In[ ]:` cell that "executes" as you scroll, your grades render as Python dict
output, Education reads like `git log`, and the floating chat button is framed as **"the
kernel"** — a small rule-based assistant that answers questions about you. Continuous
cell numbering runs `In[1]` through `In[11]` across all seven pages, so the whole site
reads as one notebook, not seven disconnected pages.

## What you got

| File | What it is |
|---|---|
| `style.css` | The entire design system (colors, type, components, animations) |
| `app.js` | All behavior — nav, theme toggle, scroll-reveal, typing effect, counters, the kernel chatbot, contact form |
| `home.html` … `contact.html` | The 7 page snippets you paste into Google Sites |

**Why two shared files instead of everything inline?** Each Google Sites "Embed code"
block is its own little sealed page (technically its own iframe). If every page carried
its own full copy of the CSS/JS, you'd have ~2,500 duplicated lines and updating the
design later would mean editing all 7 files. Instead, the 7 HTML files are short and just
*point to* `style.css` and `app.js`, hosted once. You already have a live GitHub Pages
site (`Digital-Portfolio`), so that's where they'll live.

---

## Step 1 — Host the shared CSS/JS on your existing GitHub repo

1. Go to your `Digital-Portfolio` repo on github.com.
2. Click **Add file → Create new file**.
3. For the filename, type `gsite/style.css` (the `gsite/` makes GitHub create a folder automatically). Paste in the full contents of `style.css`. Commit.
4. Repeat: **Add file → Create new file**, name it `gsite/app.js`, paste in `app.js`. Commit.
5. Wait about a minute, then open these two URLs directly in a browser tab to confirm they load (you should see raw CSS/JS text, not a 404):
   - `https://nikheel108.github.io/Digital-Portfolio/gsite/style.css`
   - `https://nikheel108.github.io/Digital-Portfolio/gsite/app.js`

Your current GitHub Pages portfolio keeps working exactly as before — you're only adding two new files, not touching the existing pages.

## Step 2 — Build the page structure in Google Sites

1. Go to [sites.google.com](https://sites.google.com) → create a new site.
2. In the right-hand **Pages** panel, add 7 pages named: `Home`, `About`, `Skills`, `Projects`, `Education`, `Achievements`, `Contact`. The name you give each page becomes part of its URL.
3. For **each page**, open its page settings (⋮ menu next to the page name) and set **Header type → None/Minimal** if available, so Google's own title banner doesn't sit above your custom toolbar.
4. Click **Publish** once now, even with empty pages — you need real, live URLs before you can wire up the navigation.

## Step 3 — Collect your 7 page URLs

Open your published site, visit each of the 7 pages, and copy the URL from the address bar into a note. You'll get something like:

```
Home         → https://sites.google.com/view/yoursitename/home
About        → https://sites.google.com/view/yoursitename/about
Skills       → https://sites.google.com/view/yoursitename/skills
Projects     → https://sites.google.com/view/yoursitename/projects
Education    → https://sites.google.com/view/yoursitename/education
Achievements → https://sites.google.com/view/yoursitename/achievements
Contact      → https://sites.google.com/view/yoursitename/contact
```

## Step 4 — Replace the placeholders

Every one of the 7 HTML files has the same 7 navigation placeholders (because the nav bar
repeats on every page). Open each file in any text editor and **find-and-replace all 7**,
using the URLs from Step 3:

| Placeholder | Replace with |
|---|---|
| `{{URL_HOME}}` | your Home page URL |
| `{{URL_ABOUT}}` | your About page URL |
| `{{URL_SKILLS}}` | your Skills page URL |
| `{{URL_PROJECTS}}` | your Projects page URL |
| `{{URL_EDUCATION}}` | your Education page URL |
| `{{URL_ACHIEVEMENTS}}` | your Achievements page URL |
| `{{URL_CONTACT}}` | your Contact page URL |
| `{{FORMSPREE_ENDPOINT}}` | *(contact.html only — see Step 5)* |

Tip: paste each file into Google Docs or VS Code and use Find & Replace (`Ctrl/Cmd+H`) —
7 replacements × 7 files, but each replacement is identical everywhere it appears, so it's
quick.

## Step 5 — Make the contact form actually send (optional but recommended)

Google Sites can't run a backend, so the form needs a small free service to deliver the
email:

1. Go to [formspree.io](https://formspree.io) → sign up free → **New Form**.
2. Copy the endpoint it gives you, e.g. `https://formspree.io/f/abcdwxyz`.
3. In `contact.html`, replace `{{FORMSPREE_ENDPOINT}}` with that URL.

**If you skip this**, the form still works — clicking "send --message" just opens the
visitor's email app pre-filled with their message instead of submitting silently. That
fallback is already built in, so nothing breaks either way.

## Step 6 — Embed each page

For each of the 7 Google Sites pages:

1. Click **Insert → Embed → Embed code** tab (⚠️ not "By URL" — that tab only accepts a
   single external link, not full HTML/CSS/JS).
2. Paste the **entire contents** of the matching `.html` file (after you've done the
   find-and-replace).
3. Click **Insert**.
4. Drag the embed block's corner handles to full page width, and pull the bottom edge
   down until the internal scrollbar disappears. Starting heights that work well:

   | Page | Suggested height |
   |---|---|
   | Home | ~850px |
   | About | ~900px |
   | Skills | ~950px |
   | Projects | ~1500px |
   | Education | ~1150px |
   | Achievements | ~950px |
   | Contact | ~1500px |

5. Publish (or **Republish**) after each page, and check it on your phone too — everything
   is responsive down to small screens.

---

## The AI feature: "the kernel"

The floating `>_` button is a genuine feature, not a decoration — it's a small rule-based
assistant, entirely client-side, that recognizes questions about your skills, projects,
education, achievements, contact info, and resume, and answers in a terminal-style panel
with a typewriter effect. It costs nothing to run and needs no setup.

**Why not a real LLM-backed chatbot?** That would need an API key, and Google Sites embeds
run entirely in the visitor's browser — anything you paste in is visible via "view source."
Pasting a real API key into this code would let anyone extract and misuse it. If you want
to upgrade to a genuine AI-powered version later, that requires a small backend (e.g. a
free Cloudflare Worker or Vercel function) that holds the key server-side and the embed
calls *that* instead — happy to help you build that as a separate step whenever you want it.

## Swapping content later

- **Photos/resume**: they're pulled straight from your existing repo (`images/profile.jpg`,
  `images/project1.png`, `images/project3.png`, `assets/resume.pdf`). Replace those same
  files in `Digital-Portfolio` on GitHub and every page updates automatically.
- **Text/colors/animations**: everything lives in `style.css` and `app.js`. Edit those two
  files on GitHub and all 7 pages update at once — no need to touch Google Sites again.
- **Color palette** is set as CSS variables at the top of `style.css` (`--amber`, `--teal`,
  `--bg`, etc.) if you ever want to retheme.

## Troubleshooting

- **Page looks unstyled (plain black text, no fonts/icons)** — the two GitHub URLs from
  Step 1 aren't loading yet. Open them directly in a browser tab; GitHub Pages can take a
  minute after a commit.
- **Nav links go nowhere / refresh the same page** — a placeholder wasn't replaced. Search
  the pasted code for `{{` — if you find any, that one's still a placeholder.
- **Scrollbar inside the embed box** — the embed height is too short; drag it taller (Step 6).
- **Mobile hamburger menu doesn't open** — the `app.js` `<script>` tag got stripped. Re-check
  you used the **Embed code** tab, not "By URL".
- **Form always falls back to opening email app** — `{{FORMSPREE_ENDPOINT}}` wasn't replaced
  with your real Formspree URL (Step 5).

Your original GitHub Pages site keeps running independently the whole time — this is a
second, parallel version, so there's no risk to what's already live.
