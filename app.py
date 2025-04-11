import json
# Загружаем список номеров из файла
def load_rooms():
    with open('rooms.json', 'r') as file:
        return json.load(file)