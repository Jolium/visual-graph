import pandas as pd
import csv


df = pd.read_csv('elextraflex.csv')

with open('elextraflex.csv') as f:
    d_reader = csv.DictReader(f)

    # get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames


print(headers[0])
