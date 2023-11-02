import os
from asyncio import*
from asyncio import sleep
import msvcrt
import client

Clear = lambda: os.system("cls")
client = client.Playar()
async def main():
    
    print("Приветствую тебя странник\n\nПредлагаю тебе сначала создать своего персонажа")   
    print("Нажми пробел чтобы начать приключение")
    char = msvcrt.getch()
    Clear()
    print("Для начала предлагаю создать персонажа")
    client.name = str(input('Введи имя своего персонажа: '))
    Clear()
    print(f" Отлично, теперь {client.name} нуждается в выборе навыков\n У тебя есть 10 очков опыта.\n Ты можешь потратить их на прокачку навыков твоего персонажа\n Всего есть 3 ветви прокачки персонажа: Сила, Интеллект и Ловкость - каждое внесет свой вклад в игровой процесс\n\n\n Чтож, ты готов? ")
    char = msvcrt.getch()
    Customization()
def Customization(): 
    client.power = int(input("Сколько очков опыта ты вложишь в Ловкость персонажа?\n")) 
    client.brain = int(input("Сколько очков опыта ты вложишь в Интеллект персонажа?\n"))
    client.speed = int(input("Сколько очков опыта ты вложишь в силу персонажа?\n"))
    if client.power +  client.brain + client.speed>10:
        Clear()
        print("У вас только 10 очков опыта!\nДавай попробуем еще раз")
        char = msvcrt.getch()
        Customization()
    else: 
        Start()

def Start():
    Clear()
    print(f"{client.name} просыпается в холодном поту, ему снова приснился кошмар. Он страдает уже 3 месяца после того как его отец погиб. На него напали гоблины, он храбро сражался и дал {client.name}у с матерью время для побега. Его разорвали у них на глазахъ\n\n")
    mmm = int(input("1. Пойти на кухню\n 2. Пойти в душ"))
    if mmm == 1: Kitchen()
    if mmm == 2: Bathroom()
    else: Start()

def Bathroom():
    Clear()
    print(f"{client.name} подходит к зеркалу и ему становится стыдно")
    print(f"{client.name} принимает душ и идет на кухню")
    Kitchen()

def Kitchen():
    Clear()
    print(f"{client.name} видит как его мать плачет и рассматривает фото отца")
    print(f"{client.name} не может на это смотреть и возвращается в свою комнату\n")
    mmm = int(input("1. Месть \n 2. Смирение"))
    if mmm == 1: TravelStart()
    if mmm == 2: TerpilaEnd()

def TerpilaEnd():
    print(f"{client.name} смирился с тем, что ничего не может сделать, через неделю его мать повесилась и он также свел счеты с жизнью \n")
run(main())
def TravelStart():
    print(f"{client.name} четко решил что отомстит за отца и их семья больше не будет жить в страхе\n")
    print(f"{client.name} видит золотые монеты, отложенные отцом на покупку коня\n")
    mmm = int(input("1. Взять деньги \n 2. Не брать деньги"))
    if mmm == 1: 
        print(f"Они и вправду мне пригодятся, подумал {client.name}")
        print(f"Вы взяли с полки {10} монет, отцовский боевой меч и легкую броню\n")
        print(f"У вашего персонажа 10 очков жизни, его меч наносит {client.weapons[0].Value}")
    if mmm == 2: TerpilaEnd()