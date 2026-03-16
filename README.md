# SBU 102: Motivational Video Generator with Docker

## What This Project Does

A Python application that creates motivational YouTube videos with AI-generated scripts and voiceovers, then combines them with a background video to produce a finished MP4 file.

## Learning Goals (SBU 102 - Week 7 API Style)

- Use an API key safely (environment variables, not hardcoding secrets)
- Run a project in a reproducible environment (Docker container)
- Treat the app like an API client: input -> request -> output artifacts

## Files in This Project

- `main.py` - Main Python application that runs the workflow
- `requirements.txt` - Python dependencies (openai, moviepy)
- `Dockerfile` - Container build instructions
- `docker-compose.yml` - One-command runner for students
- `.env.example` - Template for environment variables
- `.gitignore` - Prevents sensitive files from being committed
- `background.mp4` - Input background video (you need to provide this)

## Output Files Created by the Script

- `script.txt` - Generated motivational script
- `voiceover.mp3` - Generated audio voiceover  
- `final_video.mp4` - Final combined video

---

## IMPORTANT: Get Your Google Gemini API Key First (FREE!)

Great news! This project uses Google's Gemini AI which has a very generous FREE tier - perfect for university students. You won't need to pay anything!

### How to Create a FREE Gemini API Key

1. **Go to Google AI Studio**
   - Visit: https://aistudio.google.com/app/apikey
   - Sign in with your Google account (use your university account if you have one)

2. **Create Your Free API Key**
   - Click **"Create API key"** button
   - Select **"Create API key in new project"** (recommended)
   - Your API key will be generated instantly

3. **Copy Your API Key**
   - Copy the key immediately and save it somewhere safe
   - The key looks like: `AIzaSyA...` (starts with AIzaSy)
   - You can always come back to view it later

4. **Why Gemini is Better for Students**
   - **Completely FREE** with generous daily limits
   - No credit card required
   - Perfect for educational projects
   - Very fast and high-quality responses
   - Much more accessible than paid alternatives

### Security Reminder
- **Never share your API key with others**
- **Never paste it directly into code files**
- **Never commit it to GitHub**
- We'll show you how to use it safely with environment variables below

---

## Step-by-Step Instructions for Students

### Step 0: Open the Repository in GitHub Codespaces

1. Open this GitHub repository in your web browser
2. Click the green **Code** button
3. Click **Codespaces** tab
4. Click **Create codespace on main**
5. Wait for the Codespace to finish setting up (this may take 2-3 minutes)

### Step 1: Confirm Docker is Available

Once your Codespace is ready, open the terminal and run these commands to verify Docker is installed:

```bash
docker --version
docker compose version
```

Both commands should print version numbers. If they do, you're ready to proceed.

### Step 2: Add Your Background Video

You need to provide a background video file for your motivational video.

1. **Option A: Upload a file**
   - Drag and drop a video file into the VS Code file explorer
   - Rename it to exactly `background.mp4`

2. **Option B: Use a sample video (for testing)**
   - Find a short video online (10-30 seconds is good for testing)
   - Download it and rename it to `background.mp4`
   - Place it in the root directory of the project

**Important:** The file must be named exactly `background.mp4` and be in the same folder as `main.py`.

### Step 3: Set Up Your FREE Gemini API Key

You already got your API key from https://aistudio.google.com/app/apikey in the first section. Now let's set it up securely.

### Step 4: Set Up Your API Key (Choose One Method)

**Method A: Environment Variable (Temporary)**

In the Codespace terminal, run:
```bash
export GEMINI_API_KEY="paste-your-actual-key-here"
```

To verify it's set correctly:
```bash
echo $GEMINI_API_KEY
```

**Method B: Environment File (Recommended)**

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file:
   ```bash
   code .env
   ```

3. Replace `your-gemini-api-key-here` with your actual API key
4. Save the file (Ctrl+S)

**Important Security Notes:**
- Never paste your API key directly into `main.py`
- The `.env` file is automatically ignored by git (won't be committed)
- If you close the Codespace, you may need to set the environment variable again
- **Good news:** No payment required - Gemini API is free for students!

### Step 5: Build the Docker Container

This step installs Python, ffmpeg, and all the required dependencies inside a container:

```bash
docker compose build
```

This will take a few minutes the first time. You'll see it downloading and installing:
- Python 3.11
- ffmpeg (for video processing)
- Google Generative AI library (Gemini)
- gTTS (Google Text-to-Speech - also free!)
- MoviePy (for video editing)

### Step 5.5: Test Your Setup (Optional but Recommended)

Before using your API credits, test that everything is configured correctly:

```bash
docker compose run --rm test
```

This will check:
- Python packages are installed correctly
- ffmpeg is working
- Your background video file exists  
- Your API key is configured

Fix any issues before proceeding to the next step.

### Step 6: Run the Application

Now run your motivational video generator:

```bash
docker compose run --rm app
```

**What happens next:**

1. The program will ask you for a motivational topic
2. Type something like "overcoming challenges" or "staying focused" and press Enter
3. The program will:
   - Generate a motivational script using Google Gemini AI (free!)
   - Create a voiceover using Google Text-to-Speech (also free!)
   - Combine the audio with your background video
   - Save the final MP4 file

### Step 7: Check Your Results

After the program finishes successfully, you should see these new files in your project folder:

- `script.txt` - The AI-generated motivational script
- `voiceover.mp3` - The AI-generated audio voiceover
- `final_video.mp4` - Your finished motivational video

**To download your video:**
1. Right-click on `final_video.mp4` in the VS Code file explorer  
2. Select **Download**

**To preview your video:**
1. Click on `final_video.mp4` in the file explorer
2. It should open a video player in VS Code

### Step 8: Create More Videos

To create another video with a different topic:

```bash
docker compose run --rm app
```

Each time you run this command, it will overwrite the previous files, so download any videos you want to keep before running it again.

---

## Troubleshooting Common Issues

### "API key missing" error
- **Solution:** Re-run the export command: `export GEMINI_API_KEY="your-key"`  
- **Or:** Check that your `.env` file exists and contains the correct key

### "background.mp4 not found" error  
- **Solution:** Make sure the file is named exactly `background.mp4` (all lowercase)
- **Solution:** Make sure the file is in the root directory (same level as `main.py`)

### "Permission denied" or Docker errors
- **Solution:** Try running: `sudo docker compose build`
- **Solution:** Restart the Codespace if Docker seems unresponsive

### MoviePy or ffmpeg errors
- **Solution:** Rebuild the container: `docker compose build --no-cache`
- **Solution:** Make sure your background video file isn't corrupted

### Slow performance
- **Normal:** The first build takes several minutes
- **Normal:** Video processing can take 1-2 minutes depending on video length
- **Tip:** Use shorter background videos (10-30 seconds) for faster testing

### Out of API credits
- **Great News:** This shouldn't happen! Gemini API has a generous free tier
- **Check:** Your usage at https://aistudio.google.com/app/apikey
- **Solution:** The free tier should be more than enough for this project

---

## What Students Should NOT Do

- **Do not** paste API keys directly into `main.py`
- **Do not** commit `.env` files to GitHub  
- **Do not** install Python packages manually (Docker handles this)
- **Do not** edit the Dockerfile unless instructed

## What Students Should Edit

- The topic they enter when prompted
- The `background.mp4` file (try different background videos)
- **Advanced:** Modify `main.py` to change the TTS language (line 64: change 'en' to 'es', 'fr', 'de', etc.)

---

## Technical Details (For Instructors)

### Container Architecture
- **Base Image:** `python:3.11-slim`
- **System Dependencies:** `ffmpeg` (required by MoviePy)
- **Volume Mount:** Current directory mounted to `/app` for file I/O
- **Environment:** `OPENAI_API_KEY` passed from host to container

### API Usage
- **Text Generation:** Google Gemini 1.5 Flash (generates motivational scripts - FREE!)
- **Audio Generation:** Google Text-to-Speech (gTTS - also FREE!)
- **Estimated Cost:** $0.00 - Completely free for students!

### Dependencies
- `google-generativeai>=0.3.0` - Google Gemini AI client library
- `gTTS>=2.3.0` - Google Text-to-Speech (free)
- `moviepy>=1.0.3` - Video editing and processing

### File Flow
1. **Input:** `background.mp4` (user provided)
2. **Generated:** `script.txt` (AI-generated text)
3. **Generated:** `voiceover.mp3` (AI-generated audio)  
4. **Output:** `final_video.mp4` (combined result)

This project demonstrates API integration, containerization, and media processing in a practical, engaging way for students.

---

## Quick Reference Commands

```bash
# Build the container (first time only)
docker compose build

# Test your setup (recommended before first run)
docker compose run --rm test

# Run the video generator
docker compose run --rm app

# Rebuild container (if you change requirements.txt)
docker compose build --no-cache

# Set API key (if not using .env file)
export GEMINI_API_KEY="your-key-here"

# Check API key is set
echo $GEMINI_API_KEY
```

## Files Created Each Run

- `script.txt` - Keep or rename before next run
- `voiceover.mp3` - Keep or rename before next run  
- `final_video.mp4` - Keep or rename before next run

**Tip:** To keep multiple videos, rename them after each run:
```bash
mv final_video.mp4 my_motivation_video_1.mp4
```
