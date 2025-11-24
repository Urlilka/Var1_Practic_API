from tkinter import ttk, Tk
from tkinter import *

import re
from requests import get
from docx import Document


class Validate():
    def __init__():
        super().__init__()
        self.TestCase_file = "ТестКейс.docx"


        self.API_url = "http://prb.sylas.ru/TransferSimulator/fullName"