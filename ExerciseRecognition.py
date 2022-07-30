# Real APP
from fileinput import filename

import cap as cap
import cv2
import cvzone
import mediapipe as mp
import numpy as np
import pyttsx3

import PoseModule as pm
from pymongo import MongoClient  # import mongo client to connect
import pprint
from tkinter import ttk, CENTER, filedialog
import tkinter as tk


# print(z[0][1])

root = tk.Tk()
root.geometry("700x500")
root.title("List")
root.configure()
root['background'] = '#AED6F1'

lbl1 = tk.Label(root, text="Welcome to exercise recognition AI S/W", background="#5DADE2", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack(padx=5, pady=25)

frame = tk.LabelFrame(root, background="#5DADE2", text='choice your method')
frame.pack(padx=5, pady=(40, 10))

selection = tk.IntVar()
OPTIONS = [
    "Push Up",
    "Seat Up",
    "Surya Namashkar"
]  # etc

variable = tk.StringVar(root)
variable.set(OPTIONS[0])

def onRadioButtonChange():
    if selection.get() != 0:
        print("1")
        b1["state"] = "active"

    else:
        print("2")
        b1["state"] = "disabled"



def browsefunc():
    global filename
    filename = filedialog.askopenfilename()




tk.Radiobutton(frame, command=onRadioButtonChange, text="Opern camara (Live)", variable=selection, value=0).grid(
    column=0, row=0)
tk.Radiobutton(frame, command=onRadioButtonChange, text="Using local storage", variable=selection, value=1).grid(
    column=1, row=0)


b1 = browsebutton = tk.Button(root, text="Browse", state="disable", command=browsefunc)
b1.pack(pady=(5, 40))

w = tk.OptionMenu(root, variable, *OPTIONS)
w.pack()


def submit():
    # Creating instance of mongoclient
    client = MongoClient("mongodb+srv://test:test@cluster0.9sg1rjo.mongodb.net/?retryWrites=true&w=majority")
    # Creating database
    db = client.Exercise
    pushupdata = db.pushup
    seatupdata = db.seatup
    detector = pm.poseDetector()
    count = 0
    direction = 0
    seatup = 0
    pushup = 0
    form = 0
    feedback = "Fix Form"
    angle = 0
    l = 0
    r = 0
    z = []
    p = []
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s7 = []
    s8 = []
    s9 = []

    # col_1 = db.col_1
    # col_2 = db.col_2
    # col_3 = db.col_3
    # col_4 = db.col_4
    # col_5 = db.col_5
    # col_6 = db.col_6
    # col_7 = db.col_7
    # col_8 = db.col_8
    # col_9 = db.col_9
    # col_10 = db.col_10
    # col_11 = db.col_11
    # col_12 = db.col_12
    step = 0

    dir_1 = 0
    dir_2 = 0
    dir_3 = 0
    dir_4 = 0
    dir_5 = 0
    dir_6 = 0
    dir_7 = 0
    dir_8 = 0
    dir_9 = 0
    dir_10 = 0
    dir_11 = 0
    dir_12 = 1
    namaskar = 0
    h=0
    x=0
    n_count=0;s_count=0;p_count=0


    for y in seatupdata.find({}, {'_id': 0, 'pushup_data': 1}):
        z.append(y.get('pushup_data'))
        # print(z)

    for y in pushupdata.find({}, {'_id': 0, 'pushup_data': 1}):
        p.append(y.get('pushup_data'))
        print(p)

    # for y in col_1.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s1.append(y.get('pushup_data'))
    #     print(s1)
    #
    # for y in col_2.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s2.append(y.get('pushup_data'))
    #     print(s2)
    #
    # for y in col_3.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s3.append(y.get('pushup_data'))
    #     print(s3)
    #
    # for y in col_4.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s4.append(y.get('pushup_data'))
    #     print(s4)
    #
    # for y in col_5.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s5.append(y.get('pushup_data'))
    #     print(s5)
    #
    # for y in col_7.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s7.append(y.get('pushup_data'))
    #     print(s7)
    #
    # for y in col_8.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s8.append(y.get('pushup_data'))
    #     print(s8)
    #
    # for y in col_9.find({}, {'_id': 0, 'pushup_data': 1}):
    #     s9.append(y.get('pushup_data'))
    #     print(s9)


    print ("value is:" + variable.get())
    if(variable.get()=="Push Up"):
        form = 1
    elif(variable.get()=="Seat Up"):
        form = 2
    elif(variable.get()=="Surya Namashkar"):
        form = 3


    if(b1["state"]=="disabled"):
        cap = cv2.VideoCapture(0)
    else:
        print(filename)
        cap = cv2.VideoCapture(filename)
        if(filename==""):
            print("no file")



    detector = pm.poseDetector()

    while cap.isOpened():

        ret, img = cap.read()  # 640 x 480
        # Determine dimensions of video - Help with creation of box in Line 43
        width = cap.get(3)  # float `width`
        height = cap.get(4)  # float `height`
        # print(width, height)

        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            elbow_left = detector.findAngle(img, 11, 13, 15)
            elbow_right = detector.findAngle(img, 12, 14, 16)
            leg_left = detector.findAngle(img, 23, 25, 27)
            leg_right = detector.findAngle(img, 24, 26, 28)

            # hand
            step1_1 = detector.findAngle(img, 11, 13, 15)
            step1_2 = detector.findAngle(img, 12, 14, 16)
            # leg
            step1_3 = detector.findAngle(img, 23, 25, 27)
            step1_4 = detector.findAngle(img, 24, 26, 28)

            # hand
            step2_1 = detector.findAngle(img, 13, 11, 23)
            step2_2 = detector.findAngle(img, 14, 12, 24)
            # kamar
            step2_3 = detector.findAngle(img, 11, 23, 25)
            step2_4 = detector.findAngle(img, 12, 24, 26)

            # both kamar
            step3_1 = detector.findAngle(img, 11, 23, 25)
            step3_2 = detector.findAngle(img, 12, 24, 26)

            # kamar left
            step4_1 = detector.findAngle(img, 11, 23, 25)
            # leg left
            step4_2 = detector.findAngle(img, 23, 25, 27)

            # kamar both
            step5_1 = detector.findAngle(img, 11, 23, 25)
            step5_2 = detector.findAngle(img, 12, 24, 26)

            # hand
            step7_1 = detector.findAngle(img, 13, 11, 23)
            step7_2 = detector.findAngle(img, 14, 12, 24)
            # kamar
            step7_3 = detector.findAngle(img, 11, 23, 25)
            step7_4 = detector.findAngle(img, 12, 24, 26)

            # kamar both
            step8_1 = detector.findAngle(img, 11, 23, 25)
            step8_2 = detector.findAngle(img, 12, 24, 26)

            # kamar right
            step9_1 = detector.findAngle(img, 12, 24, 26)
            # leg right
            step9_2 = detector.findAngle(img, 24, 26, 28)

            # kamar
            step10_1 = detector.findAngle(img, 11, 23, 25)
            step10_2 = detector.findAngle(img, 12, 24, 26)

            # hand
            step11_1 = detector.findAngle(img, 13, 11, 23)
            step11_2 = detector.findAngle(img, 14, 12, 24)
            # kamar
            step11_3 = detector.findAngle(img, 11, 23, 25)
            step11_4 = detector.findAngle(img, 12, 24, 26)

            # hand
            step12_1 = detector.findAngle(img, 11, 13, 15)
            step12_2 = detector.findAngle(img, 12, 14, 16)
            # leg
            step12_3 = detector.findAngle(img, 23, 25, 27)
            step12_4 = detector.findAngle(img, 24, 26, 28)

            if (form == 1):
                temp = []
                temp.append(int(elbow_left))
                temp.append(int(elbow_right))
                temp.append(int(leg_left))
                temp.append(int(leg_right))

                for i in range(30):
                    if (temp[0] + 4 > p[i][0] and temp[0] - 4 < p[i][0] and temp[1] + 4 > p[i][1] and temp[1] - 4 < p[i][1] and
                            temp[2] + 4 > p[i][2] and temp[2] - 4 < p[i][2] and temp[3] + 4 > p[i][3] and temp[3] - 4 < p[i][3]):
                        if(h==0):
                            pushup += 1
                            h=1
                    elif(temp[0]>130 or temp[1]>130):
                        h=0

                if (pushup == 1):
                    print("PushUpOK")
                    pushup = 0
                    p_count += 1
                    # speak number code
                    # initialize Text-to-speech engine
                    engine = pyttsx3.init()
                    # convert this text to speech
                    # play the speech
                    if p_count % 5 == 0 and p_count != 0:
                        engine.say(p_count)
                        engine.runAndWait()
                    angle = 1
                    # print(seatup)
                else:
                    pushup = 0

            if(form==2):
                    temp = []
                    temp.append(int(elbow_left))
                    temp.append(int(elbow_right))
                    temp.append(int(leg_left))
                    temp.append(int(leg_right))

                    for i in range(24):
                        if(temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2] and temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3]):
                            if(x==0):
                                seatup+=1

                                x=1
                        elif(temp[2]>130 or temp[3]>130):
                            x=0

                    if(seatup==1):
                                print("SeatUpOK")
                                seatup=0
                                s_count+=1
                                # speak number code
                                # initialize Text-to-speech engine
                                engine = pyttsx3.init()
                                # convert this text to speech
                                # play the speech
                                if s_count % 5 == 0 and s_count != 0:
                                    engine.say(s_count)
                                    engine.runAndWait()
                                angle=1
                                l=temp[2]
                                print(l)
                                # print(seatup)
                    else:
                               seatup=0

            if (form == 3):

                temp = []
                # temp.append(int(hand))
                # temp.append(int(leg_left))
                # temp.append(int(leg_right))
                """shoulder = detector.findAngle(img, 13, 11, 23)
                hip = detector.findAngle(img, 11, 23,25)"""

                # # Percentage of success of pushup
                # per_left = np.interp(elbow_left, (90, 160), (0, 100))
                # per_right = np.interp(elbow_right, (90, 160), (0, 100))
                #
                # # Bar to show Pushup progress
                # bar_left = np.interp(elbow_left, (90, 160), (380, 50))
                # bar_right = np.interp(elbow_right, (90, 160), (380, 50))

                if step1_1 <= 60 and step1_2 <= 60 and step1_3 >= 165 and step1_4 >= 165:
                    if dir_1 == 0:
                        temp.append(int(step1_1))
                        temp.append(int(step1_2))
                        temp.append(int(step1_3))
                        temp.append(int(step1_4))

                        dir_1 = 1

                        print("Push Step-1,12")

                        if dir_2 == 1 and dir_3 == 1 and dir_4 == 1 and dir_5 == 1 and dir_7 == 1 and dir_8 == 1:
                            print("1")
                            dir_1 = 0


                elif step2_3 <= 165 and step2_4 <= 165 and step2_1 >= 160 and step2_2 >= 160 and dir_1 == 1:
                    if dir_2 == 0:
                        temp.append(int(step2_1))
                        temp.append(int(step2_2))
                        temp.append(int(step2_3))
                        temp.append(int(step2_4))

                        dir_2 = 1
                        print("Push Step-2,11")
                        dir_1 = 1

                elif step3_1 <= 60 and step3_2 <= 60 and dir_2 == 1:
                    if dir_3 == 0:
                        temp.append(int(step3_1))
                        temp.append(int(step3_2))

                        dir_3 = 1
                        print("Push Step-3,10")
                        dir_1 = 1
                        dir_2 = 0

                elif (step4_1 <= 40 and step4_2 <= 90) or (step9_1 <= 40 and step9_2 <= 90):

                    if ((step4_1 <= 40 and step4_2 <= 90)):
                        if dir_4 == 0:
                            temp.append(int(step4_1))
                            temp.append(int(step4_2))

                            dir_4 = 1
                            print("Push Step-4 or 9")
                            dir_1 = 0

                    if ((step9_1 <= 40 and step9_2 <= 90)):
                        if dir_9 == 0:
                            temp.append(int(step9_1))
                            temp.append(int(step9_2))

                            dir_9 = 1
                            print("Push Step-4 or 9")
                            dir_1 = 1
                            dir_4 = 1
                            dir_2 = 1

                elif step5_1 <= 95 and step5_1 >= 65 and dir_4 == 1:
                    if dir_5 == 0:
                        temp.append(int(step5_1))
                        temp.append(int(step5_2))

                        dir_5 = 1
                        print("Push Step-5")
                        dir_1 = 0
                        dir_4 = 0;

                elif (step7_1 <= 50 and step7_2 <= 50 and step7_3 <= 150 and step7_4 <= 150) and dir_5 == 1:
                    if dir_7 == 0:
                        temp.append(int(step7_1))
                        temp.append(int(step7_2))
                        temp.append(int(step7_3))
                        temp.append(int(step7_4))

                        dir_7 = 1
                        print("Push Step-6,7")
                        dir_1 = 0

                elif step8_1 <= 95 and step8_1 >= 65 and dir_7 == 1:
                    if dir_8 == 0:
                        temp.append(int(step8_1))
                        temp.append(int(step8_2))

                        dir_8 = 1
                        print("Push Step-8")

                        dir_1 = 0
                        dir_12 = 0
                        dir_11 = 1
                        dir_2 = 1
                        dir_3 = 0


                if step12_1 <= 60 and step12_2 <= 60 and step12_3 >= 165 and step12_4 >= 165 and dir_11 == 1:
                    if dir_12 == 0:
                        temp.append(int(step12_1))
                        temp.append(int(step12_2))
                        temp.append(int(step12_3))
                        temp.append(int(step12_4))

                        dir_12 = 1
                        print("Push Step-12")
                        namaskar = 1

                if (namaskar == 1):
                    print("SuryaNamaskarOK")
                    namaskar = 0
                    n_count += 1
                    # speak number code
                    # initialize Text-to-speech engine
                    engine = pyttsx3.init()
                    # convert this text to speech
                    # play the speech
                    if n_count % 5 == 0 and n_count != 0:
                        engine.say(n_count)
                        engine.runAndWait()
                    angle = 1
                    # print(seatup)
                else:
                    namaskar = 0

            if(form==1):
                # Pushup counter
                cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(p_count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 5)
            elif(form==2):
                # Pushup counter
                cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(s_count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 5)
            elif(form==3):
                # Pushup counter
                cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(n_count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 5)

        cv2.imshow('Pushup counter', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    """if (lmList[25][2] and lmList[26][2] >= lmList[23][2] and lmList[24][2]):
        posiotion = "sit"
    if (lmList[25][2] and lmList[26][2] <= lmList[23][2] and lmList[24][2] and posiotion == "sit"):
        posiotion = "up"
        count += 1
        print("tirth")
        print(count)"""


b2 = tk.Button(root, text="Submit", command=submit)
b2.pack(pady=(10, 50))

root.mainloop()