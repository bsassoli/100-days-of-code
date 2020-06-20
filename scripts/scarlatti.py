"""
A simple app to manage todos for our new home
"""
from openpyxl import Workbook


class Room():
    def __init__(self, name):
        self.name = name


file_name = input('What do you want you filename to be? ')
workbook = Workbook()

rooms = []

answer = ''

while answer != 'Done':
    answer = input('Write the name of a room (or "Done" when done): ')
    if answer != 'Done':
        rooms.append(answer)


for room in rooms:
    sheet = workbook.create_sheet(room)
workbook.save(filename=file_name+'.xlsx')

rooms_dic = {room: Room(room) for room in rooms}
print(rooms_dic)
