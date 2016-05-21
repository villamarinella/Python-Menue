Python Menue with TK

You will find here a Python 2 script for a "simple" menue working together with a shell script.

This one is made for a Raspberry PI but if you delete the 2 lines for GPIO you can use it for Ubuntu / Linux as well without the foto / video options.

The python script calls the shell script which starts the choosed application.

The text is in german but it is simple to understand.
You can change it easy for your own belongings without study ten years python or shell:-)

The program test.py you should start first to find out you have all import files  you will need.

Start the application in a terminal with:

python menue.py

You can use it headless if you login to your Raspberry with:

ssh -X pi@192.168.1.xxx

you will find:

menue.py

menue.sh

foto.py

video.py

calculator.py

file.py

test.py

readme.MD

Have fun
Klaus Werner

PS: the foto and the video starts and stops with a button you have to connect to the GPIO.
It shows a preview until you press the button and it stops if you press the button again.
The preview  will not work headless.