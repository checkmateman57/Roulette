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
currentbalance = lb()
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
        Single = False
        Double = False
        FourWay = False
        SixWay = False
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
        if sectionalbettypecounter < sectionalbettype:
            sectionalbetquestion = input(" Which bet would you like to make? Rows, Columns, Thirds, Odd/Even, Red/Black, or High/Low?\n")
            if sectionalbetquestion.lower() == 'rows':
                if Rows == True:
                    print('You already made a bet here')
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
                        sectionalbettypecounter += 1
                    elif Rowstype == '1-3':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row2 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '4-6':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row3 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '7-9':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row4 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '10-12':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row5 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '13-15':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row6 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '16-18':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row7 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '19-21':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row8 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '22-24':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row9 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '25-27':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row10 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '28-30':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row11 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '31-33':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row12 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '34-36':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row13 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    else:
                        print('Your answer must be from the options of 0-2, 1-3, 4-6, 7-9, 10-12, 13-15, 16-18, 19-21, 22-24, 25-27, 28-30, 31-33, or 34-36 ')


            elif sectionalbetquestion.lower() == 'columns':
                if Columns == True:
                    print('You already made a bet here')
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
                        sectionalbettypecounter += 1
                    elif columntype == '2':
                        columnbet = int(input('How much would you like to bet?\n'))
                        Columns = True
                        column2 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif columntype == '3':
                        columnbet = int(input('How much would you like to bet?\n'))
                        Columns = True
                        column3 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    else:
                        print('Your answer must be a 1,2, or 3.')


            elif sectionalbetquestion.lower() == 'thirds':
                if Thirds == True:
                    print('You already made a bet here')
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
                        sectionalbettypecounter += 1
                    elif Thirdtype == '13-24':
                        Thirdbet = int(input('How much would you like to bet\n'))
                        Thirds = True
                        Third2 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Thirdtype == '25-36':
                        Thirdbet = int(input('How much would you like to bet\n'))
                        Thirds = True
                        Third3 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    else:
                        print('Your answer must be either 1-12, 13-24, or 25-36.')


            elif sectionalbetquestion.lower() == 'odd/even':
                if OddEven == True:
                    print('You already made a bet here')
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
                        sectionalbettypecounter += 1
                    elif OddEventype.lower() == 'even':
                        OddEvenbet = int(input('How much would you like to bet?\n'))
                        OddEven = True
                        Even = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    else:
                        print('Your answer must be odd or even.')


            elif sectionalbetquestion.lower() == 'red/black':
                if Colours == True:
                    print('You already made a bet here')
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
                        sectionalbettypecounter += 1
                    elif Colourtype.lower() == 'black':
                        Colourbet = int(input('How much would you like to bet?\n'))
                        Colours = True
                        Black = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    else:
                        print('Your answer must be red or black.')


            elif sectionalbetquestion.lower() == 'high/low':
                if HighLow == True:
                    print('You already made a bet here')
                else:
                    High = False
                    Low = False
                    HighLowbet = 0
                    HighLowtype = input('Would you like to bet on Low or High? Low is 1-18, High is 19-36\n')
                    if HighLowtype.lower() == 'low':
                        HighLowbet = int(input('How much would you like to bet?\n'))
                        HighLow = True
                        Low = True
                        sectionalbettypecounter += 1
                        print('Your bet has been placed')
                    elif HighLowtype.lower() == 'high':
                        HighLowbet = int(input('How much would you like to bet?\n'))
                        HighLow = True
                        High = True
                        sectionalbettypecounter += 1
                        print('Your bet has been placed')
                    else:
                        print('Your answer must be low or high.')


            else:
                print('Your answer must be one of the following: Rows, Columns, Thirds, Odd/Even, Red/Black, or High/Low')

        if sectionalbettypecounter == sectionalbettype:
            if allbettypes == True:
                action = 5
            else:
                action = 6


    if action == 5:
        print('You are on the number type bet')
        numberpayout = input('Would you like to know the payouts for the different types of number bets?\n')
        if numberpayout.lower() == 'yes':
            print('Single number: 36:1, 2 way split: 18:1, 4 way corner: 9:1, 6 way double row: 6:1')
        numberbettype = int(input('How many bet types would you like to make here? (max 4)\n'))
        if numberbettype > 0 and numberbettype <= 4:
            numberbettypecounter = 0
            action = 51
        else:
            print('Your answer must be in a range from 1-4')

    if action == 51:
        if numberbettypecounter < numberbettype:
            numberbetquestion = input('Which bet would you like to make? Single, 2 Way, 4 Way, or 6 Way?\n')
            if numberbetquestion.lower() == 'single':
                if Single == True:
                    print('You already made a bet here')
                else:
                    Single0 = False
                    Single1 = False
                    Single2 = False
                    Single3 = False
                    Single4 = False
                    Single5 = False
                    Single6 = False
                    Single7 = False
                    Single8 = False
                    Single9 = False
                    Single10 = False
                    Single11 = False
                    Single12 = False
                    Single13 = False
                    Single14 = False
                    Single15 = False
                    Single16 = False
                    Single17 = False
                    Single18 = False
                    Single19 = False
                    Single20 = False
                    Single21 = False
                    Single22 = False
                    Single23 = False
                    Single24 = False
                    Single25 = False
                    Single26 = False
                    Single27 = False
                    Single28 = False
                    Single29 = False
                    Single30 = False
                    Single31 = False
                    Single32 = False
                    Single33 = False
                    Single34 = False
                    Single35 = False
                    Single36 = False
                    Singlebet = 0
                    Singletype = input('From 0-36, on which number would you like to place a bet on?\n')
                    if Singletype == '0':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single0 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '1':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single1 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '2':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single2 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '3':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single3 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '4':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single4 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '5':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single5 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '6':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single6 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '7':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single7 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '8':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single8 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '9':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single9 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '10':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single10 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '11':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single11 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '12':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single12 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '13':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single13 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '14':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single14 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '15':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single15 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '16':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single16 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '17':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single17 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '18':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single18 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '19':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single19 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '20':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single20 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '21':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single21 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '22':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single22 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '23':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single23 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '24':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single24 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '25':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single25 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '26':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single26 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '27':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single27 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '28':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single28 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '29':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single29 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '30':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single30 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '31':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single31 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '32':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single32 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '33':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single33 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '34':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single34 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '35':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single35 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    elif Singletype == '36':
                        Singlebet = int(input('How much would you like to bet\n'))
                        Single = True
                        Single36 = True
                        print('Your bet has been placed')
                        numberbettypecounter += 1
                    else:
                        print('Your answer must be a number from 0-36')


            if numberbetquestion.lower() == '2 way':
                if Double == True:
                    print('You already made a bet here')
                else:
                    Vertical1 = False
                    Vertical2 = False
                    Vertical3 = False
                    Vertical4 = False
                    Vertical5 = False
                    Vertical6 = False
                    Vertical7 = False
                    Vertical8 = False
                    Vertical9 = False
                    Vertical10 = False
                    Vertical11 = False
                    Vertical12 = False
                    Vertical13 = False
                    Vertical14 = False
                    Vertical15 = False
                    Vertical16 = False
                    Vertical17 = False
                    Vertical18 = False
                    Vertical19 = False
                    Vertical20 = False
                    Vertical21 = False
                    Vertical22 = False
                    Vertical23 = False
                    Vertical24 = False
                    Vertical25 = False
                    Vertical26 = False
                    Vertical27 = False
                    Vertical28 = False
                    Vertical29 = False
                    Vertical30 = False
                    Vertical31 = False
                    Vertical32 = False
                    Vertical33 = False
                    Vertical34 = False
                    Vertical35 = False
                    Vertical36 = False
                    Horizontal1 = False
                    Horizontal2 = False
                    Horizontal3 = False
                    Horizontal4 = False
                    Horizontal5 = False
                    Horizontal6 = False
                    Horizontal7 = False
                    Horizontal8 = False
                    Horizontal9 = False
                    Horizontal10 = False
                    Horizontal11 = False
                    Horizontal12 = False
                    Horizontal13 = False
                    Horizontal14 = False
                    Horizontal15 = False
                    Horizontal16 = False
                    Horizontal17 = False
                    Horizontal18 = False
                    Horizontal19 = False
                    Horizontal20 = False
                    Horizontal21 = False
                    Horizontal22 = False
                    Horizontal23 = False
                    Horizontal24 = False
                    Doublebet = 0
                    Doubletype = input('Is your 2 way bet vertical or horizontal?\n')
                    if Doubletype.lower() == 'vertical':
                        DoubleVertical = input('On which 2 way would you like to make a bet on?\n'
                                               '0&1, 0&2, 0&3, 1&4, 2&5, 3&6, 4&7, 5&8, 6&9, 7&10, 8&11, 9&12, 10&13, 11&14, 12&15, 13&16, 14&17, 15&18, 16&19, 17&20, 18&21\n'
                                               '19&22, 20&23, 21&24, 22&25, 23&26, 24&27, 25&28, 26&29, 27&30, 28&31, 29&32, 30&33, 31&34, 32&35, 33&36\n')
                        if DoubleVertical == '0&1':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical1 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '0&2':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical2 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '0&3':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical3 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '1&4':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical4 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '2&5':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical5 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '3&6':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical6 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '4&7':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical7 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '5&8':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical8 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '6&9':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical9 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '7&10':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical10 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '8&11':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical11 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '9&12':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical12 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '10&13':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical13 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '11&14':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical14 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '12&15':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical15 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '13&16':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical16 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '14&17':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical17 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '15&18':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical18 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '16&19':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical19 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '17&20':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical20 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '18&21':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical21 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '19&22':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical22 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '20&23':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical23 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '21&24':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical24 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '22&25':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical25 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '23&26':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical26 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '24&27':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical27 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '25&28':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical28 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '26&29':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical29 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '27&30':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical30 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '28&31':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical31 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '29&32':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical32 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '30&33':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical33 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '31&34':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical34 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '32&35':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical35 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleVertical == '33&36':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Vertical36 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        else:
                            print('Your answer must be from the following:')
                            print('0&1, 0&2, 0&3, 1&4, 2&5, 3&6, 4&7, 5&8, 6&9, 7&10, 8&11, 9&12, 10&13, 11&14, 12&15, 13&16, 14&17, 15&18, 16&19, 17&20, 18&21')
                            print('19&22, 20&23, 21&24, 22&25, 23&26, 24&27, 25&28, 26&29, 27&30, 28&31, 29&32, 30&33, 31&34, 32&35, 33&36')

                    elif Doubletype.lower() == 'horizontal':
                        DoubleHorizontal = input('On which 2 way would you like to bet on?\n'
                                                 '1&2, 2&3, 4&5, 5&6, 7&8, 8&9, 10&11, 11&12, 13&14, 14&15, 16&17, 17&18, 19&20, 20&21\n'
                                                 '22&23, 23&24, 25&26, 26&27, 28&29, 29&30, 31&32, 32&33, 34&35, 35&36\n')
                        if DoubleHorizontal == '1&2':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal1 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '2&3':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal2 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '4&5':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal3 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '5&6':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal4 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '7&8':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal5 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '8&9':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal6 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '10&11':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal7 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '11&12':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal8 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '13&14':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal9 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '14&15':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal10 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '16&17':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal11 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '17&18':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal12 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '19&20':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal13 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '20&21':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal14 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '22&23':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal15 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '23&24':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal16 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '25&26':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal17 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '26&27':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal18 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '28&29':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal19 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '29&30':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal20 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '31&32':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal21 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '32&33':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal22 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '34&35':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal23 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        elif DoubleHorizontal == '35&36':
                            Doublebet = int(input('How much would you like to bet?\n'))
                            Double = True
                            Horizontal24 = True
                            print('Your bet has been placed')
                            numberbettypecounter += 1
                        else:
                            print('Your answer must be from:')
                            print('1&2, 2&3, 4&5, 5&6, 7&8, 8&9, 10&11, 11&12, 13&14, 14&15, 16&17, 17&18, 19&20, 20&21')
                            print('22&23, 23&24, 25&26, 26&27, 28&29, 29&30, 31&32, 32&33, 34&35, 35&36')

                    else:
                        print('Your answer must be vertical or horizontal')

            if numberbetquestion.lower() == '4 way':
                if FourWay == True:
                    print('You already made a bet here.')
                else:
                    FourWay1 = False
                    FourWay2 = False
                    FourWay3 = False
                    FourWay4 = False
                    FourWay5 = False
                    FourWay6 = False
                    FourWay7 = False
                    FourWay8 = False
                    FourWay9 = False
                    FourWay10 = False
                    FourWay11 = False
                    FourWay12 = False
                    FourWay13 = False
                    FourWay14 = False
                    FourWay15 = False
                    FourWay16 = False
                    FourWay17 = False
                    FourWay18 = False
                    FourWay19 = False
                    FourWay20 = False
                    FourWay21 = False
                    FourWay22 = False
                    FourWaybet = 0
                    Fourbettype = input('Where would you like to make a bet? Your options are:\n'
                                        '1,2,4,5    2,3,5,6    4,5,7,8    5,6,8,9    7,8,10,11    8,9,11,12    10,11,13,14    11,12,14,15    13,14,16,17    14,15,17,18   16,17,19,20    17,18,20,21\n'
                                        '19,20,22,23    20,21,23,24    22,23,25,26    23,24,26,27    25,26,28,29    26,27,29,30    28,29,31,32    29,30,32,33    31,32,34,35    32,33,35,36\n')
                    if Fourbettype == '1,2,4,5':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay1 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '2,3,5,6':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay2 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '4,5,7,8':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay3 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '5,6,8,9':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay4 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '7,8,10,11':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay5 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '8,9,11,12':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay6 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '10,11,13,14':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay7 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '11,12,14,15':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay8 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '13,14,16,17':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay9 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '14,15,17,18':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay10 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '16,17,19,20':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay11 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '17,18,20,21':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay12 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '19,20,22,23':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay13 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '20,21,23,24':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay14 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '22,23,25,26':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay15 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '23,24,26,27':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay16 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '25,26,28,29':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay17 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '26,27,29,30':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay18 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '28,29,31,32':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay19 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '29,30,32,33':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay20 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '31,32,34,35':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay21 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif Fourbettype == '32,33,35,36':
                        FourWaybet = int(input('How much would you like to bet?'))
                        FourWay = True
                        FourWay22 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    else:
                        print('Your answer must be from:')
                        print('1,2,4,5    2,3,5,6    4,5,7,8    5,6,8,9    7,8,10,11    8,9,11,12    10,11,13,14    11,12,14,15    13,14,16,17    14,15,17,18   16,17,19,20    17,18,20,21')
                        print('19,20,22,23    20,21,23,24    22,23,25,26    23,24,26,27    25,26,28,29    26,27,29,30    28,29,31,32    29,30,32,33    31,32,34,35    32,33,35,36')
