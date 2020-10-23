import json


class ReadFromJson:
    def __init__(self, json_path):
        self._json_path = json_path

    def read_from_json(self):
        return self._read_from_json()

    def _read_from_json(self):
        with open(self._json_path, encoding='utf-8-sig') as json_file:
            return json.load(json_file)
