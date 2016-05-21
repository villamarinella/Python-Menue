import picamera
import time
import os

#Change this to alter the save path
SAVEPATH = '/root/bilder/'
fname=SAVEPATH+(time.strftime("%d%m%Y%H%M%S"))+".h254"
name = raw_input('Enter a video name: ')
length = input('Enter a video length in seconds: ')
camera = picamera.PiCamera()
camera.preview_fullscreen=False
camera.preview_window=(100, 100, 640, 480)
camera.resolution=(1280,720)
print 'Now recording '
camera.start_preview()
camera.start_recording(fname)
time.sleep(10

camera.stop_preview()
print 'Saving ' + fname
camera.stop_recording()

