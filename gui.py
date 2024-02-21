import wx

class MyFrame(wx.Frame):
    def __init__ (self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        



        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)



    def update_surname(self, surname):
        self.text_ctrl.SetValue(surname)

