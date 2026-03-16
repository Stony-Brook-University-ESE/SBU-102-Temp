# Sample Background Video Instructions

Since you need a background.mp4 file to run the application, here are some quick options:

## Option 1: Download a Free Sample Video
- Visit: https://pixabay.com/videos/ or https://www.pexels.com/videos/
- Search for "abstract" or "background" videos
- Download a short video (10-30 seconds)
- Rename it to "background.mp4"
- Place it in this project folder

## Option 2: Use Your Phone
- Record a 10-30 second video of anything (sky, nature, etc.)
- Transfer it to your computer
- Rename it to "background.mp4"
- Upload it to this project

## Option 3: Create a Simple Test Video
If you have ffmpeg installed, you can create a test video:

```bash
ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 -pix_fmt yuv420p background.mp4
```

**Remember:** The file must be named exactly "background.mp4" (all lowercase) and placed in the same directory as main.py