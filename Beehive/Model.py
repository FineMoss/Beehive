
# Created by Jake Stephens


import os
# import sys
# import shutil
# import datetime


class Model():

    # default reports directory name is ".reports"
    # default extension is ".report"
    def __init__(self, reports_dir=".reports", extension=".report"):
        self.reports_dir = reports_dir
        self.extension   = extension
        # make sure there is a reports direcory
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)

    # creates a report with report_name.extension in reports_dir and
    # adds path of files from source_path that the fit the conditions to the report
    def run_report(self, report_name="", source_dir="", conditions={}):
        report_path = os.path.join(self.reports_dir, report_name+self.extension)
        report      = open(report_path, "w")
        file_count  = 0
        # recursively walk the directory tree
        for root, dirs, files in os.walk(source_dir, onerror=self.handle_error):
            for file in files:
                # if the file meets the conditions
                if self.conditions_apply(conditions, file):
                    report.write(os.path.join(root, file)+"\n")
                    file_count+=1

        report.write("!! File Count: "+str(file_count)+" !!\n")
        report.close()




    def conditions_apply(self, conditions, file):
        return True


    def handle_error(self, Error_instance):
        print("!! ERROR: could not find file !!")



# testing purposes 
if __name__ == "__main__":
    m = Model(reports_dir=".beehive_reports")
    m.run_report(report_name="my_report", source_dir="test")