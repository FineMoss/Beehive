
# Created by Jake Stephens

# TODO import only what is needed
import os
import time
# import sys
# import datetime


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
            os.makedirs(self.reports_dir)
        # create the report
        with open(report_path, "w") as report:
            # recursively walk the directory tree
            for root, dirs, files in os.walk(source_dir, onerror=self.__handle_error):
                for file in files:
                    # if the file meets the conditions
                    if self.conditions_apply(conditions, file):
                        # add the path to the report
                        report.write(os.path.join(root, file)+"\n")
                        file_count+=1
            # add file count and the source_dir for later use
            report.write("!! File Count: "+str(file_count)+" !!\n")
            report.write("source_dir="+source_dir+"\n")
        return report_path

    # moves all of the files from the report to a destination directory
    def move_files(self, report_name, destination_dir):
        # TODO

        with open(report_path, "w") as report:
            for line in report:
                # TODO filter out "!!" comments

                # TODO should be rel path or use absolute path
                dst = destination_dir
                os.rename(line, dst)


    def conditions_apply(self, conditions, file):
        # TODO
        return True


    def __handle_error(self, error_instance):
        # TODO
        print("!! ERROR: could not find file !!")


    def __name_report(self, report_name):
        if report_name is "":
            return time.strftime("%Y%m%d-%H%M%S")
        else:
            return report_name


# testing purposes 
# TODO: remove
if __name__ == "__main__":
    m = Model(reports_dir=".beehive_reports")
    m.run_report("test", report_name="my_report")