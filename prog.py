import os

pathname = ".."


def get_file_data(main_dir: str):
    if not os.path.exists(main_dir):
        print("Директории не существует")
        return

    file_list = {}
    for root, directories, files in os.walk(main_dir):
        dir_data = directories
        for i in range(len(dir_data)):
            print(root)
            print(dir_data[i])
            dir_data[i] = (dir_data[i], f"Папка весом в {os.path.getsize(os.path.join(root, dir_data[i]))}")
        file_list[root] = [dir_data, files]

    for key, value in file_list.items():
        print(f"Корневая папка: {key}")
        print(f"Вложенные папки: {value[0]}")
        print(f"Файлы: {value[1]}")


get_file_data(pathname)
