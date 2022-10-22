from time import *
from random import *
import arts
import quest_soundracks as qs

card = False

def story_start():
    global card
    card = False
    qs.start_quest_sound()
    print("Вы проснулись в комнате")
    sleep(2)
    print("Вы осмотрелись")
    sleep(2)
    main_room()

def main_room():
    print("Вы видети две двери, рядом с одной что то есть, а у другой только ручка")
    sleep(2)
    choise = input("К какой двери пойдете?\n1 - Первой\n2 - Второй\n")
    if choise == "1":
        door1()
    elif choise == "2":
        door2()
    else:
        print("Не распознанно.")
        main_room()


def door2():
    print("Вы подошли к двери и дергаете ручку")
    sleep(1)
    print("Ручка работает и дверь открылась")
    choise = input("1 - Войти в комнату\n2 - Вернуться\n")
    if choise == "1":
        room1_1()
    elif choise == "2":
        main_room()
    else:
        print("Не распознанно.")
        door2()


def room1_1():
    global card
    print("Вы прошли в дверь и она захлопнулась")
    sleep(1)
    print("На полу лежит карта")
    sleep(0.5)
    print(arts.card_art)
    sleep(3)
    card = True
    print("Под картой была кнопка, и когда вы подняли карту\nСекретный проход открылся")
    sleep(5)
    choise = input("Проход начинается потихоньку закрываться...\n1 - БЕЖАТЬ В ПРОХОД\n")
    if choise == "1":
        can = randint(0, 5)
        if can >= 1:
            room1_2()
        else:
            print("Вы не успели")
            qs.bad_end_sound()
            for cycle in range(0, 5):
                sleep(1)
                print("...")
            print("Плохая концовка, проход закрылся и вскоре вы умерли")
            print("Нажмите любую клавишу что бы начать заново")
            input()
            story_start()
    else:
        print("Не распознанно.")
        room1_1()


def room1_2():
    print("Хух, вы успели забежать...")
    sleep(0.5)
    print("Перед вами экран на стене")
    sleep(1)
    print("И написанно:\n")
    sleep(1)
    print(arts.question)
    choise = input("1 - 4\n2 - 2\n")
    if choise == "1":
        print("Вау какой ты умный и ответил правильно(Сарказм)")
        sleep(2)
        print("КХМ.\nВы открылся проход и вы вышли в него")
        sleep(3)
        print("Это была та начальная комната.")
        sleep(3)
        main_room()
    elif choise == "2":
        print("Вау...")
        qs.bad_end_sound()
        sleep(2)
        print(". . .")
        sleep(2)
        print("Вы умерли, даже расписывать не хочу НАСТОЛЬКО тупую концовку")
        input("Нажмите любую клавишу что бы начать заново. БОЖЕ ДА КАК ТАК МОЖНО ОТВЕТИТЬ А????")
        story_start()
    else:
        print("Не распознано.")
        room1_2()


def door1():
    if card == False:
        print("Вы подошли к двери.")
        sleep(2)
        print("Рядом с ней было устройство для считывания карт")
        choise = input("Поскольку у вас нет карты\nЕсть только один вариант\n1 - Вернустья назад\n")
        if choise == "1":
            main_room()
        else:
            print("Не распознанно.")
            door1()
    else:
        room2()

def room2():
    print("Вы провели картой и прошли в следущую комнату")
    sleep(1)
    print("Есть еще одна дверь с ручкой, и окно в следущую комнату")
    choise = input("1 - Прыгнуть в окно(Там видно что это соиденительное окно между комнатами)\n2 - Еще одна дверь\n")
    if choise == "1":
        last_room()
    elif choise == "2":
        lol_room()
    else:
        print("Не распознано.")
        room2()

def lol_room():
    print("Вы вошли в комнату, там еще одна дверь")
    choise = input("1 - Пойти дальше\n2 - Вернуться\n")
    if choise == "1":
        print("Вы пошли в слейдущую комнату...")
        sleep(1)
        print("Вы пришли к такой же комнате")
        sleep(0.5)
        print("Вы оглянулись назад и увидели первую комнату с окном в двери")
        last_choise = input("1 - Вернуться в ту комнату с окном\n2 - Идти дальше\n")
        if last_choise == "2":
            print("Вы пошли в комнату")
            qs.inf_door_end_sound()
            sleep(0.1)
            print("Войдя в слейдущую дверь и оглянувшись назад вы не увидели комнату с окном...")
            sleep(2)
            print("Вы испугались, но пошли дальше")
            sleep(1)
            print(arts.inf_door_art)
            sleep(1)
            print("Плохая концовка, вы попали в цыкл и ходили пока у вас не иссякли силы.")
            sleep(2)
            input("Нажмите любую клавишу что бы начать занаво")
            story_start()
        elif last_choise == "1":
            room2()
        else:
            print("Не распознано.")
            lol_room()
    elif choise == "2":
        room2()
    else:
        print("Не распознано.")
        lol_room()

def last_room():
    print("Вы вошли в окно, но комната оказалось галограммой...")
    qs.true_end_sound()
    sleep(1)
    print("Вы падаете")
    sleep(0.5)
    print("...")
    sleep(2)
    print("Вы проснулись в комнате из начала")
    sleep(1)
    non_value_choise = input("1 - Встать\n")
    if non_value_choise == "1":
        print("Вы проснулись в холоном поту на полу и в одеяле")
        sleep(1)
        print(arts.bed_art)
        print("Истеная концовка, это был просто сон...")
        sleep(0.5)
        input("Нажмите любую клавишу что бы начать занаво")
        story_start()
    else:
        print("Не распознано.")
        last_room()

story_start()
