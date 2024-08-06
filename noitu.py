import sys
import codecs
import io
import time
import random
from addon import check_similar_words
# Set the standard output and input to utf-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def ReadWord(file):
    list = []
    for line in file.readlines():
        inner_list = []
        for char in line.strip("\n"):  # Use strip() to remove newline characters
            inner_list.append(char)
        list.append(inner_list)
    return list

def HandleInputTail(s):
    for i in range(len(s)):
        if s[i] == " ":
            pos = i
    s = s[pos+1:]
    return s 

def HandleInputHead(s):
    for i in range(len(s)):
        if s[i] == " ":
            pos = i
    s = s[:pos]
    return s 

def BinarySearch(list,target):
    high = len(list)
    low = 0
    while (low <= high):
        mid = (low+high)//2
        x = HandleInputHead(list[mid])
        if target == x:
            return list[mid]
        if target < x:
            high = mid-1
        if target > x:
            low = mid + 1
    return '0'


#setup
bot_brain = []

#doc file tu dien
try:
    with codecs.open("C:\\Users\\hoang\\Python\\NoiTuProject\\dictionary.txt", "r", "utf-8") as file:
        list = ReadWord(file)
        for item in list:
            s = "".join(item)
            if '\r' in s:
                s = s.replace('\r','')
            bot_brain.append(s) 
except FileNotFoundError:
    print("That file was not found")


#xu ly du lieu
bot_brain.sort()


#game
print("------TRO CHOI NOI TU------")
is_winner = False
second_turn = False


while is_winner == False:
    #Luot dau tien random
    if second_turn == False:
        ran = random.randrange(len(bot_brain))
        ans = bot_brain[ran]
        bot_brain.remove(ans)
        processed_ans = HandleInputTail(ans)
        print("Luot cua bot:",ans)

    #Luot nguoi choi
    inp = input("Luot cua ban (Nhap 0 de bo cuoc, hay chac rang tu ban viet la dung): ")
    if inp == "0":
        print("Ban da bo cuoc")
        break
    processed_inp_tail = HandleInputTail(inp)
    processed_inp_head = HandleInputHead(inp)

    #kiem tra xem nguoi choi co input dung ko
    if processed_ans != processed_inp_head and second_turn == True:
        print("Ban chon tu khong trung khop. Ban da thua!")
        break

    #bot xu ly
    print("Bot is thinking...")
    time.sleep(1)
    ans = BinarySearch(bot_brain,processed_inp_tail)
    if ans == '0':
        print("BOT khong nghi ra. Ban da thang!!")
        is_winner = True
    else:
        print("Luot cua bot:",ans)
        processed_ans = HandleInputTail(ans)
        bot_brain.remove(ans)
        second_turn = True