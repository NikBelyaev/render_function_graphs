import wx
from Obj.InputWindowClass import InputWindow

def main():
    app = wx.App()
    dlg = InputWindow()
    dlg.ShowModal()
    dlg.Destroy()

if __name__ == '__main__':
    main()
