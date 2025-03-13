import cv2
import mediapipe as mp
import pyautogui
cap =cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
(1920, 1080)

index_y=0
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id==8:
                #defining the pointer point
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
               #defining the thumb point
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y  
                    print('outside',abs(index_y-thumb_y))  
                    #defining the click point
                    if abs(index_y-thumb_y)<40:
                        pyautogui.click()
                        pyautogui.sleep(1)
            # print(hands)
    cv2.imshow('virtual Mouse',frame)
    cv2.waitKey(1)



    


#     import cv2
# face_cap=cv2.CascadeClassifier('D:/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# cap= cv2.VideoCapture(0)#run time camera enables
# #pramennt camera access
# while True:
#     #reading the images 
#     ret,video_data=cap.read()
#     col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
#     video_data=cv2.flip(video_data,1)
#     face=face_cap.detectMultiScale(
#         col,
#         scaleFactor=1.1,
#         minNeighbors=4,
#         minSize=(30,30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for(x,y,w,h) in face:
#         cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow('Face Recognigation',video_data)
#     if cv2.waitKey(10)== ord('a'):
#         break
# cap.release()
 

# #only for enabling camera
# # import cv2
# # cap= cv2.VideoCapture(0)#run time camera enables
# # #pramennt camera access
# # while True:
# #     #reading the images 
# #     ret,video_data=cap.read()
# #     cv2.imshow('Face Recognigation',video_data)
# #     if cv2.waitKey(10)== ord('a'):
# #         break
# # cap.release()

