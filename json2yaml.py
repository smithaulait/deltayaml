import json
import pathlib


def json2yaml(file_json: pathlib.Path, indent="  "):
    file_yaml = file_json.parent / (file_json.name.removesuffix(".json") + ".yaml")
    with open(file_json, "r", encoding="utf-8") as f:
        file_data: dict[str, str] = json.load(f)
    with open(file_yaml, "w", encoding="utf-8") as f:
        for k in file_data:
            f.write(k + ": " + "|-" + "\n" + indent)
            for c in file_data[k]:
                f.write(c)
                if c == "\n":
                    f.write(indent)
            f.write("\n")
    file_json.unlink()


for f in pathlib.Path(".").rglob("**.json"):
    if f.is_dir():
        continue
    json2yaml(f)
