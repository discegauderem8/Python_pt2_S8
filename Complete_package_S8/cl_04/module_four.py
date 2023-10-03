import csv
import json


def export_csv_to_json(csv_file: str, json_file: str):
    final_dict = {}
    with open(csv_file, "r", encoding="utf-8") as file:
        data = file.readlines()
        for i, items in enumerate(data):
            data[i] = data[i].strip().split("\t")
            data[i][0] = data[i][0].zfill(10)
            final_dict[hash(data[i][0] + data[i][1])] = data[i]
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(final_dict, file, indent=4, ensure_ascii=False)

csv_path = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S8\003\out2.csv"
json_path = r".\new_out.json"
export_csv_to_json(csv_path, json_path)