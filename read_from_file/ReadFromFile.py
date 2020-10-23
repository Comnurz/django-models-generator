from read_json import ReadFromJson


class ReadJson:
    @staticmethod
    def read_json_file():
        read_json = ReadFromJson("/Users/caglanursaglam/Projects/django-models-generator/tests/schema.json")

        return read_json.read_from_json()
