def lb():
    try:
        with open ('rbalance.txt', 'r') as file:
            return float(file.read())
    except FileNotFoundError:
        return 500
def sb(rbalance):
    with open('rbalance.txt', 'w') as file:
        file.write(str(rbalance))
spin = 0
cb = lb()
action = 1
print('Welcome to Roulette! Please answer yes or no to questions of that nature, and please answer multiple choice questions exactly\n')
rules = input('Would you like to know the rules?\n')
if rules.lower() == 'yes':
    print('Roulette is a game where a random number, from 0-36 is spun.')
    print('You have the option to bet on numbers, sections, or colours.')
    print('18 of the 37 numbers are red, the other 18 are black, and 0 is green.')
    print('You on a singular number, two numbers, three numbers, four numbers, 6 numbers, 12 number, or 18.')
    print('You can also bet on columns, which would include 12 numbers.')
    print("In case you haven't noticed, 0 is a number to balance the odds more in the house's favour.")
    print('This is more of a luck based game, so good luck!\n')
import random
p = True
bettypex = 0
while p == True:
    if action == 1:
        play = input('Would you like to play?\n')
        if play.lower() == 'yes':
            action = 2
        elif play.lower() == 'no':
            p = False
        else:
            print('Your answer must be in the form of yes or no')


    if action == 2:
        if bettypex != 1:
            print('Here are the 2 types of bets:')
            print('1: Number specific - single number, 2 way, 4 way, 6 way')
            print('2: Sectional - rows, columns, in thirds, high/low odd/even, red/black\n')
            bettypex += 1
        action = 3

    if action == 3:
        allbettypes = False
        Rows = False
        Columns = False
        Thirds = False
        OddEven  = False
        Colours = False
        HighLow = False
        betsection = int(input('How many types of bets would you like to make? (max 2) \n'))
        if betsection == 1:
            bettype = input('What type of bet would you like to make? Number or Sectional?\n')
            if bettype.lower() == 'sectional':
                action = 4
            elif bettype.lower() == 'number':
                action = 5
            else:
                print('Your answer must be sectional or number')
        elif betsection == 2:
            allbettypes = True
            action = 4
        else:
            print('Your answer must be 1 or 2')


    if action == 4:
        print('You are on the sectional bet type')
        sectionalpayout = input('Would you like to know the payouts for the different sections?\n')
        if sectionalpayout.lower() == 'yes':
            print('Rows: 12:1, Columns and Thirds: 3:1, Odd/Even, Red/Black, and High/Low: 2:1')
        sectionalbettype = int(input('How many bet types would you like to make here? (max 6)\n'))
        if sectionalbettype > 0 and sectionalbettype <= 6:
            sectionalbettypecounter = 0
            action = 41
        else:
            print('Your answer must be in a range from 1-6')

    if action == 41:
        while sectionalbettypecounter != sectionalbettype:
            sectionalbetquestion = input(" Which bet would you like to make? Rows, Columns, Thirds, Odd/Even, Red/Black, or High/Low?\n")
            sectionalbettypecounter += 1
            if sectionalbetquestion.lower() == 'rows':
                if Rows == True:
                    print('You already made a bet here')
                    sectionalbettypecounter -= 1
                else:
                    Row1 = False
                    Row2 = False
                    Row3 = False
                    Row4 = False
                    Row5 = False
                    Row6 = False
                    Row7 = False
                    Row8 = False
                    Row9 = False
                    Row10 = False
                    Row11 = False
                    Row12 = False
                    Row13 = False
                    Rowbet = 0
                    Rowstype = input('On which row would you like to make your bet on?\n'
                                     '0-2, 1-3, 4-6, 7-9, 10-12, 13-15, 16-18, 19-21, 22-24, 25-27, 28-30, 31-33, or 34-36\n')
                    if Rowstype == '0-2':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row1 = True
                        print('Your bet has been placed')

                    if Rowstype == '1-3':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row2 = True
                        print('Your bet has been placed')

                    if Rowstype == '4-6':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row3 = True
                        print('Your bet has been placed')

                    if Rowstype == '7-9':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row4 = True
                        print('Your bet has been placed')

                    if Rowstype == '10-12':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row5 = True
                        print('Your bet has been placed')

                    if Rowstype == '13-15':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row6 = True
                        print('Your bet has been placed')

                    if Rowstype == '16-18':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row7 = True
                        print('Your bet has been placed')

                    if Rowstype == '19-21':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row8 = True
                        print('Your bet has been placed')

                    if Rowstype == '22-24':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row9 = True
                        print('Your bet has been placed')

                    if Rowstype == '25-27':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row10 = True
                        print('Your bet has been placed')

                    if Rowstype == '28-30':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row11 = True
                        print('Your bet has been placed')

                    if Rowstype == '31-33':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row12 = True
                        print('Your bet has been placed')

                    if Rowstype == '34-36':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row13 = True
                        print('Your bet has been placed')

                    if Rowstype != '0-2' and '1-3' and '4-6' and '7-9' and '10-12' and '13-15' and '16-18' and '19-21' and '22-24' and '25-27' and '28-30' and '31-33' and '34-36':
                        print('Your answer must be from the options of 0-2, 1-3, 4-6, 7-9, 10-12, 13-15, 16-18, 19-21, 22-24, 25-27, 28-30, 31-33, or 34-36 ')
                        sectionalbettypecounter -= 1


            if sectionalbetquestion.lower() == 'columns':
                if Columns == True:
                    print('You already made a bet here')
                    sectionalbettypecounter -= 1
                else:
                    column1 = False
                    column2 = False
                    column3 = False
                    columnbet = 0
                    columntype = input('On what column would you like to make a bet on?\n'
                                       'Column 1: (1,4,7,10,13,16,19,22,25,28,31,34) Column 2: (2,5,8,11,14,17,20,23,26,29,32,35) Column 3: (3,6,9,12,15,18,21,24,27,30,33,36)\n'
                                       'Please answer with 1, 2, or 3\n')
                    if columntype == '1':
                        columnbet = int(input('How much would you like to bet?\n'))
                        Columns = True
                        column1 = True
                        print('Your bet has been placed')

                    if columntype == '2':
                        columnbet = int(input('How much would you like to bet?\n'))
                        Columns = True
                        column2 = True
                        print('Your bet has been placed')

                    if columntype == '3':
                        columnbet = int(input('How much would you like to bet?\n'))
                        Columns = True
                        column3 = True
                        print('Your bet has been placed')

                    if columntype != '1' and '2' and '3':
                        print('Your answer must be a 1,2, or 3.')
                        sectionalbettypecounter -= 1


            if sectionalbetquestion.lower() == 'thirds':
                if Thirds == True:
                    print('You already made a bet here')
                    sectionalbettypecounter -= 1
                else:
                    Third1 = False
                    Third2 = False
                    Third3 = False
                    Thirdbet = 0
                    Thirdtype = input('Which third would you like to make a bet on? 1-12, 13-24, or 25-36?\n')
                    if Thirdtype == '1-12':
                        Thirdbet = int(input('How much would you like to bet\n'))
                        Thirds = True
                        Third1 = True
                        print('Your bet has been placed')
                    if Thirdtype == '13-24':
                        Thirdbet = int(input('How much would you like to bet\n'))
                        Thirds = True
                        Third2 = True
                        print('Your bet has been placed')
                    if Thirdtype == '25-36':
                        Thirdbet = int(input('How much would you like to bet\n'))
                        Thirds = True
                        Third3 = True
                        print('Your bet has been placed')
                    if Thirdtype != '1-12' and '13-24' and '25-36':
                        print('Your answer must be either 1-12, 13-24, or 25-36.')
                        sectionalbettypecounter -= 1


            if sectionalbetquestion.lower() == 'odd/even':
                if OddEven == True:
                    print('You already made a bet here')
                    sectionalbettypecounter -= 1
                else:
                    Odd = False
                    Even = False
                    OddEvenbet = 0
                    OddEventype = input('Would you like to bet on odd or even? 0 is not included.\n')
                    if OddEventype.lower() == 'odd':
                        OddEvenbet = int(input('How much would you like to bet?\n'))
                        OddEven = True
                        Odd = True
                        print('Your bet has been placed')
                    if OddEventype.lower() == 'even':
                        OddEvenbet = int(input('How much would you like to bet?\n'))
                        OddEven = True
                        Even = True
                        print('Your bet has been placed')
                    if OddEventype.lower() != 'odd' and 'even':
                        print('Your answer must be odd or even.')
                        sectionalbettypecounter -= 1


            if sectionalbetquestion.lower() == 'red/black':
                if Colours == True:
                    print('You already made a bet here')
                    sectionalbettypecounter -= 1
                else:
                    Red = False
                    Black = False
                    Colourbet = 0
                    Colourtype = input('Would you like to bet on red or black?\n'
                                       'Red numbers are: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, and 36.\n'
                                       'Black numbers are 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, and 35.\n')
                    if Colourtype.lower() == 'red':
                        Colourbet = int(input('How much would you like to bet?\n'))
                        Colours = True
                        Red = True
                        print('Your bet has been placed')
                    if Colourtype.lower() == 'black':
                        Colourbet = int(input('How much would you like to bet?\n'))
                        Colours = True
                        Black = True
                        print('Your bet has been placed')
                    if Colourtype.lower() != 'red' and 'black':
                        print('Your answer must be red or black.')
                        sectionalbettypecounter -= 1

