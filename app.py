import json

print("Версия является учебной")

# Загружаем список номеров из файла
def load_rooms():
    with open('rooms.json', 'r') as file:
        return json.load(file)

# Сохраняем обновленные данные о номерах в файл
def save_rooms(rooms):
    with open('rooms.json', 'w') as file:
        json.dump(rooms, file, indent=2)

# Функция для бронирования
def reserve_room(room_id, guest_name):
    rooms = load_rooms()
    room = next((r for r in rooms if r['id'] == room_id), None)

    if not room:
        print('Ошибка: Номер не найден')
        return

    if room['reserved']:
        print(f'Ошибка: Номер {room_id} уже забронирован')
        return

    room['reserved'] = True
    room['guestName'] = guest_name
    print(f'Успех! Номер {room_id} забронирован на имя {guest_name}')

    # Сохраняем обновленные данные
    save_rooms(rooms)


# Тестируем функцию
reserve_room('101', 'Иван Иванов')
reserve_room('102', 'Мария Петрова')
reserve_room('101', 'Алексей Смирнов')  # Этот номер уже забронирован
