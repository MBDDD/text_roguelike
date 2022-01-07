import glob
import random
from classes import *
name_list = []

def adventure():  # Приключение
    print(color.yellow + 'Используйте следующие команды:' + color.end)
    print('1 - Идти в следующую комнату\n'
          '2 - Вернуться в город')
    event = ['treasure', 'goblin', 'trap', 'empty']
    chance = ['True', 'False']
    adventure.hp = parameter.hp
    adventure.treasure = 0
    adventure.room = 0
    while adventure.hp > 0:
        command = int(input('Команда:'))
        if command == 1:
            ev = random.choice(event)
            if ev == 'treasure':
                adventure.treasure += 1
                adventure.room += 1
                print(color.green + 'В комнате Вы нашли сокровище' + color.end)
                print('Сокровища:', adventure.treasure)
            if ev == 'goblin':
                adventure.hp -= 1
                adventure.room += 1
                print(color.red + 'В комнате Вы встретили гоблина, Вы теряете здоровье' + color.end)
                print('Здоровье:', adventure.hp)
            if ev == 'trap':
                adventure.room += 1
                print(color.yellow + 'В комнате ловушка' + color.end)
                trap_chance = random.choice(chance)
                if trap_chance == 'True':
                    print(color.green + 'Вы успешно обезвредили её' + color.end)
                if trap_chance == 'False':
                    print(color.red + 'Вы не смогли её обезвредить, Вы теряете здоровье' + color.end)
                    adventure.hp -= 1
                    print('Здоровье:', adventure.hp)
            if ev == 'empty':
                adventure.room += 1
                print('Вы попали в пустую комнату')
        if command == 2:
            parameter.command = 'finish adventure'
            parameter.adventure += 1
            print(color.yellow + 'Вы закончили поход' + color.end)
            print(color.blue + 'Статистика похода:\n'
                               f'Собрано сокровищ:{adventure.treasure}\n'
                               f'Комнат исследовано:{adventure.room}' + color.end)
            autosave()
    if adventure.hp == 0:
        print(color.red + 'Вы погибли. Игра окончена' + color.end)
        print(color.blue + 'Итоговая статистика\n'
                           f'Имя: {parameter.name}\n'
                           f'Монеты: {parameter.money}\n'
                           f'Сокровище: {parameter.treasure}\n'
                           f'Кол-во успешных походов: {parameter.adventure}' + color.end)
        exit()

def autosave():
    if parameter.command == 'finish adventure':
        parameter.money -= 10
        parameter.treasure += adventure.treasure
        parameter.hp = adventure.hp
    if parameter.command == 1:
        if parameter.treasure == 0:
            print(color.red + 'У Вас нет сокровищ на продажу' + color.end)
        else:
            print(color.green + 'Вы успешно продали сокровище' + color.end)
            parameter.money += 5
            parameter.treasure -= 1
    if parameter.command == 2:
        print(color.green + 'Вы успешно пополнили здоровье' + color.end)
        parameter.hp = 3
    if parameter.command == 3:
        adventure()
    if parameter.command == 4:
        start()
    file = open(f'{parameter.name}.txt', 'w+')
    file.write(f'Имя: {parameter.name}\n'
               f'Здоровье: {parameter.hp}\n'
               f'Монеты: {parameter.money}\n'
               f'Сокровище: {parameter.treasure}\n'
               f'Кол-во успешных походов: {parameter.adventure}')
    file.close()
    print(color.green + 'Изменения сохранены' + color.end)
    city()

def city():  # Город
    a = parameter.money + (parameter.treasure * 5)
    if a < 10:
        print(color.red + 'У Вас не хватает денег для последующих походов. Игра окончена' + color.end)
        print(color.blue + 'Итоговая статистика\n'
                           f'Имя: {parameter.name}\n'
                           f'Монеты: {parameter.money}\n'
                           f'Сокровище: {parameter.treasure}\n'
                           f'Кол-во успешных походов: {parameter.adventure}' + color.end)
        exit()
    file = open(f'{parameter.name}.txt', 'r')
    info_list = file.readlines()
    file.close()
    parameter.hp = int(info_list[1][10:])
    parameter.money = int(info_list[2][8:])
    parameter.treasure = int(info_list[3][11:])
    print(color.blue + f'Имя: {parameter.name}\n'
                       f'Здоровье: {parameter.hp}\n'
                       f'Монеты: {parameter.money}\n'
                       f'Сокровище: {parameter.treasure}\n'
                       f'Кол-во успешных походов: {parameter.adventure}' + color.end)
    print(color.yellow + 'Выберите нужную команду:' + color.end)
    print('1 - Продать одно сокровище (+5 монет)\n'
          '2 - Восполнить здоровье (бесплатно)\n'
          '3 - Отправиться в поход (-10 монет)\n'
          '4 - Выйти в главное меню')
    parameter.command = int(input('Команда:'))
    autosave()

def start():
    name_list.clear()
    for filename in glob.glob('*txt'):
        name_list.append(filename)
    if len(name_list) == 0:
        print('Введите имя нового героя' + color.end)
        parameter.name = input('Имя: ')
        new_hero()
    if len(name_list) > 0:
        print('Доступные герои:')
        for i in name_list:
            print(i[:-4])
        parameter.name = input('Введите имя героя, за которого хотите продолжить игру\n'
                               'или пропишите имя нового героя, чтобы создать его: ')
        if (f'{parameter.name}.txt') in name_list:
            print('not new')
            city()
        else:
            print('new')
            new_hero()

def new_hero():
    print(parameter.name)
    file = open(f'{parameter.name}.txt', 'w+')
    file.write(f'Имя: {parameter.name}\n'
               f'Здоровье: {3}\n'
               f'Монеты: {100}\n'
               f'Сокровище: {0}\n'
               f'Кол-во успешных походов: {0}')
    file.close()
    print(color.green + 'Вы успешно создали нового героя' + color.end)
    city()
