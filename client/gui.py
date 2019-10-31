import os
import wx
from wx.lib.agw.hyperlink import HyperLinkCtrl
import pyautogui

from upload import Client

class ScreenShot(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(
            parent=parent, 
            title=title
            )

        self.widgets()
        self.Show()

    def widgets(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        btns = {
            'ScreenShot': self.ss,
            }

        for label, func in btns.items():
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, func)
            sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

    @staticmethod
    def ss(self):
        screen = wx.ScreenDC()
        size = pyautogui.size()
        bmp = wx.Bitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)

        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem
        bmp.SaveFile(os.path.join('screenshots', 'screenshot.png'), wx.BITMAP_TYPE_PNG)

        print('Screenshot taken!')
        
        c = Client()
        c.send_img()
