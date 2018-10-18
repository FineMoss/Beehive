
# Created by Jake Stephens


from   tkinter import *
import Control as c


class Application(Frame):

    # initializes the window
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.__control = c.Control(self)
        self.__create_widgets()

    # generates the widgets
    def __create_widgets(self):

        # buttons

        # quit button
        self.quit_button                  = Button(self)
        self.quit_button["text"]          = "QUIT"
        self.quit_button["bg"]            = "red"
        self.quit_button["command"]       = self.quit

        # archive button
        self.archive_button               = Button(self)
        self.archive_button["text"]       = "Run Archive Report"
        self.archive_button["command"]    = self.__control.archive

        # clear all button
        self.clear_button                 = Button(self)
        self.clear_button["text"]         = "Clear All Fields"
        self.clear_button["command"]      = self.__control.clear

        # confirm button
        self.confirm_button               = Button(self)
        self.confirm_button["text"]       = "Confirm Archive"
        self.confirm_button["fg"]         = "green"
        self.confirm_button["command"]    = self.__control.confirm
        self.confirm_button["state"]      = "disable"

        # cancel button
        self.cancel_button                = Button(self)
        self.cancel_button["text"]        = "Cancel Archive"
        self.cancel_button["fg"]          = "red"
        self.cancel_button["command"]     = self.__control.cancel
        self.cancel_button["state"]       = "disabled"

        # entries

        # target entry 
        self.current_entry                = Entry(self)
        self.current_entry["width"]       = 40

        # archive entry
        self.target_entry                 = Entry(self)
        self.target_entry["width"]        = 40

        # date entry
        self.date_entry                   = Entry(self)
        self.date_entry["width"]          = 10

        # labels

        # target label
        self.current_label                = Label(self)
        self.current_label["text"]        = "Folder to be Archived"
        self.current_label["pady"]        = 5

        # archive label
        self.target_label                 = Label(self)
        self.target_label["text"]         = "Archive To This Location"
        self.target_label["pady"]         = 5

        # date label
        self.date_label                   = Label(self)
        self.date_label["text"]           = "Enter a Date (MM/DD/YYYY)"
        self.date_label["pady"]           = 5

        # text field
        self.text_field                   = Text(self)
        self.text_field["height"]         = 30
        self.text_field["padx"]           = 5
        self.text_field["yscrollcommand"] = True
        self.text_field["state"]          = "disabled"

        # organize the grid

        # buttons
        self.quit_button.grid(row = 8, column = 0, columnspan = 2)
        self.archive_button.grid(row = 6, column = 0)
        self.clear_button.grid(row = 6, column = 1)
        self.cancel_button.grid(row = 7, column = 1)
        self.confirm_button.grid(row = 7, column = 0)

        #entries
        self.current_entry.grid(row = 1, column = 0, columnspan = 2)
        self.target_entry.grid(row = 3, column = 0, columnspan = 2)
        self.date_entry.grid(row = 5, column = 0, columnspan = 2)

        # labels
        self.current_label.grid(row = 0, column = 0, columnspan = 2)
        self.target_label.grid(row = 2, column = 0, columnspan = 2)
        self.date_label.grid(row = 4, column = 0, columnspan = 2)

        # text field
        self.text_field.grid(row = 0, column = 2, rowspan = 30, sticky = W+E+N+S)