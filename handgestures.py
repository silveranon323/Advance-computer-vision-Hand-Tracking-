from tkinter import *
import cv2
import mediapipe as mp
import  time
root = Tk()
root.configure(bg ="black")
root.title(" HAND TRACKER ")
def center_window( width =610 , height = 90):
     #get screen width and height
     screen_width= root.winfo_screenwidth()
     screen_height= root.winfo_screenheight()
     #calculating the position of x and y coordinate
     x = (screen_width/2) - (width/2)
     y = (screen_height/2) - (height/2)
     root.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window()
def track():
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    pTime = 0
    cTime = 0



    while True:
        success,img = cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks :
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img , handLms, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

        cv2.imshow("WEBCAM" , img)
        cv2.waitKey(1)



b1 = Button(root , text = "START" , command = track , fg = "red", cursor = "hand2",padx = "100").place(x = 200 , y=10)
b2 = Button(root , text = "QUIT" , command = quit , fg = "red", cursor = "hand2" , padx = "105").place(x = 200, y=50)



root.mainloop()