import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from cred import email, key
from doctors import full_doctors_list
import os
import time
import wx
import threading




class MyFrame(wx.Frame):  
    def __init__(self, parent, title):  
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))  
        self.panel = wx.Panel(self)  
        self.sizer = wx.BoxSizer(wx.VERTICAL)  
        self.panel.SetSizer(self.sizer)  
        self.text_ctrl_name = wx.TextCtrl(self.panel, style=wx.TE_READONLY)  
        self.text_ctrl_lastname = wx.TextCtrl(self.panel, style=wx.TE_READONLY)  
        self.sizer.Add(self.text_ctrl_name, 1, wx.EXPAND | wx.ALL, 5)  
        self.sizer.Add(self.text_ctrl_lastname, 1, wx.EXPAND | wx.ALL, 5)  
        self.names = ["John", "Jane", "Doe", "Smith"]  
        self.lastnames = ["Johnson", "Doe", "Smith", "Williams"]  
        self.Bind(wx.EVT_CLOSE, self.OnClose)  

        # Создаем кнопку "Стоп" и привязываем к ней событие
        self.stop_button = wx.Button(self.panel, label="Stop")
        self.stop_button.Bind(wx.EVT_BUTTON, self.OnStop)
        self.sizer.Add(self.stop_button, 0, wx.ALL, 5)

        self.running = True  # Флаг для управления выполнением потоков

        self.thread_names = threading.Thread(target=self.update_names)  
        self.thread_lastnames = threading.Thread(target=self.update_lastnames)  
        self.thread_names.daemon = True  
        self.thread_lastnames.daemon = True  
        self.thread_names.start()  
        self.thread_lastnames.start()  

    def update_names(self):  
        while self.running:  
            for name in self.names:  
                wx.CallAfter(self.update_display_name, name)  
                time.sleep(3)  

    def update_lastnames(self):  
        while self.running:  
            for lastname in self.lastnames:  
                wx.CallAfter(self.update_display_lastname, lastname)  
                time.sleep(5)  

    def update_display_name(self, name):  
        self.text_ctrl_name.SetValue(name)  

    def update_display_lastname(self, lastname):  
        self.text_ctrl_lastname.SetValue(lastname)  

    def OnClose(self, event):  
        self.running = False  # Устанавливаем флаг в False для остановки потоков
        event.Skip()  # Позволяет закрыть окно после завершения потоков

    def OnStop(self, event):
        self.running = False  # Устанавливаем флаг в False для остановки потоков

class MyApp(wx.App):  
    def OnInit(self):  
        frame = MyFrame(None, "Name and Lastname Display")  
        frame.Show(True)  
        return True  

if __name__ == "__main__":  
    app = MyApp(0)  
    app.MainLoop()  

