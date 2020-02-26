import pandas as pd
import plotly.express as px
import csv


def get_file():
    print("\nPath to file (C:\\Users\\Documents\\File_name.csv)")
    print("If in the same folder just file name (File_name.csv)")
    print("Press 'ENTER' to see default chart")
    print("Press 'q' to quit")
    file = input("\nFile (.csv): ")
    if file == 'q':
        exit(0)
    else:
        check_file(file)


def check_file(file):
    if file == '':
        file = 'elextraflex.csv'
        return file
    while True:
        try:
            print(f"1 {file}")
            pd.read_csv(file)
            print(f"2 {file}")
            break
        except FileNotFoundError:
            print(f"'{file}' is not a valid file!\n")
            get_file()


def get_header():
    with open('elextraflex.csv') as f:
        d_reader = csv.DictReader(f)

        # get fieldnames from DictReader object and store in list
        header = d_reader.fieldnames
    return header


def show_chart(file, header):
    print(f"=== {file} ====")
    df = pd.read_csv(file)
    """
    == Just for reference ==
    header[0] = 'categories'
    header[1] = 'subcategories'
    header[2] = 'number of incidents'
    header[3] = 'incident number'
    """
    fig = px.bar(df, x=header[1], y=header[2],
                 title='ElectraFlex Rapport',
                 hover_name=header[0],
                 hover_data=[header[3]],
                 )

    fig.show()


show_chart(check_file(get_file()), get_header())
