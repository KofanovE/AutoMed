import wx

class MyFrame(wx.Frame):
    def __init__ (self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Press me")
        self.text = wx.StaticText(self.panel, label="Text will be here")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button,0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.text, 0, wx.ALL|wx.CENTER, 5)
        self.panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)

        self.Show()

    def on_button_click(self, event):
        self.text.SetLabel("Button is pressed")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, title="Example of GUI")
    app.MainLoop()
