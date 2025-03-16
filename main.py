import subprocess
import RPi.GPIO as GPIO
import time

# Paths for clarity
PHOTO_CMD = ["python3", "/home/pi3b/Cornerstone/takephoto.py"]
ANALYZE_CMD = ["/home/pi3b/environment/bin/python", "/home/pi3b/Cornerstone/analyze.py"]

def run_pipeline():
    """Runs the image capture and analysis pipeline concurrently for speed."""
    print("📸 Capturing image...")
    photo_process = subprocess.Popen(PHOTO_CMD)  # Start photo process without waiting

    print("🧐 Analyzing image...")
    analyze_process = subprocess.Popen(ANALYZE_CMD)  # Start analyze process in parallel

    # Wait for both processes to finish
    photo_process.wait()
    analyze_process.wait()

    if photo_process.returncode == 0:
        print("✅ Photo taken successfully.")
    else:
        print("❌ Failed to capture photo.")

    if analyze_process.returncode == 0:
        print("✅ Analysis complete.")
    else:
        print("❌ Analysis failed.")

if __name__ == "__main__":
    run_pipeline()

