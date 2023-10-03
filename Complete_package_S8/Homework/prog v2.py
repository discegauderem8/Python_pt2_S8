import os

def get_directory_info(path):
    if not os.path.exists(path):
        return None

    directory_info = []

    for root, directories, files in os.walk(path):
        dir_size = sum(os.path.getsize(os.path.join(root, filename)) for filename in files)
        dir_info = {
            'path': os.path.relpath(root, path),
            'type': 'директория',
            'size_bytes': dir_size,
        }
        directory_info.append(dir_info)

        for filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_info = {
                'path': os.path.relpath(file_path, path),
                'type': 'файл',
                'size_bytes': file_size,
            }
            directory_info.append(file_info)

    total_size = sum(item['size_bytes'] for item in directory_info)

    return directory_info, total_size

if __name__ == "__main__":
    directory_path = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S8"
    result_data, total_size = get_directory_info(directory_path)

    if result_data is not None:
        print("Содержимое директории:")
        for item in result_data:
            print(f"Path: {item['path']}, Type: {item['type']}, Size: {item['size_bytes']} bytes")

        print(f"Суммарный размер: {total_size} bytes")
    else:
        print(f"Указанная директория не существует или не доступна.")
