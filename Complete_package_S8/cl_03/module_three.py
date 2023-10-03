import csv
import json
import os

def insert_data(json_path, csv_path):
    if os.path.exists(json_path):
        with open(json_path, "r+", encoding="utf-8") as json_file:
            ids = set()
            complete_data = {}
            if os.path.getsize(json_path) != 0:
                complete_data = json.load(json_file)
                ids = set(complete_data.keys())

            while True:
                data_piece = input("Введите имя, id и уровень доступа (1-7) через пробел или q, чтобы выйти:  ")
                if data_piece.lower() == "q":
                    break
                data = data_piece.split()

                if data[1] in ids:
                    print("id занят, введите другой")
                    continue
                elif int(data[2]) not in range(1, 8):
                    print("такого кода доступа нет")
                    continue
                elif not data[0]:
                    print("вы не ввели имя")
                    continue

                ids.add(data[1])
                print(data)

                res = {data[1]: {"name": data[0], "lvl": data[2]}}
                complete_data.update(res)

            json_file.seek(0)
            json.dump(complete_data, json_file, ensure_ascii=False, indent=1, sort_keys=True)

            with open(csv_path, "w+", encoding="utf-8", newline="") as csv_out:
                csv_writer = csv.DictWriter(csv_out, fieldnames=["id", "name", "lvl"], dialect="excel-tab", quoting=csv.QUOTE_ALL)
                csv_writer.writeheader()

                for key, value in complete_data.items():
                    print(value)
                    csv_writer.writerow({"id":key, "name":value["name"], "lvl":value["lvl"]})

    else:
        print("Указанного файла json не существует")

insert_data("out2.json", "out2.csv")
