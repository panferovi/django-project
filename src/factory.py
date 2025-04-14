import json
from marshmallow_dataclass import class_schema 
from dataclasses import asdict

def from_json(filename, cls):
    data = None
    with open(filename, "r", encoding="utf-8") as f:
        data = json.loads(f.read());

    schema = class_schema(cls)()
    try:
        objArr = []
        for obj in iter(data):
            objArr.append(schema.load(obj))
        return objArr
    except:
        return schema.load(data)

def to_json(filename, obj):
    items = None
    try:
        items = [asdict(item) for item in obj]
    except:
        items = asdict(obj)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(items, f)
