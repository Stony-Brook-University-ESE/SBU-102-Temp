#!/usr/bin/env python3
"""
Test script to verify Docker setup and dependencies work
Run this before using your OpenAI API key
"""

import sys
import os

def test_imports():
    """Test that all required packages can be imported"""
    print("Testing Python package imports...")
    
    try:
        import moviepy
        print("✓ MoviePy imported successfully")
    except ImportError as e:
        print(f"✗ MoviePy import failed: {e}")
        return False
    
    try:
        import google.generativeai
        print("✓ Google Generative AI package imported successfully")
    except ImportError as e:
        print(f"✗ Google Generative AI package import failed: {e}")
        return False
    
    try:
        import gtts
        print("✓ gTTS (Google Text-to-Speech) imported successfully")
    except ImportError as e:
        print(f"✗ gTTS import failed: {e}")
        return False
    
    return True

def test_ffmpeg():
    """Test that ffmpeg is available"""
    print("Testing ffmpeg availability...")
    
    import subprocess
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ ffmpeg is available")
            return True
        else:
            print("✗ ffmpeg returned error code")
            return False
    except FileNotFoundError:
        print("✗ ffmpeg not found")
        return False

def test_background_video():
    """Check if background video exists"""
    print("Checking for background video...")
    
    if os.path.exists('background.mp4'):
        print("✓ background.mp4 found")
        return True
    else:
        print("✗ background.mp4 not found")
        print("  Please add a background video file named 'background.mp4'")
        print("  See BACKGROUND_VIDEO_SETUP.md for instructions")
        return False

def test_api_key():
    """Check if API key is set"""
    print("Checking API key configuration...")
    
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key and api_key != 'your-gemini-api-key-here':
        print("✓ GEMINI_API_KEY environment variable is set")
        return True
    else:
        print("✗ GEMINI_API_KEY not properly configured")
        print("  Set it with: export GEMINI_API_KEY='your-key-here'")
        print("  Or create a .env file with your API key")
        return False

def main():
    print("=== Motivational Video Generator Setup Test ===")
    print()
    
    tests = [
        ("Package Imports", test_imports),
        ("FFmpeg Availability", test_ffmpeg),
        ("Background Video", test_background_video),
        ("API Key Configuration", test_api_key)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"--- {test_name} ---")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("=== Test Summary ===")
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! You're ready to generate videos.")
        sys.exit(0)
    else:
        print("✗ Some tests failed. Please fix the issues above before continuing.")
        sys.exit(1)

if __name__ == "__main__":
    main()