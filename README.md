# Cry Wolf 🐺

Everyone has heard the story where a kid keeps shouting 'the wolf has come!!!' 
every night. But the wolf never comes, until it did. We all know how that story ends.

Inspired by that story, Cry Wolf detects false urgency from real urgency. It is
for anyone curious to know if their colleagues, friends, or family are being 
cry wolves, or if the urgency is actually real.

built using Gemini.

---

## What it detects

- **No Urgency** — nothing to see here
- **False Urgency** — manufactured panic is scored and explained
- **Real Urgency** — genuine deadline, real consequence
- **Real Urgency with Suspicion** — technically urgent, probably a scam

---

## Tech Stack

- Python
- Google Gemini API (with fallback)
- FastAPI
- Streamlit

---

## Run it locally

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Add your Gemini API key to a `.env` file: `GEMINI_API_KEY=your_key`
5. Run: `streamlit run app.py`

---

## How it works

Paste any text — an email, a WhatsApp message, a tweet, a sales pitch. 
Cry Wolf analyses it across five false urgency metrics and one real urgency 
checklist, then delivers a verdict in the driest British accent possible.