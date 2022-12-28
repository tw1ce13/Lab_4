import json

class Point:
    def __init__(self):
        self.width = 0
        self.longitude = 0

    def width(self):
        return self.width

    def longitude(self):
        return self.longitude

    def display_info(self):
        print("Долгота = ", self.longitude)
        print("Широта = ", self.width)

    def json_load(self, file_path:str):
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.width = data["Place"]["width"]
            self.longitude = data["Place"]["longitude"]


class City(Point):
    def __init__(self):
        self.name = ""
        self.people_count = 0
        super().__init__()

    def display_info(self):
        super().display_info()
        print("Название города: ", self.name)
        print("Население города = ", self.people_count)

    def json_load(self, file_path:str):
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.name = data["City"]["name"]
            self.people_count = data["City"]["people_count"]
        super().json_load(file_path)

    def json_upload(self, file_path:str):
        to_json = {
            "City":{
                "name": self.name,
                "people_count": self.people_count
            },
            "Place":{
                "width": super().width(),
                "longitude": super().longitude()
            }
        }
        with open(file_path, 'w') as f:
            json.dump(to_json, f, indent=8)




p = City()
p.json_load('data_file.json')
p.json_upload('upload_data.json')
p.display_info()