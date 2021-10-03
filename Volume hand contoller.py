# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Description: Change volume with middle and thumb. Squeeze both fingers to lower and strecth to raise volume
import cv2
import time
import numpy as np
import HandTracking as ht
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volume.GetMasterVolumeLevel()
volrange =(volume.GetVolumeRange())
volume.SetMasterVolumeLevel(-20.0, None)
minVol = volrange[0]
maxVol = volrange[1]

#max - 155
#min - 50

#max - -74
#min  - 0

detect = ht.DetectorHand()


camwidth, camheight = 640,480


cap = cv2.VideoCapture(0)
cap.set(3, camwidth)
cap.set(4, camheight)
time1 = 0

detect = ht.DetectorHand(0.50)
while True:
    sucess,img = cap.read()
    img = detect.findHands(img)
    positions = detect.findp(img,draw=False)
    if len(positions) != 0:
        #print(positions[4],positions[12])
        xthumb,ythumb = positions[4][1],positions[4][2]
        xmiddle, ymiddle = positions[12][1], positions[12][2]
        centerx,centery = (xthumb+xmiddle)//2,(ythumb+ymiddle)//2
        cv2.circle(img,(xthumb, ythumb),10,(255,0,0),cv2.FILLED)
        cv2.circle(img, (xmiddle, ymiddle), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (centerx, centery), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img,(xthumb,ythumb),(xmiddle,ymiddle),(255,0,255),3)
        length = math.hypot(xmiddle-xthumb,ymiddle-ythumb)
        #print(length)

        vol = np.interp(length,[10,100],[minVol,maxVol])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length < 30:
            cv2.circle(img, (centerx, centery), 10, (255, 0, 255), cv2.FILLED)



    time0 = time.time()
    fps = 1/(time0-time1)
    time1 = time0

    cv2.putText(img, f'FPS: {int(fps)}',(45,75),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv2.imshow("Img",img)
    cv2.waitKey(1)
