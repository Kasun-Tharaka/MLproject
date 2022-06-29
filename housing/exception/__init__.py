import os
import sys

#declair the parent vlass
class HousingException(Exception):
    
    #error_message wil be Object of Exception class, and error_details will be Object of sys class. 
    # so we can capture all of details through objects
    def __init__(self, error_message:Exception, error_details:sys):
        #passing the error message to Exception class
        super().__init__(error_message)
        self.error_message = error_message


    #using this we can call this function without creating any object
    @staticmethod
    def get_detail_error_message(self, error_message:Exception, error_details:sys)->str:
        """
        error_message : Exception object
        error_detail : object of sys module
        """
        _,_ , exec_tb = error_details.exc_info()

        # getting line number of the error
        line_number = exec_tb.tb_frame.f_lineno

        # getting file name of the error
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"

        return error_message


    def __str__(self):
        return self.error_message