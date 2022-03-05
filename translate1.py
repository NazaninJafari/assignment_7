import os

words=[]

def show_menu():
    print("  Menu  ")
    print("1.Add new word")
    print("2.Translation english to persian")
    print("3.Translation persian to english")
    print("4.Show list")
    print("5.Exit")

def dic_list():
    n_fil = open('database.txt','r')
    row = n_fil.read().split('\n')
    p=0
    t=1
    while t<=len(row):
        words.append({'english':row[p] , 'persian': row[t] })
        p+=2
        t+=2

def add_word():
    x1= input("Add new english word: ")
       
    for i in range(len(words)):
        if x1==words[i]['english']:
            x1=input("this is repetitive! enter a new word: ")
        elif i==len(words)-1:  
            x2= input("Add translate: ")   
            words.append({'english': x1 , 'persian': x2})
            print("your word added!")
            save_word()

def save_word():
    f=open('database.txt','w')
    for i in range(len(words)):
        f.write(words[i]['english'] +'\n'+ words[i]['persian'] +'\n')
    f.close()

def show_dic():
    for i in range(len(words)):
        print(words[i])

def eng_to_per():

    b=[]
    str_e = input("enter your sentence:")
    
    list1=str_e.split('.')

    for i in range(len(list1)):
        a=list1[i].split(' ')
        for i in range(len(a)):
            for j in range(len(words)):
                if a[i]==words[j]['english']:
                    b.append(words[j]['persian'])
                    break    
                elif a[i]!=words[j]['english'] and j==len(words)-1 : 
                    print(CRED + a[i] +' there is not in file'+ CEND)
    print('translating to persian...')
    for i in range(len(b)):
        print(b[i], end=' ')
    print()

def per_to_eng():

    b=[]
    str_e = input("enter your sentence:")
    
    list1=str_e.split('.')

    for i in range(len(list1)):
        a=list1[i].split(' ')
        for i in range(len(a)):
            for j in range(len(words)):
                if a[i]==words[j]['persian']:
                    b.append(words[j]['english'])
                    break    
                elif a[i]!=words[j]['persian'] and j==len(words)-1 : 
                    print(CRED + a[i] +' there is not in file'+ CEND)
    print('translating to english...')
    for i in range(len(b)):
        print(b[i], end=' ')
    print()

dic_list()

CEND='\033[0m'
CRED='\033[91m'

while True:
    show_menu()
    x=int(input("Enter your choice: "))

    if x==1:
        add_word()

    elif x==2:
        eng_to_per()

    elif x==3:
        per_to_eng()

    elif x==4:
        show_dic()

    elif x==5:
        exit()