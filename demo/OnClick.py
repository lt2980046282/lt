# encoding=utf8
import os
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, 'About', '123')
        menuExit = filemenu.Append(wx.ID_EXIT, 'Exit', '456')
        menuOpen = filemenu.Append(wx.ID_OPEN, 'open', '456')
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, 'File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Show()

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, 'A small text editor', 'About Sample Editor', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def OnOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, '', '*.*', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, 'Sample editor')
app.MainLoop()