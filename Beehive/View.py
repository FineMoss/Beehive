
# Created by Jake Stephens


import tkinter as tk
import Control as c


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        c.hi()