
# Created by Jake Stephens


class Control():

    # create reference to the model and the view
    def __init__(self, model, view):
        self.__model = model
        self.__view  = view
        self.__map_buttons()

    # maps the buttons to the commands
    def __map_buttons(self):
        self.__view.archive_button["command"] = self.__archive
        self.__view.clear_button["command"]   = self.__clear
        self.__view.confirm_button["command"] = self.__confirm
        self.__view.cancel_button["command"]  = self.__cancel

    # command for archive button
    def __archive(self):
        source_dir  = str(self.__view.current_entry.get())
        conditions = self.__get_conditions()
        
        # TODO add name to report
        self.report_path = self.__model.run_report(source_dir, conditions=conditions)
        self.__update_text_field()
        self.__lock_fields()

    # helper for __archive()
    def __get_conditions(self):
        # TODO add more conditions
        return {str(self.__view.date_entry.get()) : self.__model.date_condition}

    # command for confirm button
    def __confirm(self):
        destination_dir = str(self.__view.target_entry.get())
        self.__model.move_files(self.report_path, destination_dir)
        self.__unlock_fields()

    # command for cancel button
    def __cancel(self):
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"
        self.__unlock_fields()

    # command for clear button
    def __clear(self):
        self.__view.current_entry.delete("0", "end")
        self.__view.target_entry.delete("0", "end")
        self.__view.date_entry.delete("0", "end")
        self.__view.text_field["state"] = "normal"
        self.__view.text_field.delete("1.0", "end")
        self.__view.text_field["state"] = "disabled"

    def __update_text_field(self):
        # TODO make sure path exist
        with open(self.report_path, "r") as report:
            self.__view.text_field["state"] = "normal"
            self.__view.text_field.delete("1.0", "end")
            self.__view.text_field.insert("1.0", report.read())
            self.__view.text_field["state"] = "disabled"

    # helper function
    def __lock_fields(self):
        self.__view.current_entry["state"]  = "disabled"
        self.__view.target_entry["state"]   = "disabled"
        self.__view.date_entry["state"]     = "disabled"
        self.__view.archive_button["state"] = "disabled"
        self.__view.clear_button["state"]   = "disabled"
        self.__view.confirm_button["state"] = "normal"
        self.__view.cancel_button["state"]  = "normal"

    # helper fuction
    def __unlock_fields(self):
        self.__view.current_entry["state"]  = "normal"
        self.__view.target_entry["state"]   = "normal"
        self.__view.date_entry["state"]     = "normal"
        self.__view.archive_button["state"] = "normal"
        self.__view.clear_button["state"]   = "normal"
        self.__view.confirm_button["state"] = "disable"
        self.__view.cancel_button["state"]  = "disable"