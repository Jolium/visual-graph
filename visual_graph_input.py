import pandas as pd
import plotly.express as px
import csv


file_csv = 'elextraflex.csv'
rapport_title = 'ElectraFlex Rapport'


def import_csv():
    print("\nPath to file (C:\\User\\Documents\\file_name.csv)")
    print("If in the same folder just file name (file_name.csv)")
    print("Press 'ENTER' to see default chart or 'q' to quit!")
    file = input("\nFile (.csv): ")
    try:
        pd.read_csv(file)
        get_header(file)
    except FileNotFoundError:
        if file == 'q':
            print("Quit!")
            exit(0)
        elif file == '':
            file = 'elextraflex.csv'
            print(f"File (.csv) = {file}")
            get_header(file)
        else:
            print("Not a valid file!\n")
            import_csv()


def get_header(file):
    with open(file) as f:
        d_reader = csv.DictReader(f)

        # get fieldnames from DictReader object and store in list
        header = d_reader.fieldnames
    show_chart(header, file)


def show_chart(header, file):
    """
    == Just for reference ==
    header[0] = 'categories'
    header[1] = 'subcategories'
    header[2] = 'number of incidents'
    header[3] = 'incident number'
    """
    fig = px.bar(pd.read_csv(file), x=header[1], y=header[2],
                 title='ElectraFlex Rapport',
                 hover_name=header[0],
                 hover_data=[header[3]],
                 )

    fig.show()


import_csv()
