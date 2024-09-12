import random
version = int(input('Здравствуй, игрок! Выбери режим игры:\n1 - два игрока\n2 - легкая игра с компьютером\n3 - усложненная игра с компьютером\n'))
p=0
if version ==1:
    player1=input("Введи имя первого игрока:\n")
    player2=input("Введи имя второго игрока:\n")
    hp1=50
    hp2=50
    while p!=1:
        f1= [1,1,1,1,1,1,1,1,1,1]
        f2= [2,2,2,2,2,2,2,2,2,0]
        f3= [3,3,3,3,3,3,3,3,0,0]
        f4= [4,4,4,4,4,4,4,0,0,0]
        f5= [5,5,5,5,5,5,0,0,0,0]
        f6= [6,6,6,6,6,0,0,0,0,0]
        f7= [7,7,7,7,0,0,0,0,0,0]
        f8= [8,8,8,0,0,0,0,0,0,0]
        f9= [9,9,0,0,0,0,0,0,0,0]
        force = int(input(player1+', выбери, с какой силой хочешь атаковать противника!\n'))
        if force==1:
            push = random.choice(f1)
        elif force==2:
            push = random.choice(f2)
        elif force==3:
            push = random.choice(f3)
        elif force==4:
            push = random.choice(f4)
        elif force==5:
            push = random.choice(f5)
        elif force==6:
            push = random.choice(f6)
        elif force==7:
            push = random.choice(f7)
        elif force==8:
            push = random.choice(f8)
        else:
            push = random.choice(f9)
        if push!=0:
            hp2-=push
            print(player1+' атакует '+ player2+ ' с силой '+ str(push)+'. У игрока '+player2+" осталось здоровья: "+ str(hp2)+'\n')
            
        else:
            print('Неудачная атака!\n')

        force = int(input(player2+', выбери, с какой силой хочешь атаковать противника!\n'))
        if force==1:
            push = random.choice(f1)
        elif force==2:
            push = random.choice(f2)
        elif force==3:
            push = random.choice(f3)
        elif force==4:
            push = random.choice(f4)
        elif force==5:
            push = random.choice(f5)
        elif force==6:
            push = random.choice(f6)
        elif force==7:
            push = random.choice(f7)
        elif force==8:
            push = random.choice(f8)
        else:
            push = random.choice(f9)
        if push!=0:
            hp1-=push
            print(player2+' атакует игрока '+ player1+ ' с силой '+ str(push)+'. У игрока '+player1+" осталось здоровья: "+ str(hp1)+"\n")  
        else:
            print('Неудачная атака!\n')
        if hp1<=0:
            p=1
            print('Вот это игра! Победу одерживает '+player2)
            break
        if hp2<=0:
            p=1
            print('Вот это игра! Победу одерживает '+player1)
            break
if version==2:
    player=input("Введи имя:\n")
    hp1=50
    hp2=50
    while p!=1:
        f1= [1,1,1,1,1,1,1,1,1,1]
        f2= [2,2,2,2,2,2,2,2,2,0]
        f3= [3,3,3,3,3,3,3,3,0,0]
        f4= [4,4,4,4,4,4,4,0,0,0]
        f5= [5,5,5,5,5,5,0,0,0,0]
        f6= [6,6,6,6,6,0,0,0,0,0]
        f7= [7,7,7,7,0,0,0,0,0,0]
        f8= [8,8,8,0,0,0,0,0,0,0]
        f9= [9,9,0,0,0,0,0,0,0,0]
        force = int(input(player+', выбери, с какой силой хочешь атаковать противника!\n'))
        if force==1:
            push = random.choice(f1)
        elif force==2:
            push = random.choice(f2)
        elif force==3:
            push = random.choice(f3)
        elif force==4:
            push = random.choice(f4)
        elif force==5:
            push = random.choice(f5)
        elif force==6:
            push = random.choice(f6)
        elif force==7:
            push = random.choice(f7)
        elif force==8:
            push = random.choice(f8)
        else:
            push = random.choice(f9)
        if push!=0:
            hp2-=push
            print(player+' атакует противника с силой '+ str(push)+". У соперника осталось здоровья: "+ str(hp2)+ '\n')
            
        else:
            print('Неудачная атака!\n')

        force = random.choice([int(i) for i in range(1,10)])
        if force==1:
            push = random.choice(f1)
        elif force==2:
            push = random.choice(f2)
        elif force==3:
            push = random.choice(f3)
        elif force==4:
            push = random.choice(f4)
        elif force==5:
            push = random.choice(f5)
        elif force==6:
            push = random.choice(f6)
        elif force==7:
            push = random.choice(f7)
        elif force==8:
            push = random.choice(f8)
        else:
            push = random.choice(f9)
        if push!=0:
            hp1-=push
            print('Компьютер атакует вас с силой '+ str(push)+'. У вас осталось здоровья: '+ str(hp1)+"\n")  
        else:
            print('Неудачная атака!\n')
        if hp1<=0:
            p=1
            print('Вот это игра! Победу одерживает компьютер')
            break
        if hp2<=0:
            p=1
            print('Вот это игра! Победу одерживает '+player)
            break
if version==3:
    step=0
    player=input("Введи имя:\n")
    hp1=50
    hp2=50
    while p!=1:
        f1= [1,1,1,1,1,1,1,1,1,1]
        f2= [2,2,2,2,2,2,2,2,2,0]
        f3= [3,3,3,3,3,3,3,3,0,0]
        f4= [4,4,4,4,4,4,4,0,0,0]
        f5= [5,5,5,5,5,5,0,0,0,0]
        f6= [6,6,6,6,6,0,0,0,0,0]
        f7= [7,7,7,7,0,0,0,0,0,0]
        f8= [8,8,8,0,0,0,0,0,0,0]
        f9= [9,9,0,0,0,0,0,0,0,0]
        force = int(input(player+', выбери, с какой силой хочешь атаковать противника!\n'))
        if force==1:
            push = random.choice(f1)
        elif force==2:
            push = random.choice(f2)
        elif force==3:
            push = random.choice(f3)
        elif force==4:
            push = random.choice(f4)
        elif force==5:
            push = random.choice(f5)
        elif force==6:
            push = random.choice(f6)
        elif force==7:
            push = random.choice(f7)
        elif force==8:
            push = random.choice(f8)
        else:
            push = random.choice(f9)
        if push!=0:
            hp2-=push
            print(player+' атакует противника с силой '+ str(push)+". У соперника осталось здоровья: "+ str(hp2)+ '\n')
            
        else:
            print('Неудачная атака!\n')
            
        #computers step
        if step<=5:
            force = random.choice([int(i) for i in range(4,7)])
            if force==4:
                push = random.choice(f4)
            elif force==5:
                push = random.choice(f5)
            elif force==6:
                push = random.choice(f6)
            else:
                push = random.choice(f7)
        if hp2-hp1>=20 and step>5:
            force = random.choice([int(i) for i in range(8,9)])
            if force==4:
                push = random.choice(f8)
            else:
                push = random.choice(f9)
        if hp2<=15:
            force = random.choice([int(i) for i in range(1,3)])
            if force==1:
                push = random.choice(f1)
            elif force==2:
                push = random.choice(f2)
            else:
                push=rendom.choice(f3)
            
            
        if push!=0:
            hp1-=push
            print('Компьютер атакует вас с силой '+ str(push)+'. У вас осталось здоровья: '+ str(hp1)+"\n")  
        else:
            print('Неудачная атака!\n')
        if hp1<=0:
            p=1
            print('Вот это игра! Победу одерживает компьютер')
            break
        if hp2<=0:
            p=1
            print('Вот это игра! Победу одерживает '+player)
            break
        
        
    