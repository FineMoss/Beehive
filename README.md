# Beehive v2.0
Created by Jake Stephens
File Archive Application  
Cross platform tkinter user interface
Developed and tested with Python 3.7 and MacOS Mojave
Run Main.py with python to launch the application

This version allows the user to select a directory that they wish to archive, and a directory that the archived files will move to. The program will preserve the entire directory tree in the source directory and in the target directory. First, a report will be generated letting the user know what files are about to be archived. Then the user can decide if they want to proceed with the archive or cancel. The only way to filter files is with the date of last modification. More filtering options will be available in newer versions. A hidden reports directory will be created and reports will be added each time a report is ran. These reports will eventually be used to “undo” an archive event.


Changes from version 1 to version 2: 
Nothing is different, but everything has changed. Version 1 is ad-hoc and was hacked together without a care for design, readability or extendability. Version 2 implements the Model View Controller software architecture. The new architecture makes the code easily extended for more functionality. Many potential errors were removed while MVC was being implemented. A lot of time and thought was put into each line of code to make sure version 2 is better than version 1 in every way. The functionality and look of the UI is exactly the same. However, expected more functionality and changes to the UI from here on out.


More about the MVC architecture:
The entry point for this application is Main.py. Main.py is responsible for initializing tkinter and all of the components of the app (Model, View, and Controller). The Model and the View do not reference each other nor the Controller. The Model is responsible for all the back end operations of file manipulation and parsing. The View is responsible for creating and organizing the UI. The Controller is responsible for mapping the the functionality of the UI components to the back end operations of the Model. Therefore the Controller is composed of the Model and the View.  
