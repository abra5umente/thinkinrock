# ThinkinRock

**A playful Python script to wake up your "thinkin' rock" (Stable Diffusion via auto1111) and conjure images for you, automatically managing container or batch launch, prompt input, and image saving.**

---

## 🚀 What it does
- Starts auto1111 via .bat if not already running.
- Prompts you for what you want the "rock" to imagine.
- Calls the `txt2img` API on your local auto1111 instance.
- Saves the generated image to your specified folder or the current directory with a timestamped filename.
- Shuts down auto1111 if it wasn't running before.

---

## 🛠 Requirements
- Python 3.11+
- `requests` and `python-dotenv` installed (`pip install -r requirements.txt`)
- A working [Automatic1111 (Stable Diffusion WebUI)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) instance accessible locally.
- A `.env` (example included) file containing optional config overrides:
  ```env
  SAMPLER_NAME=DPM++ 2M SDE
  SCHEDULER_NAME=Karras
  IMAGE_WIDTH=1024
  IMAGE_HEIGHT=1024
  CFG_SCALE=4.5
  STEPS=30
  ```

---

## ⚡️ Usage
1️⃣ Clone the repository:
```bash
git clone https://github.com/abra5umente/thinkinrock.git
cd thinkinrock
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Ensure your `.env` file is set up if you want custom values.

4️⃣ Run the conjurer:
```bash
python thinkinrock.py
```

5️⃣ Enter your prompt and watch the rock think.


---

## 🧩 Features to add
- Ability to auto-generate prompts using OpenAI, Gemini, etc

Contributions are welcome via issues and pull requests!

---

## 📜 License
MIT

---

