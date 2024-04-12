import sys

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python scrits {0} and line no {1} and error message is {2}".format(filename,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)

    def __str__(self) -> str:
        return self.error_message