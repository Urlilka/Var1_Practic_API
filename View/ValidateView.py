from tkinter import ttk, Tk
from tkinter import *

import re
from requests import get
from docx import Document


class Validate(Tk):
    def __init__(self):
        super().__init__()
        self.TestCase_file = "ТестКейс.docx"
        # self.API_url = "http://prb.sylas.ru/TransferSimulator/email"
        
        # Окно
        self.title("API")
        self.geometry("600x150")

    # Настройка пололжения строк
        # ROW
        self.rowconfigure(index=0,weight=1)
        self.rowconfigure(index=1,weight=1)
        
        # COLUMN
        self.columnconfigure(index=0,weight=1)
        self.columnconfigure(index=1,weight=1)


    # GET из API
        # Кнопка получения API
        self.getAPIButton = ttk.Button(self,text="Получить данные",command=self.get_API)
        self.getAPIButton.grid(row=0,column=0,padx=10)

        # Текст получения API
        self.getAPILabel = ttk.Label(self,text="Тут будут полученные данные")
        self.getAPILabel.grid(row=0,column=1,sticky="w")


    # SEND В Файл ТестКейс.docx
        # Кнопка отправления API
        self.sendAPIButton = ttk.Button(self,text="Получить данные")
        self.sendAPIButton.grid(row=1,column=0,padx=10)

        # Текст подтверждения отправления
        self.sendAPILabel = ttk.Label(self,text="Тут будет подтверждения отправления данных")
        self.sendAPILabel.grid(row=1,column=1,sticky="w")



    def get_API(self):

        API = get("http://prb.sylas.ru/TransferSimulator/email",{"key":"value"})
        # text_API = API.json()["value"]
        print(API)

if __name__ == "__main__":
    window = Validate()
    window.mainloop()