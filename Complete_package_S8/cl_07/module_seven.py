import csv
import pickle

csv_path = r"../cl_06/csv_out.csv"
pickle_path = r"./out.pickle"

def read_csv (pathname: str):
    result = ""
    with open (pathname, "r", encoding="utf-8") as csv_in:
        csv_reader = csv.reader(csv_in)
        for i in [i for i in csv_reader if len(i) > 0]:
            result += "".join(i)
    return result


def print_pickle_string (pathname: str, csv_path):
    data = read_csv(csv_path)
    pickle_string = pickle.dumps(data)
    print(pickle_string)


print_pickle_string("", csv_path)

