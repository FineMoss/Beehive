
# Created by Jake Stephens


import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        print("hi")




# initialize the app
root = tk.Tk()
app = Application(master=root)

# set the title of the app
app.master.title("Beehive Version 2.0")

# set the window size of the app
app.master.minsize(900, 488)
app.master.maxsize(900, 488)

# set the icon of the app
app.master.iconbitmap("flower.ico")

# run the app
app.mainloop()









