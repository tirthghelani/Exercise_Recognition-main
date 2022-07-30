# learn data
import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm
import pyttsx3
from pymongo import MongoClient  # import mongo client to connect
import pprint

# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = client["Exercise"]
employee = db["a"]
excercise_2 = db["xyz"]
c1 = db["col_1"]
c2 = db["col_2"]
c3 = db["col_3"]
c4 = db["col_4"]
c5 = db["col_5"]
c7 = db["col_7"]
c8 = db["col_8"]
c9 = db["col_9"]

dir_1=0
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
dir_12 = 0

def declare():

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
    dir_12 = 0
    print("Refresh")

cap = cv2.VideoCapture("C:/Users/HP/Downloads/Exercise/Exercise/suryanamaskar//video1.mp4")
# cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
direction = 0
seatup=0
up=0
pushup=0
form = 0
feedback = "Fix Form"
angle=0
l=0
r=0
z=[]
pushup_exercise=[]
col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_7 = []
col_8 = []
col_9 = []

# get seat up data
for y in employee.find({},{'_id':0,'pushup_data':1}):
  z.append(y.get('pushup_data'))
  print(z)

# get push up data
for y in excercise_2.find({},{'_id':0,'pushup_data':1}):
  pushup_exercise.append(y.get('pushup_data'))
  print(pushup_exercise)

# get surya data
for y in c1.find({},{'_id':0,'pushup_data':1}):
  col_1.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c2.find({}, {'_id': 0, 'pushup_data': 1}):
  col_2.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c3.find({}, {'_id': 0, 'pushup_data': 1}):
  col_3.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c4.find({}, {'_id': 0, 'pushup_data': 1}):
  col_4.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c5.find({}, {'_id': 0, 'pushup_data': 1}):
  col_5.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c7.find({},{'_id':0,'pushup_data':1}):
  col_7.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c8.find({},{'_id':0,'pushup_data':1}):
  col_8.append(y.get('pushup_data'))
  print(pushup_exercise)

for y in c9.find({},{'_id':0,'pushup_data':1}):
  col_9.append(y.get('pushup_data'))
  print(pushup_exercise)
# print(z[0][1])

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
        leg_left = detector.findAngle(img,23,25,27)
        leg_right = detector.findAngle(img, 24, 26, 28)

        temp = []
        temp.append(int(elbow_left))
        temp.append(int(elbow_right))
        temp.append(int(leg_left))
        temp.append(int(leg_right))
        """shoulder = detector.findAngle(img, 13, 11, 23)
        hip = detector.findAngle(img, 11, 23,25)"""

        # Percentage of success of pushup
        per_left = np.interp(elbow_left, (90, 160), (0, 100))
        per_right = np.interp(elbow_right, (90, 160), (0, 100))

        # Bar to show Pushup progress
        bar_left = np.interp(elbow_left, (90, 160), (380, 50))
        bar_right = np.interp(elbow_right, (90, 160), (380, 50))

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
        step9_1 = int(detector.findAngle(img, 12, 24, 26))
        # leg right
        step9_2 = int(detector.findAngle(img, 24, 26, 28))

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

        if( 1 ):
            for i in range(len(z)):
                if( (temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2]) and (temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3])):
                    seatup=1
                    # print(temp[0]+2)
                    # print((z[i][0]))
                    # print(temp[0] - 2)
                    # print((z[i][0]))
                # if (temp[1] + 2 > z[i][1] and temp[1] - 2 < z[i][1]):
                #      seatup += 1
                #     # print(temp[1]+2)
                #     # print((z[i][0]))
                #     # print(temp[1] - 2)
                #     # print((z[i][0]))
                # if (temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2]):
                #      seatup += 1
                #     # print(temp[2] + 2)
                #     # print((z[i][0]))
                #     # print(temp[2] - 2)
                #     # print((z[i][0]))
                # if (temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3]):
                #      seatup += 1
                #     # print(temp[3] + 2)
                #     # print((z[i][0]))
                #     # print(temp[3] - 2)
                #     # print((z[i][0]))

            if(seatup==1):
                print("SeatUpOK")
                seatup=0
                angle=1
                l=temp[2]
                # print(l)
                # print(seatup)
            else:
                seatup=0

            for i in range(len(z)):
                if( (temp[0] + 2 > pushup_exercise[i][0] and temp[0] - 2 < pushup_exercise[i][0])
                        and (temp[1] + 2 > pushup_exercise[i][1] and temp[1] - 2 < pushup_exercise[i][1])
                    and
                        (temp[2] + 2 > pushup_exercise[i][2] and temp[2] - 2 < pushup_exercise[i][2])
                    and
                        (temp[3] + 2 > pushup_exercise[i][3] and temp[3] - 2 < pushup_exercise[i][3])):
                    up=1
                    # print(temp[0]+2)
                    # print((z[i][0]))
                    # print(temp[0] - 2)
                    # print((z[i][0]))
                # if (temp[1] + 2 > z[i][1] and temp[1] - 2 < z[i][1]):
                #      seatup += 1
                #     # print(temp[1]+2)
                #     # print((z[i][0]))
                #     # print(temp[1] - 2)
                #     # print((z[i][0]))
                # if (temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2]):
                #      seatup += 1
                #     # print(temp[2] + 2)
                #     # print((z[i][0]))
                #     # print(temp[2] - 2)
                #     # print((z[i][0]))
                # if (temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3]):
                #      seatup += 1
                #     # print(temp[3] + 2)
                #     # print((z[i][0]))
                #     # print(temp[3] - 2)
                #     # print((z[i][0]))

            if(up==1):
                print("PushUpOK")
                up=0
                angle=1
                l=temp[2]
                # speak number code
                # initialize Text-to-speech engine
                engine = pyttsx3.init()
                count+=1
                # convert this text to speech
                # play the speech
                if count%5==0:
                    engine.say(count)
                    engine.runAndWait()
                # print(l)
                # print(seatup)
            else:
                seatup=0


        # else:
        #     # print(leg_left)
        # Check to ensure right form before starting the program
        # if elbow_left < 50 and elbow_right < 50:
        #     form = 1
        # elif elbow_left<50:
        #     form = 2
        # elif elbow_right<50:
        #     form = 3
        # elif leg_left<80:
        #     form = 4

            for i in range(len(col_1)):
                if step1_1 <= col_1[i][0]+2 and step1_1 >= col_1[i][0]-2 \
                        and step1_2 <= col_1[i][1] + 2 and step1_2 >= col_1[i][1]-2 \
                        and step1_3 <= col_1[i][2] + 2 and step1_3 >= col_1[i][2] - 2 \
                        and step1_4 <= col_1[i][3] + 2 and step1_4 >= col_1[i][3]-2:
                    if dir_1==0:
                        temp.append(int(step1_1))
                        temp.append(int(step1_2))
                        temp.append(int(step1_3))
                        temp.append(int(step1_4))
                        count += 0.5
                        dir_1 = 1
                        print("step-1,12")
                        if dir_2==1 and dir_4==1 and dir_5==1 and dir_7==1 and dir_8==1:
                            print("1")
                            dir_1 = 0
                        declare()

            for i in range(len(col_2)):
                if step2_1 <= col_2[i][0]+2 and step2_1 >= col_2[i][0]-2 \
                        and step2_2 <= col_2[i][1]+2 and step2_2 >= col_2[i][1]-2 \
                        and step2_3 <= col_2[i][2]+2 and step2_3 >= col_2[i][2]-2 \
                        and step2_4 <= col_2[i][3]+2 and step2_4 >= col_2[i][3]-2 and dir_1==1:
                    if dir_2 == 0:
                        temp.append(int(step2_1))
                        temp.append(int(step2_2))
                        temp.append(int(step2_3))
                        temp.append(int(step2_4))
                        print("step-2,11")
                        count += 0.5
                        dir_2 = 1
                        dir_1 = 0

            for i in range(len(col_3)):
                if step3_1 <= col_3[i][0]+2 and step3_1 >= col_3[i][0]-2 \
                        and step3_2 <= col_3[i][0]+2 and step3_2 >= col_3[i][0]-2 and dir_2==1:
                    if dir_3 == 0:
                        temp.append(int(step3_1))
                        temp.append(int(step3_2))
                        count += 0.5
                        dir_3 = 1
                        print("step-3,10")
                        dir_1 = 0

            for i in range(len(col_4)):
                if (step4_1 <= col_4[i][0] and step4_2 <= col_4[i][1]) or (step9_1 <= col_4[i][0] and step9_2 <= col_4[i][1]) :

                    if((step4_1 <= col_4[i][0] and step4_2 <= col_4[i][1])):
                        if dir_4 == 0:
                            temp.append(int(step4_1))
                            temp.append(int(step4_2))
                            count += 0.5
                            dir_4 = 1
                            print("step-4")
                            dir_1 = 0

                    if ((step9_1 <= col_4[i][0] and step9_2 <= col_4[i][1])):
                        if dir_9 == 0:
                            temp.append(int(step9_1))
                            temp.append(int(step9_2))
                            count += 0.5
                            dir_9 = 1
                            print("step-9")
                            dir_1 = 1
                            dir_4 = 1
                            dir_2 = 0
                            dir_3 = 0

            for i in range(len(col_5)):
                if step5_1 <= col_5[i][0]+2 and step5_1 >= col_5[i][0]-2 and dir_4 == 1 :

                    if dir_5 == 0:
                        temp.append(int(step5_1))
                        temp.append(int(step5_1))
                        count += 0.5
                        dir_5 = 1
                        print("step-5")
                        dir_1 = 0
                        dir_4 = 0

            for i in range(len(col_7)):
                if (step7_1 <= col_7[i][0]+2 and step7_1 >= col_7[i][0]-2
                    and step7_2 <= col_7[i][1]+2 and step7_2 >= col_7[i][1]-2
                    and step7_3 <= col_7[i][2]+2 and step7_3 >= col_7[i][2]-2
                    and step7_4 <= col_7[i][3]+2 and step7_4 >= col_7[i][3]-2)\
                        and dir_5==1:
                    if dir_7 == 0:
                        temp.append(int(step7_1))
                        temp.append(int(step7_2))
                        temp.append(int(step7_3))
                        temp.append(int(step7_4))
                        count += 0.5
                        dir_7 = 1
                        print("step-7")
                        dir_1 = 0
            for i in range(len(col_8)):
                if step8_1 <= col_5[i][0]+2 and step8_1 >= col_5[i][0]-2 and dir_7 == 1 :
                    if dir_8 == 0:
                        temp.append(int(step8_1))
                        temp.append(int(step8_2))
                        count += 0.5
                        dir_8 = 1
                        print("step-8")
                        dir_1 = 0
                        dir_2=0
                        dir_3=0
        # Check for full range of motion for the pushup
        if form == 1:
            # if per_left == 0 and  per_right==0:
            if elbow_left <= 50 and elbow_right <= 50:
                feedback = "Up"
                if direction == 0:
                    count += 0.5
                    direction = 1
                    Data = {
                        "pushup_data": temp
                    }
                    print(temp)
                    print("push up")

                    # Creating document
                    MyData = db.b
                    # Inserting data
                    MyData.insert_one(Data)
            else:
                feedback = "Fix Form"

            # if per_left == 100 and per_right==100:
            if elbow_left > 160 and elbow_right > 160:
                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0
            else:
                feedback = "Fix Form"
                # form = 0

        # Check for full range of motion for the pushup
        if form == 2:
            # if per_left == 0 and  per_right==0:
            if elbow_left <= 90:
                feedback = "Up"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                feedback = "Fix Form"

            # if per_left == 100 and per_right==100:
            if elbow_left > 160:
                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0
            else:
                feedback = "Fix Form"
                # form = 0

        # Check for full range of motion for the pushup
        if form == 3:
            # if per_left == 0 and  per_right==0:
            if elbow_right <= 90:
                feedback = "Up"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                feedback = "Fix Form"

            # if per_left == 100 and per_right==100:
            if elbow_right > 160:
                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0
            else:
                feedback = "Fix Form"
                # form = 0

        # Check for full range of motion for the pushup
        if form == 4:
            # if per_left == 0 and  per_right==0:
            if leg_left >= 140:
                feedback = "Up"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                feedback = "Fix Form"

            # if per_left == 100 and per_right==100:
            if leg_left < 80:
                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0
                    Data = {
                        "pushup_data": temp
                    }
                    print(temp)
                    print("Seat Up")

                    # Creating document
                    MyData = db.a
                    # Inserting data
                    MyData.insert_one(Data)

            else:
                feedback = "Fix Form"
                # form = 0

        # print(count)

        # Draw Bar

        if form == 3:
            cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(img, (580, int(bar_right)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per_right)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

        if form == 1 or form == 2:
            cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(img, (580, int(bar_left)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per_left)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

        # Pushup counter
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)

        # Feedback
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

    """if (lmList[25][2] and lmList[26][2] >= lmList[23][2] and lmList[24][2]):
        posiotion = "sit"
    if (lmList[25][2] and lmList[26][2] <= lmList[23][2] and lmList[24][2] and posiotion == "sit"):
        posiotion = "up"
        count += 1
        print("tirth")
        print(count)"""

    cv2.imshow('Pushup counter', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()