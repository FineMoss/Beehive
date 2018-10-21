
# Created by Jake Stephens


from   tkinter import *
import Model   as M
import View    as V
import Control as C


# the main method
def main():

    # initialize the app
    root    = Tk()
    model   = M.Model(reports_dir=".beehive_reports")
    view    = V.View(master=root)
    control = C.Control(model, view)

    # set the title of the app
    view.master.title("Beehive Version 2.0")

    # set the window size of the app
    view.master.minsize(900, 488)
    view.master.maxsize(900, 488)

    # set the icon of the app
    view.master.iconbitmap("../flower.ico")

    # run the app
    view.mainloop()


# prevent import of MacMain.py
if __name__ == "__main__":
    main()
else:
    print("ERROR: MacMain.py is being imported")