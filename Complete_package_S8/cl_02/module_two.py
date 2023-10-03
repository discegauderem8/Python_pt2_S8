import json
import os


def insert_data(pathname):
    if os.path.exists(pathname):
        with open(pathname, "r+", encoding="utf-8") as out:

            ids = set()
            complete_data = {}
            if os.path.getsize(pathname) != 0:
                complete_data = json.load(out)
                for key in complete_data.keys():
                    ids.add(key)

            while True:
                data_piece = input("Введите имя, id и уровень доступа (1-7) через пробел или q, чтобы выйти:  ")
                if data_piece.lower() == "q":
                    break
                data = data_piece.split()

                if data[0] in ids:
                    print("id занят, введите другой")
                    continue
                elif int(data[2]) not in range(1, 8):
                    print("такого кода доступа нет")
                    continue
                elif data[1].strip() == "":
                    print("вы не ввели имя")
                    continue

                ids.add(data_piece[1])
                print(data)

                res = {data[0]: [data[1], int(data[2])]}
                complete_data.update(res)

                out.seek(0)
                json.dump(complete_data, out, ensure_ascii=False, indent=1, sort_keys=True)



insert_data("out2.json")
