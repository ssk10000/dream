import cv2
import mediapipe as mep
import time

#cap = cv2.VideoCapture(0)

class DetectorHand():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCom = trackCon
        self.mHands = mep.solutions.hands
        self.hands = self.mHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCom)
        self.draw = mep.solutions.drawing_utils

#time1 = 0
#ftime = 0


#while True:
 #   sucess,img = cap.read()
    def findHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.res = self.hands.process(imgRGB)
            #print(res.multi_hand_landmarks)

        if self.res.multi_hand_landmarks:
                for handLand in self.res.multi_hand_landmarks:
                    if draw:
                        self.draw.draw_landmarks(img,handLand,self.mHands.HAND_CONNECTIONS)
        return img
    def findp(self,img,handnum = 0,draw = True):
        position=[]
        if self.res.multi_hand_landmarks:
            myhand = self.res.multi_hand_landmarks[handnum]


            for id, land in enumerate(myhand.landmark):
                  #print(id, land)
                  height,width, chan = img.shape
                  cenx,ceny = int(land.x*width),int(land.y*height)
                  #print( id, cenx,ceny)
                  position.append([id,cenx,ceny])
                  if draw:
                  #if id == 4:
                    cv2.circle(img,(cenx,ceny),7,(255,0,0),cv2.FILLED)
        return position
                #self.draw.draw_landmarks(img, handLand,self.mHands.HAND_CONNECTIONS)
#ftime = time.time()
#fps = 1/(ftime-time1)
#time1= ftime
#cv2.putText(img,str(int(fps)),(18,78),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
#cv2.imshow("Image",img)
#cv2.waitKey(1)

def main():
    time1 = 0
    ftime = 0
    cap = cv2.VideoCapture(0)
    detector = DetectorHand()
    while True:
        sucess,img = cap.read()
        img = detector.findHands(img)
        position = detector.findp(img , draw=false)
        if len(position) != 0:
            print(position[4])
        ftime = time.time()
        fps = 1/(ftime-time1)
        time1= ftime
        cv2.putText(img,str(int(fps)),(18,78),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ =="__main__":
    main()

