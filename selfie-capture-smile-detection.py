#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:27:31 2020

@author: nadiahzulkifli
"""

from Detector import haar_app, mar_app
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage
names = set()

class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("memberslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("SELFIE CAPTURE WITH SMILE DETECTION")
        self.resizable(False, False)
        self.geometry("500x250")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    def on_closing(self):

        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            f =  open("memberslist.txt", "a+")
            for i in names:
                    f.write(i+" ")
            self.destroy()


class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            #load = Image.open("homepagepic.png")
            #load = load.resize((250, 250), Image.ANTIALIAS)
            render = PhotoImage(file='homepagepic.png')
            img = tk.Label(self, image=render)
            img.image = render
            img.grid(row=0, column=1, rowspan=4, sticky="nsew")
            label = tk.Label(self, text="        Home Page        ", font=self.controller.title_font,fg="#263942")
            label.grid(row=0, sticky="ew")
            button1 = tk.Button(self, text="   Camera  ", fg="#023059", bg="#263942",command=lambda: self.controller.show_frame("PageOne"))
            #button1 = tk.Button(self, text="   Add a User  ", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageOne"))
            #button2 = tk.Button(self, text="   Check a User  ", fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageTwo"))
            button2 = tk.Button(self, text="Quit", fg="#263942", bg="#ffffff", command=self.on_closing)
            button1.grid(row=1, column=0, ipady=3, ipadx=7)
            #button2.grid(row=2, column=0, ipady=3, ipadx=2)
            button2.grid(row=3, column=0, ipady=3, ipadx=32)


        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Selfie Capture", font='Helvetica 16 bold')
        label.grid(row=0,column=0, sticky="ew")
        button1 = tk.Button(self, text="Haar Feature Selection", command=self.openwebcam1, fg="#023059", bg="#263942")
        button2 = tk.Button(self, text="Mouth Aspect Ratio (MAR)", command=self.openwebcam2, fg="#023059", bg="#263942")
        button4 = tk.Button(self, text="Go to Home Page", command=lambda: self.controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        button1.grid(row=1,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button2.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button4.grid(row=5,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)

    def openwebcam1(self):
        haar_app(self.controller.active_name)
    
    def openwebcam2(self):
        mar_app(self.controller.active_name)



app = MainUI()
app.iconphoto(False, tk.PhotoImage(file='icon.ico'))
app.mainloop()

