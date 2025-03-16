from time import sleep
from picamera2 import Picamera2

def capture_image():
    print(Picamera2.global_camera_info())

    picam2 = Picamera2(camera_num=0)
    
    # Correct config for JPEG with 480p resolution
    config = picam2.create_still_configuration(main={"size": (1280, 720)}, buffer_count=1)
    picam2.configure(config)
    
    picam2.start()
    sleep(1)  # Faster startup time

    picam2.capture_file('test_photo.jpg', format='jpeg')  # Correct format usage
    picam2.stop()
    print('Photo taken')

if __name__ == "__main__":
    capture_image()

