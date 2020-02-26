import pandas as pd
import csv


def import_csv():
    file = input("\nFile (.csv): ")
    try:
        pd.read_csv(file)
        get_header(file)
    except FileNotFoundError:
        if file == 'q':
            print("Quit")
            exit(0)
        elif file == '':
            file = 'test_file.csv'
            print(f"CVS file = {file}")
            get_header(file)
        else:
            print("Not valid file!\n")
            import_csv()


def get_header(file):
    with open(file) as f:
        d_reader = csv.DictReader(f)

        # get fieldnames from DictReader object and store in list
        header = d_reader.fieldnames
    print(f"Header = {header}")
    return header


import_csv()
