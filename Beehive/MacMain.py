
# Created by Jake Stephens


import tkinter as tk
import View    as v


# the main method
def main():

    # initialize the app
    root = tk.Tk()
    app = v.Application(master=root)

    # set the title of the app
    app.master.title("Beehive Version 2.0")

    # set the window size of the app
    app.master.minsize(900, 488)
    app.master.maxsize(900, 488)

    # set the icon of the app
    app.master.iconbitmap("../flower.ico")

    # run the app
    app.mainloop()


# prevent import of MacMain.py
if __name__ == "__main__":
    main()
else:
    print("ERROR: MacMain.py is being imported")