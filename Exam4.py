# ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.
# 1)Randint
# 2)strptime
# 3)day
# 4)month
# 5)strftime
# 6) timedelta
#7)sample




### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.
# open with
# 2)modhohi File
# 'r'	baroi khondan
# 'w'	baroi navistan yo yagon tagirot darovardan
# 'x'	fayli nav sokhtan  va kushodani on baroi navishtan
# 'a'	kushodan baroi navishtan va dabavit kardan az oxir
# 't'	text kardan
### 3 Question
# # Github чист? Командахои GitHub-ро фахмонед.
# github  yak ravzanaye meboshad ki odamon metavonand dar onjo proekthoi khudro guzorand.
# Onho metavonand ki yakjoya yak proectro pesh barand va ba on dastrasi paydo kardan
# git init
# git branch
# git add .
# git status









### 1 Question
# Write a Python program to insert an element at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]


# a = input()
# my_list = a.input().split() 
# n = input()
# k = int(input())
# if k < 0 or k > len(my_list):
#     print()
# else:
#     my_list.insert(k, n)
#     print( my_list)

### 2 Question
# Write program to print 2 days before, today, 2 days after 


# from datetime import datetime, timedelta
# today = datetime.now()
# duruz_pesh = today - timedelta(days=2)
# duruz_bad = today + timedelta(days=2)
# print("Two days before today:", duruz_pesh.strftime("%Y-%m-%d"))
# print("Today:", today.strftime("%Y-%m-%d"))
# print("Two days after today:", duruz_bad.strftime("%Y-%m-%d"))




# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.

# Input: 17.02.2024           Output: 12.02.2024


# from datetime import datetime, timedelta
# a = input()
# n = datetime.strptime(a, "%d.%m.%Y")
# new_date = n - timedelta(days=5)
# print(new_date.strftime("%d.%m.%Y"))





### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 

# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10


# def sum_of_vowels(a):
#     my_dict = {
#                "A": 4, "E": 3, "I": 1, "O": 0, "U": 0,
#                "a": 4, "e": 3, "i": 1, "o": 0, "u": 0
#                }
#     cnt = 0
#     for i in a:
#         if i in my_dict:
#             cnt += my_dict[i]
#     print(cnt)
# sum_of_vowels(input())





# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# # input
#     3
# # otput
#     Tajikistan



# def read_line_n(a, n):
#     try:
#         with open(a, 'r') as file:
#             lines = file.readlines()
#             if n <= len(lines):
#                 return lines[n-1].strip()
#             else:
#                 return "In index mavjud nest"
#     except FileNotFoundError:
#         return "File not found."
# a = 'my_file.txt'
# n = int(input())
# print(read_line_n(a, n))  



### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 


# a = 'my_file.txt'  
# n = input()
# with open(a, 'r') as file:
#     k = file.readlines()
# for i in range(len(k)):
#     if (i + 1) % 2 != 0: 
#         k[i] = n + '\n' 
# with open(a, 'w') as file:
#     file.writelines(k)
# print(n)





# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5



# import random, string
# a = int(input())
# b = string.ascii_letters + string.digits + string.punctuation
# if a > len(b):
#     print()
# else:
#     password = ''.join(random.sample(b, a))
#     print(password)



### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}



# n=int(input())
# my_dict = {i: i**2 for i in range(1, n+1)}
# print(my_dict)




### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical.
# Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. 
# Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.

# Input       
# char_appears("She sells sea shells by the seashore.", "s")

# Output
# [1, 2, 1, 2, 0, 0, 2]





# def Yoftani_harf(n, a):
#     n = n.lower()
#     a = a.lower()
#     words = n.split()
#     cnt = [i.count(a) for i in words]
#     return cnt
# res = Yoftani_harf(input(),input())
# print(res) 



