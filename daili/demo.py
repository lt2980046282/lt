import os
import time
from queue import Queue
from threading import Thread

import wx
import dlmysql


class DaiLIFrame(Thread, wx.Frame):
    def __init__(self, parent, title, size=(800, 800)):
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.panel = wx.Panel(self, wx.ID_ANY)
        # 列表组件
        self.tx = wx.ListCtrl(self.panel, -1, style = wx.LC_REPORT)
        self.tx.InsertColumn(0, '数量', wx.LIST_FORMAT_LEFT, 100)
        self.tx.InsertColumn(1, 'IP', wx.LIST_FORMAT_LEFT, 200)
        self.tx.InsertColumn(2, '是否可用', wx.LIST_FORMAT_LEFT, 100)
        # 按钮组件
        self.ibtn = wx.Button(self.panel, label='导入', size=(50, 30))
        self.satbtn = wx.Button(self.panel, label='测速', size=(50, 30))
        self.exbtn = wx.Button(self.panel, label='导出', size=(50, 30))
        self.endbtn = wx.Button(self.panel, label='关闭', size=(50, 30))
        # 多选按钮组件
        self.cekbox = wx.CheckBox(self.panel, label='国外IP')
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        titleSizer.Add(self.tx, 0, wx.ALL, 5)
        titleSizer.Add(self.exbtn, 0, wx.ALL, 5)
        titleSizer.Add(self.ibtn, 0, wx.ALL, 5)
        titleSizer.Add(self.satbtn, 0, wx.ALL, 5)
        titleSizer.Add(self.endbtn, 0, wx.ALL, 5)
        titleSizer.Add(self.cekbox, 0, wx.ALL, 5)
        self.panel.SetSizer(titleSizer)
        titleSizer.Fit(self)

        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.ibtn)
        self.Bind(wx.EVT_BUTTON, self.OnExport, self.exbtn)
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.endbtn)
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.satbtn)
        super(DaiLIFrame, self).__init__( parent, title, size)
        self.Show(True)

    def run(self):
        pass

    def OnOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "选择文件", self.dirname, '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirname = dlg.GetDirectory()
            self.filename = dlg.GetFilename()
            with open(os.path.join(self.dirname, self.filename), 'r') as f:
                for index, i in enumerate(set(f.read().split('\n'))):
                    self.tx.InsertItem(0, 16)
                    self.tx.SetItem(index, 1, i)

    def OnExport(self, e):
        self.dirname = ''
        self.num = self.tx.GetItemCount()
        dlg = wx.FileDialog(self, "选择文件", self.dirname, '', '*.txt', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirname = dlg.GetDirectory()
            self.filename = dlg.GetFilename()
            with open(os.path.join(self.dirname, self.filename), 'a+') as f:
                for index in range(self.num):
                    f.write(self.tx.GetItemText(index, 1)+'\n')

    def OnClose(self, e):
        exit()

    def OnStart(self, e):
        ls = dlmysql.showList('successstore')
        st = set(ls)
        print(st)

        for index, l in enumerate(st):
            self.tx.InsertItem(index, index)
            self.tx.SetItem(index, 0, f'{index + 1}')
            self.tx.SetItem(index, 1, l)
            self.tx.Bind(wx.EVT_RIGHT_UP, self.ShowPopup)

    def ShowPopup(self, e):
        menu = wx.Menu()
        menu.Append(1, "Copy selected items")
        menu.Bind(wx.EVT_MENU, self.CopyItems, id=1)
        self.PopupMenu(menu)

    def CopyItems(self, e):
        selectedItems = []
        for i in range(self.tx.GetItemCount()):
            if self.tx.IsSelected(i):
                selectedItems.append(self.tx.GetItemText(i))

        clipdata = wx.TextDataObject()
        clipdata.SetText("\n".join(selectedItems))
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

        print ("Items are on the clipboard")

def main():
    app = wx.App(False)
    DaiLIFrame(None, '代理测试').start()
    app.MainLoop()


if __name__ == '__main__':
    main()
