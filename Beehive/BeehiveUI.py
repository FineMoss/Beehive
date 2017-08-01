
# Created By Jake Stephens


from tkinter import *
import tkinter.filedialog
import Archiver
import os
import datetime




class Application(Frame):

   
    def isProperDate(self, targetDate):
    
        # Returns Boolean if it is proper and Formatted targetDate
        try:
            split = targetDate.split('/')
            targetMonth      = int(split[0])
            targetDay        = int(split[1])
            targetYear       = int(split[2])
            targetDateFormat = datetime.date(targetYear, targetMonth, targetDay).isoformat()
            return (True, targetDateFormat)
        except:
            return(False, False)



    def lockFields(self):
        self.currentEntry["state"]  = "disabled"
        self.targetEntry["state"]   = "disabled"
        self.dateEntry["state"]     = "disabled"
        self.archiveButton["state"] = "disabled"
        self.clearButton["state"]   = "disabled"

        self.confirmButton["state"] = "normal"
        self.cancelButton["state"]  = "normal"



    def unlockFields(self):
        self.currentEntry["state"]  = "normal"
        self.targetEntry["state"]   = "normal"
        self.dateEntry["state"]     = "normal"
        self.archiveButton["state"] = "normal"
        self.clearButton["state"]   = "normal"

        self.confirmButton["state"] = "disable"
        self.cancelButton["state"]  = "disable"


 

    def archive(self):

        # Gets info from UI Fields
        currentPath = str(self.currentEntry.get())
        targetPath  = str(self.targetEntry.get())
        targetDate  = str(self.dateEntry.get())

        # Handles possible errors in the Entry Fields
        lines = []
        properDate = self.isProperDate(targetDate)

        if os.path.isdir(currentPath):
            if os.path.isdir(targetPath):
                if properDate[0]:
                    try:
                        # Runs the Archive Report if no Errors
                        reportName = Archiver.runReport(currentPath, targetPath, properDate[1])
                        report = open(reportName, 'r')
                        lines = report.read()
                        report.close()
                        self.lockFields()

        # Prints Error codes to the UI    
                    except:
                        lines.append("ERROR: Archive Report Failed")
                else:
                    lines.append("ERROR: Invalid Date")
            else:
                lines.append("ERROR: Invalid Archive Location")
        else:
            lines.append("ERROR: Invalid Folder to be Archived")
        
        # Populates the textField
        self.textField["state"] = "normal"
        self.textField.delete("1.0", "end")
        self.textField.insert("1.0", lines)
        self.textField["state"] = "disabled"



    def confirm(self):

        # Gets info from UI Fields
        currentPath = str(self.currentEntry.get())
        targetPath  = str(self.targetEntry.get())
        targetDate  = str(self.dateEntry.get())

        # Handles possible errors in the Entry Fields
        lines = []
        properDate = self.isProperDate(targetDate)

        if os.path.isdir(currentPath):
            if os.path.isdir(targetPath):
                if properDate[0]:
                    try:
                        # Runs the Archive Report if no Errors
                        reportName = Archiver.archive(currentPath, targetPath, properDate[1])
                        report = open(reportName, 'r')
                        lines = report.read()
                        report.close()
                        self.unlockFields()

         # Prints Error codes to the UI
                    except:
                        lines.append("ERROR: Archived Failed")
                else:
                    lines.append("ERROR: Invalid Date")
            else:
                lines.append("ERROR: Invalid Archive Location")
        else:
            lines.append("ERROR: Invalid Folder to be Archived")
        
        # Populates the textField
        self.textField["state"] = "normal"
        self.textField.delete("1.0", "end")
        self.textField.insert("1.0", lines)
        self.textField["state"] = "disabled"
       
        Archiver.clearTempFiles()



    def cancel(self):
        self.textField["state"] = "normal"
        self.textField.delete("1.0", "end")
        self.textField["state"] = "disabled"
        self.unlockFields()
        Archiver.clearTempFiles()



    def clear(self):
        self.currentEntry.delete("0", "end")
        self.targetEntry.delete("0", "end")
        self.dateEntry.delete("0", "end")
        self.textField["state"] = "normal"
        self.textField.delete("1.0", "end")
        self.textField["state"] = "disabled"



    def browse(self):

        self.file = tkinter.filedialog.askopenfile(title="Browse for Location", mode = "r")





    def createWidgets(self):

        # Quit Button
        self.QUIT            = Button(self)
        self.QUIT["text"]    = "QUIT"
        self.QUIT["fg"]      = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.grid(row = 8, column = 0, columnspan = 2)


        # Target Label
        self.currentLabel         = Label(self)
        self.currentLabel["text"] = "Folder to be Archived"
        self.currentLabel["pady"] = 5

        self.currentLabel.grid(row = 0, column = 0, columnspan = 2)


        # Target Entry 
        self.currentEntry          = Entry(self)
        self.currentEntry["width"] = 40

        self.currentEntry.grid(row = 1, column = 0, columnspan = 2)


        # Archive Label
        self.targetLabel         = Label(self)
        self.targetLabel["text"] = "Archive To This Location"
        self.targetLabel["pady"] = 5

        self.targetLabel.grid(row = 2, column = 0, columnspan = 2)


        # Archive Entry
        self.targetEntry          = Entry(self)
        self.targetEntry["width"] = 40

        self.targetEntry.grid(row = 3, column = 0, columnspan = 2)


        # Date Label
        self.dateLabel         = Label(self)
        self.dateLabel["text"] = "Enter a Date (MM/DD/YYYY)"
        self.dateLabel["pady"] = 5

        self.dateLabel.grid(row = 4, column = 0, columnspan = 2)


        # Date Entry
        self.dateEntry          = Entry(self)
        self.dateEntry["width"] = 10

        self.dateEntry.grid(row = 5, column = 0, columnspan = 2)


        # Archive Button
        self.archiveButton            = Button(self)
        self.archiveButton["text"]    = "Run Archive Report"
        self.archiveButton["command"] = self.archive

        self.archiveButton.grid(row = 6, column = 0)


        # Clear all Button
        self.clearButton            = Button(self)
        self.clearButton["text"]    = "Clear All Fields"
        self.clearButton["command"] = self.clear

        self.clearButton.grid(row = 6, column = 1)


        # Confirm Button
        self.confirmButton            = Button(self)
        self.confirmButton["text"]    = "Confirm Archive"
        self.confirmButton["fg"]      = "green"
        self.confirmButton["command"] = self.confirm
        self.confirmButton["state"]   = "disable"

        self.confirmButton.grid(row = 7, column = 0)


        # Cancel Button
        self.cancelButton            = Button(self)
        self.cancelButton["text"]    = "Cancel Archive"
        self.cancelButton["fg"]      = "red"
        self.cancelButton["command"] = self.cancel
        self.cancelButton["state"]   = "disabled"

        self.cancelButton.grid(row = 7, column = 1)
        

        # # Browse Button
        # self.browseButton            = Button(self)
        # self.browseButton["text"]    = "Browse"
        # self.browseButton["command"] = self.browse

        # self.browseButton.grid(row = 8, column = 0)


        # Text Field
        self.textField                   = Text(self)
        self.textField["height"]         = 30
        self.textField["padx"]           = 5
        self.textField["yscrollcommand"] = True
        self.textField["state"]          = "disabled"

        self.textField.grid(row = 0, column = 2, rowspan = 30, sticky = W+E+N+S)



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()





# Create the UI object
root = Tk()
app = Application(master=root)


# Main window setup
app.master.title("Beehive Version 1.0")
app.master.minsize(900, 488)
app.master.maxsize(900, 488)


# Run the UI object
app.mainloop()