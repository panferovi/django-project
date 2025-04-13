import json

def from_json(filename, cls):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.loads(f.read());

    try:
        objArr = []
        for obj in iter(data):
            objArr.append(cls.Schema().load(obj))
        return objArr;
    except:
        return cls.Schema().load(data);
