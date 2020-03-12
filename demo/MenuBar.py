import wx

class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, '&Exit', 'Terminate the program')
        menuItem = filemenu.Append(wx.ID_ABOUT, 'About', " Information about this program")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '&File')
        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        self.SetMenuBar(menuBar)
        self.Show()

    def OnAbout(self, event):
        wx.MessageBox('111111')


app = wx.App()
frame = mainWindow(None, 'Sample editor')
app.MainLoop()