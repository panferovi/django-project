import json
from marshmallow_dataclass import class_schema
from dataclasses import asdict


def from_json(filename, cls):
    """Function allows to load json object from file on the server"""
    data = None
    with open(filename, "r", encoding="utf-8") as f:
        data = json.loads(f.read())

    schema = class_schema(cls)()
    try:
        obj_arr = []
        for obj in iter(data):
            obj_arr.append(schema.load(obj))
        return obj_arr
    except BaseException:
        return schema.load(data)


def to_json(filename, obj):
    """Function allows to store json object from file on the server"""
    items = None
    try:
        items = [asdict(item) for item in obj]
    except BaseException:
        items = asdict(obj)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(items, f)
