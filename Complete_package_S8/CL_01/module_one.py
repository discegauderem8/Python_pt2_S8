import json

with (open("task_one_in.txt", "r", encoding="utf-8") as f,
      open("out.json", "w", encoding="utf-8") as out):
    content = [i for i in f.readlines() if i != "\n"]
    for i in range(len(content)):
        this_item = content[i].split(":")
        content[i] = [this_item[1].title(), this_item[0]]

    res = json.dump(content, out, ensure_ascii=False, indent=2)
