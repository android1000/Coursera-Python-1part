from random import randint

print(bool(0.0000000001))
print("привет"[0:1])

pi = 3.1415926
pi_fmt = f"{pi:#0.2f}"
#print(type(pi_fmt))

byte_str="&#1047;&#1085;&#1072;&#1095;&#1077;&#1085;&#1080;&#1077; &#1069;&#1062;&#1055; &#1085;&#1077; &#1087;&#1088;&#1086;&#1096;&#1083;&#1086; &#1087;&#1088;&#1086;&#1074;&#1077;&#1088;&#1082;&#1091;."

byte_str.replace("&#",r"\u")
print(byte_str)

'''number = randint(0, 100)
print(number)
while True:
    answer = input("Введите число: ")
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print("Введите правильное число!")
        continue
    user_answer = int(answer)
    if user_answer > number:
        print("Загаданное число меньше")
    elif user_answer < number:
        print("Загаданное число больше")
    else:
        print("Поздравляем")
        break
'''


