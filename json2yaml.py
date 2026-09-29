import json
from pathlib import Path
from io import StringIO
from shutil import copyfileobj

def json2yaml(file_json: Path, indent="  "):
    file_yaml = file_json.parent / (file_json.name.removesuffix(".json") + ".yaml")
    with open(file_json, "r", encoding="utf-8") as f:
        file_data: dict[str, str] = json.load(f)
    buff_yaml = StringIO()
    for k in file_data:
        buff_yaml.write(k + ": ")
        if file_data[k] is None:
            buff_yaml.write("null" + "\n")
            continue
        buff_yaml.write("|-" + "\n" + indent)
        for c in file_data[k]:
            buff_yaml.write(c)
            if c == "\n":
                buff_yaml.write(indent)
        buff_yaml.write("\n")
    with open(file_yaml, "w", encoding="utf-8") as f:
        buff_yaml.seek(0)
        copyfileobj(buff_yaml, f, -1)
    file_json.unlink()


for f in Path(".").rglob("**.json"):
    if f.is_dir():
        continue
    if f.parent.parent is not "text":
        continue
    json2yaml(f)
