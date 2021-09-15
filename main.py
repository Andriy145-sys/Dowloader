# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""import sys
import pygame as pg

def run_game():
    pg.init()
    screen = pg.display.set_mode((1400, 800))
    pg.display.set_caption("Revers Tetris")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pg.display.flip()

run_game()"""
import random
import instaloader
import phonenumbers as ph
from pytube import YouTube
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

def numbers():
    number = input("Введіть номер телефону: ")
    number = ph.parse(number)
    print(timezone.time_zones_for_number(number))
    print(carrier.name_for_number(number, "en"))
    print(geocoder.description_for_number(number, "en"))

def instaload():
    ig = instaloader.Instaloader()
    dp = input("Введіть username користувача: ")
    ig.download_profile(dp, profile_pic=True)
    print("Успішно завантажено")
    return main()

def run_apl():
     link = input("Введіть url відео з ютуба : ")
     yt = YouTube(link)
     print("Відео:", yt.title, yt.rating)
     print("Ви впевнені,що бажаєте завантажити це відео?")
     a = int(input())
     if(a == 1):
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Відео успішно завантажено")
        return main()
     else:
        return run_apl()

def generate_password():
    small = "qwertyuiopasdfghjklzxcvbnm"
    big = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "1234567890"
    symbol = "{[}]'';:.,><"
    all = small + big + number + symbol

    lengt = 16
    password = "".join(random.sample(all,lengt))
    print("Ваш пароль: ",password)
    return main()

def ch():
    i = 0
    name = "Andriy Petro Ivan"
    print(name)
    print(1, 2, 3,sep=", ", end=". ")
    while i<10:
        print(i)
        i+=1
    for i in 1, 2, 3:
        print(i)
    sum = 0
    n = 5
    for i in range(1, n + 2):
        sum += i
        print("sum: ",sum)
        print("i: ",i)
    print(sum)
def main():
    print("Завантажити аватарку користувача інстаграм(1)")
    print("Завантажити відео з ютуб(2)")
    print("Сгенерувати пароль(3)")
    print("Дані по номеру телефону(4)")
    a = int(input())
    if(a == 1):
       instaload()
    if(a == 2):
       run_apl()
    if(a == 3):
       generate_password()
    if(a == 4):
       numbers()
    if(a == 5):
        ch()

main()
"""
link = input("Введіть url відео з ютуба : ")
print("1")
yt = YouTube(link)
print("2")
print("Title: ",yt.title)
print("Description: ",yt.description)
videos = 144
print("3")

#video = list(enumerate(videos))

print("2")

#for i in video:
 #   print(i)
print("3")
print("Введіть формат завантаження")
dn_option = int(input("Формат:"))
dn_video = videos
dn_video.download()

print("Завантажено успішно")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    names = input("Як вас звати?")
    age = input("Скільки вам років?")
    i=10
    print(f'Hi, {names}')# Press Ctrl+F8 to toggle the breakpoint.
    print(f"You age {age+str(i)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
