from argparse import ArgumentParser
from json import loads, dumps
from os import path
from tempfile import gettempdir

storage_path = path.join(gettempdir(), 'storage.data')


def get_data():
    if path.exists(storage_path):
        with open(storage_path, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return loads(raw_data)
    return {}


def put(key_name, value):
    dict_key_value = get_data()
    if key_name not in dict_key_value:
        dict_key_value[key_name] = []
    dict_key_value[key_name].append(value)
    with open(storage_path, 'w') as f:
        f.write(dumps(dict_key_value))


def get_value(key):
    dict_key_value = get_data()
    if key in dict_key_value:
        return ", ".join(dict_key_value.get(key))
    return "None"


parser = ArgumentParser(add_help=False)
parser.add_argument("--key", help="Key")
parser.add_argument("--val", help="Val")
args = parser.parse_args()
if args.key and args.val:
    put(args.key, args.val)
else:
    print(get_value(args.key))
