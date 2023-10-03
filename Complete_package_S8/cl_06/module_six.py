import csv
import pickle
import json

pickle_path = r"../cl_05/new_out.pickle"
csv_path = r"./csv_out.csv"

def read_pickle(pathname):
    with open(pathname, "rb") as pickle_file:
        data = pickle.load(pickle_file)
    return data

def create_csv_table(data_csv: dict):
    csv_headers = list(data_csv.keys())
    csv_table = list(data_csv.values())
    csv_table = list(zip(*csv_table))
    with open (csv_path, "w", encoding="utf-8") as file:
        csv_writer = csv.writer(file, dialect="excel", delimiter = " ")
        csv_writer.writerow(csv_headers)
        csv_writer.writerows(csv_table)


data = read_pickle(pickle_path)
create_csv_table(data)