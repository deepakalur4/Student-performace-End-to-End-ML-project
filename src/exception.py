import sys

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message=f"error occored at the file name {file_name} and line no {exc_tb.tb_lineno} and the error is {str(error)}"
    return error_message

class Custom_exception(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error=error_message,error_details=error_details)

    def __str__(self) -> str:
        return self.error_message
    


