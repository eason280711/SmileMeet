
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from re import I

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, dialog
import tkinter
import cv2
from PIL import Image, ImageTk, ImageDraw,ImageSequence,ImageEnhance

from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import pygame
import random


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
camlst = []

pygame.mixer.init()
def play(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.1)

def get_cam():
    global camlst
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    camlst = arr

def change_cam():
    global cap,camlst,camidx
    get_cam()
    camidx = camidx + 1
    if camidx >= len(camlst):
        camidx = camlst[0]
    print(camidx)
    cap = cv2.VideoCapture(camidx)


window = Tk()
get_cam()
camidx = camlst[0]
window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
 
    return canvas.create_polygon(points, **kwargs, smooth=True)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
round_rectangle(
    101.0,
    150.0,
    681.0,
    893.0,
    radius=40,
    fill="#FFE075",
    outline="")

round_rectangle(
    760.0,
    150.0,
    1340.0,
    893.0,
    radius=40,
    fill="#FFE075",
    outline="")

round_rectangle(
    0.0,
    0.0,
    1440.0,
    90.0,
    radius=5,
    fill="#FFE075",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    115.0,
    45.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    903.0,
    1438.0,
    1024.0,
    
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1352.0,
    90.0,
    1438.0,
    1024.0,
    fill="#FFFFFF",
    outline="")

cap_show = True
def cap_close():
    global cap_show,camidx,camlst,cap
    print(cap_show)
    if cap_show:
        cap.release()
    else:
        get_cam()
        camidx = camlst[0]
        cap = cv2.VideoCapture(camidx)
    cap_show = not cap_show

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: cap_close(),
    relief="flat"
)
button_1.place(
    x=682.0,
    y=922.0,
    width=75.0,
    height=75.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: change_cam(),
    relief="flat"
)
button_2.place(
    x=870.0,
    y=922.0,
    width=75.0,
    height=75.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: window.quit(),
    relief="flat"
)
button_3.place(
    x=1272.0,
    y=922.0,
    width=75.0,
    height=75.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=92.0,
    y=922.0,
    width=75.0,
    height=75.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: start(),
    relief="flat"
)
button_6.place(
    x=494.0,
    y=922.0,
    width=75.0,
    height=75.0
)

from tkinter import ttk

def change_volume(value=None):
    pygame.mixer.music.set_volume(0.1* (scale_h.get()/100))

style = ttk.Style()
style.configure("TScale", background="#FFFFFF",troughcolor="#FFE075")

scale_h=ttk.Scale(window, from_=0, to=100,command=change_volume,style="TScale")
scale_h.set(100)
scale_show = False 

scale_h.pack_forget()

def show_scale():
    global scale_show
    if scale_show:
        scale_h.place_forget()
    else:
        scale_h.place(
            x=765.0,
            y=900.0,
        )
    scale_show = not scale_show

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=show_scale,
    relief="flat"
)
button_7.place(
    x=776.0,
    y=922.0,
    width=75.0,
    height=75.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#FFFFFF",
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=589.0,
    y=921.0,
    width=75.0,
    height=75.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    233.0,
    45.0,
    image=image_image_2
)

canvas.create_rectangle(
    278.0,
    35.0,
    354.0,
    67.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    298.0,
    52.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    334.0,
    51.0,
    image=image_image_4
)

# image_image_5 = PhotoImage(
#     file=relative_to_assets("image_5.png"))
# image_5 = canvas.create_image(
#     1059.0,
#     536.0,
#     image=image_image_5
# )

label = tkinter.Label(window)
label.config(bg="#FFE075")
label.place(
    x=895.0,
    y=212.0,
)


frameCnt = 180

def GIF_OPEN(frames):
    ret = []
    im = Image.open(frames)
    iter = ImageSequence.Iterator(im)
    for frame in iter:
        frame = frame.convert('RGBA')
        pic = ImageTk.PhotoImage(image=frame)
        ret.append(pic)
    return ret
frames_wait = GIF_OPEN('GIF/待機.gif')
frames_angry = GIF_OPEN('GIF/生氣.gif')
frames_sad = GIF_OPEN('GIF/哀.gif')
frames_happy = GIF_OPEN('GIF/樂.gif')
frames_surprise = GIF_OPEN('GIF/驚訝.gif')

correct_sound = pygame.mixer.Sound('assets/correct.mp3')
wrong_sound = pygame.mixer.Sound('assets/wrong.mp3')

anstime = False
get_face = False

emotion_lst = [frames_wait,frames_angry,frames_sad,frames_happy,frames_surprise]
emotion_sq = []
emotion_path = ["","assets/angry.png","assets/sad.png","assets/happy.png","assets/surprise.png"]
emotion = ['','Angry','Sad','Happy','Surprise']
test_emo = 0

def check():
    global anstime,wrong_sound,test_emo
    if anstime and get_face:
        print(cur_emotion,emotion[test_emo])
        if cur_emotion == emotion[test_emo]:
            answerbox("assets/correct.png")
            correct_sound.play()
        else:
            answerbox("assets/wrong.png")
            wrong_sound.play()
        test_emo = 0
        anstime = False

def ReduceOpacity(im, opacity):

    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im
    
def rmchat():
    global anstime
    if anstime:
        answerbox("assets/wrong.png")
        wrong_sound.play()
    anstime = False
    canvas.delete("chatbox")
def rmans():
    canvas.delete("ansbox")
def rmtitle():
    canvas.delete("titlebox")

def chatbox(emo):
    global image_image_R,anstime
    anstime = True
    img = Image.open(emo).convert("RGBA")
    image_image_R = ImageTk.PhotoImage(image=img)
    canvas.create_image(
        1060.0,
        160.0,
        tags="chatbox",
        image=image_image_R
    )
    canvas.after(5000,rmchat)
    return image_image_R

def titlebox(emo):
    global image_image_T
    img = Image.open(emo).convert("RGBA")
    image_image_T = ImageTk.PhotoImage(image=img)
    canvas.create_image(
        1060.0,
        160.0,
        tags="titlebox",
        image=image_image_T
    )
    canvas.after(5000,rmtitle)
    return image_image_T

def answerbox(ans):
    global image_image_A
    img = Image.open(ans).convert("RGBA")
    image_image_A = ImageTk.PhotoImage(image=img)
    canvas.create_image(
        400.0,
        160.0,
        tags="ansbox",
        image=image_image_A
    )
    canvas.after(800,rmans)
    return image_image_A
def reset(lst):
    global emotion_sq
    emotion_sq = lst

def start():
    lst = []
    for _ in range(5):
        lst.append(random.randint(1,4))
    titlebox("assets/follow.png")
    canvas.after(2000,reset,lst)
def update(frames,ind):
    global test_emo
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
        if len(emotion_sq) > 0:
            frames = emotion_lst[emotion_sq[0]]
            if not canvas.find_withtag("chatbox"):
                if emotion_sq[0] != 0:
                    chatbox(emotion_path[emotion_sq[0]])
            else:
                if emotion_sq[0] != 0:
                    canvas.delete("chatbox")
                    canvas.itemconfig("chatbox",image= chatbox(emotion_path[emotion_sq[0]]))
            test_emo = emotion_sq[0]
            emotion_sq.pop(0)
        else:
            frames = emotion_lst[0]
        label.configure(image=frame)
        window.after(30, update, frames,ind)
        return
    label.configure(image=frame)
    window.after(30, update, frames,ind)
    return

cap = cv2.VideoCapture(camidx)

lmain = tkinter.Label(bg="#FFE075")
lmain.pack()

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

class_labels=['Angry','Happy','Neutral','Sad','Surprise']
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model('EmotionDetectionModel.h5')

cur_emotion = ''

def show_frame():
    global cur_emotion,get_face
    if cap.isOpened():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)
        if  len(faces) == 0:
            get_face = False
        for (x,y,w,h) in faces:
            get_face = True
            cv2.rectangle(frame,(x,y),(x+w,y+h),(117,224,255),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray])!=0:
                roi=roi_gray.astype('float')/255.0
                roi=img_to_array(roi)
                roi=np.expand_dims(roi,axis=0)

                preds=classifier.predict(roi)[0]
                label_position=(x,y)
                cur_emotion = class_labels[np.argmax(preds)]
                cv2.putText(frame,"I GOT YOU",label_position,cv2.FONT_HERSHEY_PLAIN,2,(117,224,255),3)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        img = add_corners(img,0)
        half = 580/img.size[0]
        img = img.resize( [int(half * s) for s in img.size] )

        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.place(x=101,y=231,width=580,height=580)
    else:
        lmain.place_forget()
    lmain.after(120, show_frame)

show_frame()

window.bind('<Return>', lambda e: check())
window.wm_iconbitmap('assets/LOGO.ico')
window.wm_title('Smile Meet')
window.resizable(True,True)
window.after(0,play,"./assets/BGM_01.wav")
window.after(0, update,frames_wait, 0)
window.mainloop()