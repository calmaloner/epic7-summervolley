import pyautogui
import time
import math
from PIL import Image

print('Auto Volley for E7')
print('======================')
print('If this scripts works well, just press Enter to skip')
default_size = [1920, 1080]
main_size = [int(i) for i in pyautogui.size()]
#x, y = [int(i) for i in pyautogui.size()]
'''
try:
    x, y = [int(i) for i in input('Your screen resolution, (default: '+ str(def) +' '+ str(y) +'): ').split()]
    print('Screen resolution changed to '+ str(x) + 'x' + str(y))
except (SyntaxError, ValueError):
    print('Screen resolution will use default value')
'''
x, y = int(main_size[0]/2), int(main_size[1])
#delay
t1 = 0.04
t2 = 0.15

try:
    t1 = float(input('Delay 1 ('+str(t1)+'):'))
    print('Delay 1 changed to ' + str(t1))
except (SyntaxError, ValueError):
    print('Delay 1 will use default value')

try:
    t2 = float(input('Delay 2 ('+str(t2)+'):'))
    print('Delay 2 changed to ' + str(t2))
except (SyntaxError, ValueError):
    print('Delay 2 will use default value')

print('To end this script just close the console')
print('======================')
print('Script started')
print('======================')

#ImageResize
prop = (main_size[0]/default_size[0], main_size[1]/default_size[1])
img = Image.open('images/volley.png')

#img.show()
resized_img = img.resize((int(img.size[0]*prop[0]), int(img.size[1]*prop[1])))
resized_img.save('images/resized_volley.png')

#VolleyScripts
a = [0,0]

while True:
    time.sleep(0.1)
    volley = pyautogui.locateCenterOnScreen('images/resized_volley.png', region=(0,0,x,y), confidence=0.52)
    a = volley
    if volley!=None:
        print('Volley detected    ', end='\r')
        if math.dist(volley,a) < 200:
            #Delay if distance between ball is short
            time.sleep(0.04)
        #Delay between every click
        time.sleep(0.15)
        pyautogui.click(volley)
    
    else:
        print('Volley not detected', end='\r')