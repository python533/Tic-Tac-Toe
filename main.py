import os
import time

tahta=['','','','','','','','','','']


player=1

Win=1

Draw=-1

Running=0

Stop=1

Game=Running

Mark='X'

def drawboard():
    print("%c|%c|%c"% tahta[1],tahta[2],tahta[3])
    print("___|___|___")
    print("%c|%c|%c" % tahta[4], tahta[5], tahta[6])
    print("___|___|___")
    print("%c|%c|%c" % tahta[7], tahta[8], tahta[9])
    print("||")

def checkpos():
    if tahta[Mark] == '':
        return True
    else:
        False



def checkwin():
    global Game
    y=1
    while(y < 10):
        if tahta[1] == tahta[2] and tahta[2] ==tahta[3] and tahta[1] != '':
            Game = Win

        elif tahta[4] == tahta[5] and tahta[5] == tahta[6] and tahta[4] != '':
            Game = Win

        elif tahta[7] == tahta[8] and tahta[9] == tahta[3] and tahta[7] != '':
            Game = Win

        elif tahta[1] == tahta[4] and tahta[4] == tahta[7] and tahta[1] != '':
            Game = Win

        elif tahta[2] == tahta[5] and tahta[5] == tahta[8] and tahta[2] != '':
            Game = Win

        elif tahta[3] == tahta[6] and tahta[6] == tahta[9] and tahta[3] != '':
            Game = Win

        elif tahta[1] == tahta[5] and tahta[5] == tahta[9] and tahta[5] != '':
            Game = Win

        elif tahta[3] == tahta[5] and tahta[5] == tahta[7] and tahta[5] != '':
            Game = Win

        elif [1] !='' and tahta[2] != ''[3] !='' and \
            [2] != '' and tahta[3] != ''[4] != '' and \
            [5] != '' and tahta[6] != ''[7] != '' and \
            [7] != '' and tahta[8] != ''[9] != '':
            Game = Draw

        else:
            Game = Running

        print("Tic Tac Toe Game By Cihan Senatak")
        print("Player 1 [X] ---- Player2 [O]\n")
        print()
        print()
        print("Lütfen Bekleyin")
        time.sleep(3)

        while Game == Running:
            global Player
            os.system('cls')
            drawboard()

            if Player % 2 !=0:
                print('Birinci Oyuncu Şansı')
                Mark = 'X'

            else:
                print('İkinci Oyunucu Şansı')
                Mark = 'O'


            Konumsec=int(input("1 ile 9 arası bir rakam Belirtin?"))

            if checkpos(Konumsec):
                tahta[Konumsec] = Mark
                Player +=1
                checkwin()

            os.system('cls')
            drawboard()

            if Game == Draw :
                print("Oyun Berabere")

            elif Game == Win:
                Player -=1
                if Player %2 != 0:
                    print("Player 1 Won")
                else:
                    print("Player 2 Won")























