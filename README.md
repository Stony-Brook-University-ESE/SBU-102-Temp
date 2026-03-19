# SBU 102: Simple Motivational Video Generator

## What This Project Does

A Python application that creates motivational videos with AI-generated scripts and voiceovers, then combines them with a background video to produce a finished MP4 file.

## How This Docker Project Works

| Step | What Happens | Command | File Location | Where It Happens | Result |
|------|-------------|---------|---------------|------------------|---------|
| 1 | **Clean Up** | `docker system prune -f` | run.sh | Your Computer | Removes old Docker files |
| 2 | **Build Image** | `docker build -t motivational-video-generator .` | run.sh | Docker Engine | Creates container with Python + AI tools |
| 3 | **Get API Key** | `read -p "API Key:" GEMINI_API_KEY` | run.sh | Terminal Prompt | You enter your Google Gemini key |
| 4 | **Run Container** | `docker run --rm -i -v $(pwd):/app` | run.sh | Inside Docker | Container starts with your files |
| 5 | **Generate Video** | `python main.py` | Dockerfile | Inside Container | AI creates script → audio → video |
| 6 | **Save Files** | Volume mount saves output | run.sh | Your Computer | Output files saved to your folder |
| 7 | **Cleanup** | `docker rmi motivational-video-generator` | run.sh | Docker Engine | Removes container, keeps your files |

**Simple Command:** Just run `./run.sh` and Docker handles everything automatically!

## Learning Goals

- Use an API key safely (environment variables)
- Run a project in a reproducible Docker environment
- Generate content using AI APIs

## Files in This Project

- `main.py` - Main Python application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions
- `run.sh` - Simple script to build and run the project
- `background.mp4` - Your background video (required)
- `README.md` - This instruction file
- `voiceover.mp3` - Generated audio voiceover  
- `final_video.mp4` - Your finished motivational video

## To-Do List

### Setup Tasks
- [ ] Get your free Google Gemini API key from https://aistudio.google.com/app/apikey
- [ ] Add your `background.mp4` file to the project directory
- [ ] Make sure you have the complete API key (starts with `AIzaSy`)

### Running the Project
- [ ] Make script executable: `chmod +x run.sh`  
- [ ] Run the project: `./run.sh`
- [ ] Enter API key when prompted
- [ ] Enter your motivational topic when asked
- [ ] Check your generated `final_video.mp4`

### Optional Improvements
- [ ] Try different background videos
- [ ] Experiment with different motivational topics
- [ ] Test with shorter/longer topics

---

## Quick Start Guide

### Step 1: Get Your FREE Google Gemini API Key

1. **Visit Google AI Studio**: https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Create API key** → "Create API key in new project"
4. **Copy your API key** (starts with `AIzaSy`)

### Step 2: Add Your Background Video

You need a `background.mp4` file in this directory.

**Quick options:**
- Download from [Pixabay](https://pixabay.com/videos/) or [Pexels](https://www.pexels.com/videos/)
- Record a 10-30 second video with your phone
- Use any MP4 video you have (just rename it to `background.mp4`)

**Important:** File must be named exactly `background.mp4` in the same folder as `main.py`

### Step 3: Run the Project

Make the script executable and run it:
```bash
chmod +x run.sh
./run.sh
```

**The script will:**
1. Build the Docker container
2. **Prompt you to enter your API key** (it will be visible when you type)
3. Run the application
4. Ask for your motivational topic
5. Generate your video!

**Important:** When entering your API key, make sure you paste the complete key from Google AI Studio.

### Step 4: Check Your Results

After completion, you'll have:
- `script.txt` - Your AI-generated script
- `voiceover.mp3` - The audio narration
- `final_video.mp4` - Your finished motivational video

**To download:** Right-click on `final_video.mp4` → Download

---

## Troubleshooting

**Docker not found?** Make sure you're in a GitHub Codespace or have Docker installed.

**API key errors?** 
- Double-check your key starts with `AIzaSy` 
- Make sure you copied the complete key from https://aistudio.google.com/app/apikey
- Try generating a new API key if the old one doesn't work

**No background.mp4?** The file must exist and be named exactly `background.mp4`.

**Permission denied on run.sh?** Run: `chmod +x run.sh`

**Docker build issues?** Clean up first: `docker system prune -f` then try again.

**Container errors?** Try rebuilding: `docker build -t motivational-video-generator . && ./run.sh`

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

## Troubleshooting

**Docker not found?** Make sure you're in a GitHub Codespace or have Docker installed.

**API key errors?** 
- Double-check your key starts with `AIzaSy` 
- Make sure you copied the complete key from https://aistudio.google.com/app/apikey
- Try generating a new API key if the old one doesn't work

**No background.mp4?** The file must exist and be named exactly `background.mp4`.

**Permission denied on run.sh?** Run: `chmod +x run.sh`

**Docker build issues?** Clean up first: `docker system prune -f` then try again.

**Container errors?** Try rebuilding: `docker build -t motivational-video-generator . && ./run.sh`

## Your Generated Files

After running successfully, you'll have:
- `script.txt` - Your AI-generated motivational script
- `voiceover.mp3` - The AI-generated audio narration  
- `final_video.mp4` - Your finished motivational video

**Tip:** To keep multiple videos, rename them after each run:
```bash
mv final_video.mp4 my_motivation_video_1.mp4
```

---

## Understanding .sh vs .yml: Which Tool for Which Job?

| Aspect | Bash Script (.sh) | Docker Compose (.yml) |
|--------|-------------------|----------------------|
| **What** | Shell commands in a file | Declarative container configuration |
| **How** | `chmod +x run.sh && ./run.sh` | `docker compose up --build` |
| **Why Use** | Simple automation, custom logic | Professional container orchestration |
| **When Use** | Quick scripts, complex workflows | Multi-container apps, team projects |

### Simple Examples

#### Bash Script Example (.sh)
```bash
#!/bin/bash
echo "Building image..."
docker build -t myapp .
echo "Running container..."
docker run --rm myapp
```

#### Docker Compose Example (.yml)
```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
```

### Pros and Cons

| Feature | Bash Script | Docker Compose |
|---------|-------------|----------------|
| **Learning Curve** | Easy for beginners | Requires YAML knowledge |
| **Flexibility** | Very flexible, any logic | Structured, container-focused |
| **Team Sharing** | Platform dependent | Works everywhere |
| **Industry Standard** | Good for automation | Standard for containers |
| **Error Handling** | Manual error handling | Built-in container management |
| **Documentation** | Comments in code | Self-documenting structure |

---

## Homework Challenge: Convert to Docker Compose

**Question:** Can we replace the `run.sh` bash script with a `docker-compose.yml` file?

**Answer:** YES! Docker Compose is actually the more professional way to manage Docker applications.

### Your Assignment

Create a `docker-compose.yml` file that does the same job as `run.sh`. This will teach you industry-standard container orchestration.

### What You Need to Convert

Currently `run.sh` does these steps:
1. Clean up old containers: `docker system prune -f`
2. Build image: `docker build -t motivational-video-generator .`
3. Get API key from user input
4. Run container: `docker run --rm -i -v $(pwd):/app -e GEMINI_API_KEY="$API_KEY" motivational-video-generator`
5. Clean up: `docker rmi motivational-video-generator`

### Hints for Your docker-compose.yml

```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    stdin_open: true
    tty: true
```

### Challenge Requirements

1. **Create** `docker-compose.yml` that builds and runs the app
2. **Test** that `docker compose up --build` works
3. **Compare** the command simplicity:
   - Old way: `./run.sh` (but script has 30+ lines)
   - New way: `GEMINI_API_KEY="your-key" docker compose up --build`

### Bonus Points

- How would you handle the cleanup automatically?
- Can you make the API key input more user-friendly?
- What other Docker Compose features could improve this project?

### Expected Learning Outcomes

After completing this homework, you should understand:
- Docker Compose vs bash scripts for container management
- YAML syntax for defining services
- Environment variable handling in containers
- Volume mounting for file sharing
- When to use Compose vs single containers

**Time Estimate:** 30-60 minutes  
**Difficulty:** Intermediate  
**Submit:** Your working `docker-compose.yml` file

### Solution Testing

Your solution works if:
1. `docker compose up --build` builds the image
2. The container runs and asks for motivational topic
3. Video files are created in your host directory
4. Container stops cleanly after completion

Good luck!
