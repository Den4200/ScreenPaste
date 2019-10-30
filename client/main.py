from wx import App
from gui import ScreenShot

def main():
    app = App()
    ScreenShot(None, 'Screen Paste')
    app.MainLoop()

if __name__ == "__main__":
    main()
