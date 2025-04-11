import json
# Загружаем список номеров из файла
def load_rooms():
    with open('rooms.json', 'r') as file:
        return json.load(file)

# Сохраняем обновленные данные о номерах в файл
def save_rooms(rooms):
    with open('rooms.json', 'w') as file:
        json.dump(rooms, file, indent=2)
