#!/bin/python
import sys
from tools.upload.csv_uploader import process_csv
import getopt

BANK_INPUT = 'bank'
FILE_INPUT = 'input_file'

def main(argv):
    input_params = process_input_params(argv);
    # print (input_params)
    print(input_params[BANK_INPUT] + " file " + input_params[FILE_INPUT]);
    # store_to_database = False;
    processed_csv = process_csv(input_params[BANK_INPUT], input_params[FILE_INPUT])

def process_input_params(argv):
    """
     obtain and validate input file arguments when starting script

     :type argv: array of strings -b bank name -i input file
     :param argv:

     :raises:

     :rtype: dictionary if form {"bank":some bank name, "input_file": some path }
    """
    input_params = get_from_input(argv)
    # TODO ARTUR validate input params

    return input_params


def get_from_input(argv):
    """ Description
       :type argv: String
       :param argv: string input parameters should be -b bank name -i file path
       :raises: GetoptErro if params cannot be obtained
       :rtype: dictionary if form {"bank":some bank name, "input_file": some path }
    """
    input_params = dict();
    try:
        opts, args = getopt.getopt(argv, "b:i:")
    except getopt.GetoptError:
        print('error with input params')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-b"):
            input_params["bank"] = arg
        elif opt in ("-i"):
            input_params["input_file"] = arg
    return input_params


if __name__ == "__main__":
    main(sys.argv[1:])
