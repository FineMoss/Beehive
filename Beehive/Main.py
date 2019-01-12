
# Created by Jake Stephens

# only import what is needed
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
    view.master.minsize(976, 488)
    view.master.maxsize(976, 488)

    # set the icon of the app
    # TODO catch no file errors
    img = Image("photo", file="../icons/beehive_icon.png")
    root.iconphoto(True, img)

    # run the app
    view.mainloop()


# Main.py should only be run as "__main__"
if __name__ == "__main__":
    main()
else:
    print("ERROR: Main.py is not running as "'__main__'" ")