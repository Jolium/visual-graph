import pandas as pd
import plotly.express as px
import csv

file_csv = 'elextraflex.csv'
rapport_title = 'ElectraFlex Rapport'


def data_frame(file):
    """Import the file"""
    df = pd.read_csv(file)
    return df


def get_file_header(file):
    """Get the headers of the file"""
    with open(file) as f:
        d_reader = csv.DictReader(f)

        # Get fieldnames from DictReader object and store in list
        headers = d_reader.fieldnames
    return headers


def show_chart(title, df, header):
    """Show chart on browser

    == Just for reference ==
    header[0] = 'categories'
    header[1] = 'subcategories'
    header[2] = 'number of incidents'
    header[3] = 'incident number'
    """
    # Shows per subcategory
    fig_sub = px.bar(df,
                     x=header[1],
                     y=header[2],
                     title=title,
                     hover_name=header[0],
                     hover_data=[header[3]],
                     )

    # Shows per category
    fig_cat = px.bar(df,
                     x=header[0],
                     y=header[2],
                     title=title,
                     hover_name=header[1],
                     hover_data=[header[3]],
                     )

    fig_sub.show()
    fig_cat.show()


show_chart(rapport_title, data_frame(file_csv), get_file_header(file_csv))
