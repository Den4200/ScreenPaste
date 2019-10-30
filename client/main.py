import wx
from gui import ScreenShot

def main():
    app = wx.App()
    ScreenShot(None, 'Screen Paste')
    app.MainLoop()

if __name__ == "__main__":
    main()
