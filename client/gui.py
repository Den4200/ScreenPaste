import os
import webbrowser

import wx
import pyautogui
import tkinter as tk

from upload import Client
from logger import log

class Screenshot:

    def __init__(self, title='ScreenPaste'):
        self.root = tk.Tk()
        self.root.title(title)

        self.canvas = tk.Canvas(self.root, width=40, height=60)
        self.canvas.pack()

        self.btns = {
            'ScreenShot': self.ss,
        }

        self.init_btns()
        self.root.mainloop()

    def init_btns(self):
        for text, command in self.btns.items():
            btn = tk.Button(
                self.canvas, 
                text=text, 
                width=25, 
                command=command
            )
            btn.pack()

    def ss(self):
        app = wx.App()
        screen = wx.ScreenDC()
        size = pyautogui.size()
        bmp = wx.Bitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)

        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem
        bmp.SaveFile(os.path.join('screenshots', 'screenshot.png'), wx.BITMAP_TYPE_PNG)
        
        log('INFO', 'Screenshot taken')

        client = Client()
        client.send_img()

        label = tk.Label(self.canvas, text=client.returnLink(), fg="blue", cursor="hand2")
        label.pack()
        label.bind("<Button-1>", lambda e: self.callback(client.returnLink()))
        
        app.MainLoop()

    def callback(self, link):
        webbrowser.open_new_tab(link)

# Importing this class from main script won't work for some reason..
# So I'll just call the class from here
Screenshot()
