import time

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100)).__init__()
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.control.AppendText(f'{i}\n')
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None, "Small editor")
app.MainLoop()