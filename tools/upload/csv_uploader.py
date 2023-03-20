#!/bin/python
import subprocess
import sys
import getopt
import csv
import os
from tools.upload.BankEnum import BankEnum

# post bash file processing
# @input_file csv file path from command line
# returns file ready to store to db

def prepare_file(formatting_script, input_file):
    # procss file by bash script
    bash_result_file = subprocess.run(
        
        [formatting_script + " " +  input_file], stdout=subprocess.PIPE, shell=True)

    # print("bash_result_file is : {} of type : {}".format(bash_result_file, type(bash_result_file)))

    # fix file encoding to urf-8 so as polish signs are properly presented
    decoded_file = (bash_result_file.stdout).decode("utf-8")
    # cut last two characters since input file contains \n - new line sign
    final_file = decoded_file[slice(0, -1, 1)]
    # print("Processed file  is : {} of type : {}".format(
    #     final_file, type(final_file)))
    return final_file

def process_csv(bank, input_file):
    print('csv_uploader.py process_csv called')
    formating_script = reslove_formating_script(bank)
    processed_file = prepare_file(formating_script, input_file)
    
    return processed_file

def reslove_formating_script (bank):
    print('csv_uploader.py#resolve_formating_script called with arg: ' + bank )
    try: 
        b=BankEnum();
        script = b.get_bank_enum_by_name(bank.upper())
        print('scrpit: '+ script)
        return script
    except ValueError :  
        print ("Sript not found based on provided bank argument:" + bank)
