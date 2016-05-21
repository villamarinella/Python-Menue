import picamera
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
SAVEPATH = '/root/bilder/'
fname=SAVEPATH+(time.strftime("%d%m%Y%H%M%S"))+".jpg"
with picamera.PiCamera() as camera:
    camera.preview_fullscreen=False
    camera.preview_window=(100, 100, 640, 480)
    camera.resolution=(640,480)
    camera.start_preview()
    while True:
       if GPIO.input(27):
          camera.capture(fname)
          camera.stop_preview()
          camera.close
          break
       print GPIO.input(27)
       time.sleep(1)
       
