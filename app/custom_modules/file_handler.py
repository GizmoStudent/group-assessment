"""
This file holds file operations for CRUD
Create, Read, Update, Delete
"""
# python / system modules
from os import path, listdir
import csv, json

# custom imports
from app import APP_ROOT

#Add a global for the file_handler module
DATA_FILES_LOC = path.join(APP_ROOT, "data_files")


def path_exists(filepath, dir=False):
    """
    A simple function to check if a file or folder exists
    :param filepath:    filepath to check
    :type filepath:     string
    :param dir:         is it a directory
    :type dir:          boolean
    :return:            True or False
    :rtype:             Boolean
    """
    if dir:
        if path.exists(filepath):
            return True
    else:
        if path.isfile(filepath):
            return True

    return False


def read_csv_file(filepath):
    """
    read csv file 'filename' and create a dict with the results.
    :param filepath:    csv filename and loaction
    :type filepath:     string
    :return:            contents of CSV
    :rtype:             list of dicts
    """
    data = []
    with open(filepath, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_file(data, fname="output.json"):
    """
    Output data (dict) to filename.
    Creates file in the custom_modules directory.
    :param data:    json to write to a file
    :type data:     dict
    :param fname:   file name defaulting to 'output.json'
    :type fname:    string
    :return:        N/A
    :rtype:         N/A
    """
    with open(fname, 'w') as f:
        f.write(json.dumps(data))
    return


def load_files_in_directory(directory):
    """
    Loop through each of the csv files in 'directory'
    :param directory:   directory to loop through to load files.
    :type directory:    string
    :return:            all of the csvs in directory
    :rtype:             dict
    """

    loaded_data = []
    # for .csv file in directory
    for f in listdir(path.join(DATA_FILES_LOC, directory)):
        if f.endswith(".csv"):
            loaded_data.extend(load_file(path.join(DATA_FILES_LOC, "crime_files", f)))
        else:
            continue
    return loaded_data


def load_file(fpath, in_data_files=True):
    """
    loads fpath.
    :param fpath: file path (inc filename and ext)
    :type fpath: string
    :return: returns the contents of the csv
    :rtype: dict
    """
    if in_data_files:
        file_path = path.join(DATA_FILES_LOC, fpath)
    else:
        file_path = fpath

    if path_exists(file_path):
        return read_csv_file(file_path)
    else:
        print(f"Could not read file {file_path}")


# Version 1
# Date Creation 9/3/2021
# File output-er function for crime data
# This takes values from the dictionary and outputs data into a csv

def file_outputer(name_of_file,crime_data):
    fields = []
    file_name = name_of_file + ".csv"
    for data in crime_data:
        for d in data:
            fields.append(d)

# dynamically created fields using keys
    field_names = list(dict.fromkeys(fields))

    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(crime_data)

# Example code run file_outputer("testing", crime_data)



if __name__ == '__main__':
    # print(path_exists(DATA_FILES_LOC, dir=True))
    # print(load_files_in_directory("crime_files"))
    write_file(load_file(path.join("postcodes", "postcodes.csv")), 'postcodes.json')
