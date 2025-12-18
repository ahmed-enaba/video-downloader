from tkinter import *
from tkinter import ttk
from yt_dlp import YoutubeDL


def mp3():
    try:
        url=Field.get()
        deic={
            'format':'bestaudio',
            'outtmpl':'Downloads/%(title)s.%(ext)s',
        }
        with YoutubeDL(deic) as ydl:
            ydl.download([url])
            print("the audio has been downloaded")

    except:
        print("can't downlaod")


def low():
    try:
        url=Field.get()
        deic={
            'format':'best[height<=240]',
            'outtmpl':"Downloads/%(title)s.%(ext)s"
        }
        with YoutubeDL(deic) as ydl:
            ydl.download([url])
            print("the video has been downloaded") 

    except:
        print("faild to download")



def mediam():
    try:
        url=Field.get()
        deic={
            'format':'best[height<=480]',
            'outtmpl':'Downloads/%(title)s.%(ext)s'
        }     
        with YoutubeDL(deic) as ydl:
            ydl.download([url])
            print("the video has been downloaded")   

    except:
        print("faild to downlaod")



def high():
    try:
        url=Field.get()
        deic={
            'format':'best[height<=720]',
            'outtmpl':'Downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(deic) as ydl:
            ydl.download([url])
            print("the video has been downloaded")
            
    except:
        print("faild to download")



window=Tk()
window.title('video downloader')
window.geometry("600x400")
window.configure(background="gray41")


label=Label(window,text=("paste your link here"),font='bold',background=window['background'])
label.place(x=220,y=100)


Field=Entry(window,width=60)
Field.place(x=120,y=80)


high_quality=Button(window,text="high",font='bold',activeforeground='SteelBlue3',command=high)
high_quality.place(x=170,y=140)


mediam_quality=Button(window,text="mediam",font='bold',activeforeground='SteelBlue3',command=mediam)
mediam_quality.place(x=240,y=140)


low_quality=Button(window,text="low",font='bold',activeforeground='SteelBlue3',command=low)
low_quality.place(x=340,y=140)


sound=Button(window,text="mp3",font='bold',activeforeground='SteelBlue3',command=mp3)
sound.place(x=400,y=140)


copy_right_label=Label(window,text="@all copy right reserved by Ahmed Elsayed",font=("arial",9),background=window['background'])
copy_right_label.pack(side="bottom",pady=4)




window.mainloop()
