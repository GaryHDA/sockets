from time import sleep
from picamera import PiCamera

def takeapicture(name):

	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	# Camera warm-up time
	sleep(2)
	mypicture = '{}.jpg'.format(name)
	camera.capture(mypicture)
