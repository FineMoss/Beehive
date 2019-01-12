
# Created by Jake Stephens

# only import what is needed
import time
import os.path
from os     import makedirs
from shutil import move


class Model():

    # default reports directory name is ".reports"
    # default extension is ".report"
    def __init__(self, reports_dir=".reports", extension=".report"):
        self.reports_dir = reports_dir
        self.extension   = extension

    # creates a report with report_name.extension in reports_dir and
    # adds path of files from source_path that the fit the conditions to the report
    def run_report(self, source_dir, report_name="", conditions={}):
        # initalize variables
        report_name = self.__name_report(report_name)
        report_path = os.path.join(self.reports_dir, report_name+self.extension)
        file_count  = 0
        # make sure there is a reports directory
        if not os.path.exists(self.reports_dir):
            makedirs(self.reports_dir)
        # create the report
        with open(report_path, "w") as report:
            # recursively walk the directory tree
            for root, dirs, files in os.walk(source_dir, onerror=self.__handle_error):
                for file in files:
                    file_path = os.path.join(root, file)
                    # if the file meets the conditions
                    if self.__conditions_apply(conditions, file_path):
                        # add the path to the report
                        report.write(file_path+"\n")
                        file_count+=1
            # add file count and the source_dir for later use
            report.write("!! File Count: "+str(file_count)+" !!\n")

        return report_path

    # moves all of the files from the report to a destination directory
    def move_files(self, report_path, destination_dir):
        # TODO try catch OS_Error __handle_error
        # TODO if file already exists in dir - rename to new_file(1)
        if os.path.exists(report_path):
            with open(report_path, "r") as report:
                for line in report.readlines():
                    if line[:2] != "!!":
                        line = line.rstrip()
                        # TODO should be rel path or use absolute path
                        common_path = os.path.commonpath([destination_dir, line])
                        cutoff = len(common_path.split("/"))
                        dst = os.path.join(destination_dir, *line.split("/")[cutoff:-1])
                        if not os.path.exists(dst):
                            # TODO make sure (try catch) dst is not a file
                            makedirs(dst)
                        move(line, dst)
        else:
            __throw_error()

    # create name for the report
    def __name_report(self, report_name):
        if report_name == "":
            return time.strftime("%Y%m%d-%H%M%S")
        else:
            return report_name

    # verify that all conditions are met for a file to be added to the report
    def __conditions_apply(self, conditions, file):
        all_conditions_apply = True
        # iterate 
        for key in conditions:
            # pass off condition types
            if conditions[key](key, file) == False:
                all_conditions_apply = False

        return all_conditions_apply

    # return true if the file was last mod before the given date
    # else return false
    def date_condition(self, date, file):
        # get time last modified in epoch format
        mod_epoch = os.path.getmtime(file)
        # convert input date to epoch format
        # TODO check for errors in format
        date_struct = time.strptime(date, "%m/%d/%Y")
        date_epoch = time.mktime(date_struct)

        if date_epoch > mod_epoch:
            return True
        else:
            return False

    
    def __throw_error():
        # TODO
        print("!! ERROR: could not find file !!")

    def __handle_error(self, error_instance):
        # TODO
        print("!! ERROR: could not find file !!")