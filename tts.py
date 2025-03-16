import os

# Requires the piper 64 aarch 
PIPER_DIR = "/home/pi3b/Cornerstone/piper"
PIPER_BIN = f"{PIPER_DIR}/piper"
MODEL = f"{PIPER_DIR}/en_US-ryan-low.onnx" # 
CONFIG = f"{PIPER_DIR}/en_US-ryan-low.onnx.json"

def text_to_speech(text):
    command = f'echo "{text}" | {PIPER_BIN} --model {MODEL} --config {CONFIG} --output-file {PIPER_DIR}/output.wav'
    os.system(command)
    os.system(f"aplay {PIPER_DIR}/output.wav")

if __name__ == "__main__":
    text_to_speech("Hello, this is a test!")
