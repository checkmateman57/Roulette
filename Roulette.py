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
                        Row13 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '1-3':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row1 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '4-6':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row2 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '7-9':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row3 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '10-12':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row4 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '13-15':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row5 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '16-18':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row6 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '19-21':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row7 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '22-24':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row8 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '25-27':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row9 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '28-30':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row10 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '31-33':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row11 = True
                        print('Your bet has been placed')
                        sectionalbettypecounter += 1
                    elif Rowstype == '34-36':
                        Rowbet = int(input('How much would you like to bet?\n'))
                        Rows = True
                        Row12 = True
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


            elif numberbetquestion.lower() == '2 way':
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


            elif numberbetquestion.lower() == '4 way':
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


            elif numberbetquestion.lower() == '6 way':
                if SixWay == True:
                    print('You already made a bet here')
                else:
                    SixWay1 = False
                    SixWay2 = False
                    SixWay3 = False
                    SixWay4 = False
                    SixWay5 = False
                    SixWay6 = False
                    SixWay7 = False
                    SixWay8 = False
                    SixWay9 = False
                    SixWay10 = False
                    SixWay11 = False
                    SixWaybet = 0
                    SixWaytype = input('What would you like to bet on? 1-6, 4-9, 7-12, 10-15, 13-18, 16-21, 19-24, 22-27, 25-30, 28-33, 31-36\n')
                    if SixWaytype == '1-6':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay1 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '4-9':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay2 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '7-12':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay3 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '10-15':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay4 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '13-18':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay5 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '16-21':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay6 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '19-24':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay7 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '22-27':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay8 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '25-30':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay9 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '28-33':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay10 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    elif SixWaytype == '31-36':
                        SixWaybet = int(input('How much would you like to bet?\n'))
                        SixWay = True
                        SixWay11 = True
                        print('Your bet has been placed.')
                        numberbettypecounter += 1
                    else:
                        print('Your answer must be from: 1-6, 4-9, 7-12, 10-15, 13-18, 16-21, 19-24, 22-27, 25-30, 28-33, 31-36')


            else:
                print('Your answer must be Single, 2 way, 4 way, or 6 way')

        if numberbettypecounter == numberbettype:
            action = 6

    if action == 6:
        spin = random.randint(0,36)
        if spin == 0:
            print('And the roll is 0, green')
        elif spin in [1,3,5,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            print(f'And the roll is {spin}, red\n')
        else:
            print(f'And the roll is {spin}, black\n')
        action = 7

    if action == 7:
        Row1Checker = False
        Row2Checker = False
        Row3Checker = False
        Row4Checker = False
        Row5Checker = False
        Row6Checker = False
        Row7Checker = False
        Row8Checker = False
        Row9Checker = False
        Row10Checker = False
        Row11Checker = False
        Row12Checker = False
        Row13Checker = False
        column1Checker = False
        column2Checker = False
        column3Checker = False
        Third1Checker = False
        Third2Checker = False
        Third3Checker = False
        RedChecker = False
        BlackChecker = False
        OddChecker = False
        EvenChecker = False
        HighChecker = False
        LowChecker = False
        Single0Checker = False
        Single1Checker = False
        Single2Checker = False
        Single3Checker = False
        Single4Checker = False
        Single5Checker = False
        Single6Checker = False
        Single7Checker = False
        Single8Checker = False
        Single9Checker = False
        Single10Checker = False
        Single11Checker = False
        Single12Checker = False
        Single13Checker = False
        Single14Checker = False
        Single15Checker = False
        Single16Checker = False
        Single17Checker = False
        Single18Checker = False
        Single19Checker = False
        Single20Checker = False
        Single21Checker = False
        Single22Checker = False
        Single23Checker = False
        Single24Checker = False
        Single25Checker = False
        Single26Checker = False
        Single27Checker = False
        Single28Checker = False
        Single29Checker = False
        Single30Checker = False
        Single31Checker = False
        Single32Checker = False
        Single33Checker = False
        Single34Checker = False
        Single35Checker = False
        Single36Checker = False
        Vertical1Checker = False
        Vertical2Checker = False
        Vertical3Checker = False
        Vertical4Checker = False
        Vertical5Checker = False
        Vertical6Checker = False
        Vertical7Checker = False
        Vertical8Checker = False
        Vertical9Checker = False
        Vertical10Checker = False
        Vertical11Checker = False
        Vertical12Checker = False
        Vertical13Checker = False
        Vertical14Checker = False
        Vertical15Checker = False
        Vertical16Checker = False
        Vertical17Checker = False
        Vertical18Checker = False
        Vertical19Checker = False
        Vertical20Checker = False
        Vertical21Checker = False
        Vertical22Checker = False
        Vertical23Checker = False
        Vertical24Checker = False
        Vertical25Checker = False
        Vertical26Checker = False
        Vertical27Checker = False
        Vertical28Checker = False
        Vertical29Checker = False
        Vertical30Checker = False
        Vertical31Checker = False
        Vertical32Checker = False
        Vertical33Checker = False
        Vertical34Checker = False
        Vertical35Checker = False
        Vertical36Checker = False
        Horizontal1Checker = False
        Horizontal2Checker = False
        Horizontal3Checker = False
        Horizontal4Checker = False
        Horizontal5Checker = False
        Horizontal6Checker = False
        Horizontal7Checker = False
        Horizontal8Checker = False
        Horizontal9Checker = False
        Horizontal10Checker = False
        Horizontal11Checker = False
        Horizontal12Checker = False
        Horizontal13Checker = False
        Horizontal14Checker = False
        Horizontal15Checker = False
        Horizontal16Checker = False
        Horizontal17Checker = False
        Horizontal18Checker = False
        Horizontal19Checker = False
        Horizontal20Checker = False
        Horizontal21Checker = False
        Horizontal22Checker = False
        Horizontal23Checker = False
        Horizontal24Checker = False
        FourWay1Checker = False
        FourWay2Checker = False
        FourWay3Checker = False
        FourWay4Checker = False
        FourWay5Checker = False
        FourWay6Checker = False
        FourWay7Checker = False
        FourWay8Checker = False
        FourWay9Checker = False
        FourWay10Checker = False
        FourWay11Checker = False
        FourWay12Checker = False
        FourWay13Checker = False
        FourWay14Checker = False
        FourWay15Checker = False
        FourWay16Checker = False
        FourWay17Checker = False
        FourWay18Checker = False
        FourWay19Checker = False
        FourWay20Checker = False
        FourWay21Checker = False
        FourWay22Checker = False
        SixWay1Checker = False
        SixWay2Checker = False
        SixWay3Checker = False
        SixWay4Checker = False
        SixWay5Checker = False
        SixWay6Checker = False
        SixWay7Checker = False
        SixWay8Checker = False
        SixWay9Checker = False
        SixWay10Checker = False
        SixWay11Checker = False


        if spin == 0:
            Single0Checker = True
            Vertical1Checker = True
            Vertical2Checker = True
            Vertical3Checker = True
            Row13Checker = True
        elif spin == 1:
            Single1Checker = True
            Vertical1Checker = True
            Vertical4Checker = True
            Horizontal1Checker = True
            FourWay1Checker = True
            SixWay1Checker = True
            column1Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row1Checker = True
            Row13Checker = True
            OddChecker = True
        elif spin == 2:
            Single2Checker = True
            Vertical2Checker = True
            Vertical5Checker = True
            Horizontal1Checker = True
            Horizontal2Checker = True
            FourWay1Checker = True
            FourWay2Checker = True
            SixWay1Checker = True
            column2Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row1Checker = True
            Row13Checker = True
            EvenChecker = True
        elif spin == 3:
            Single3Checker = True
            Vertical3Checker = True
            Vertical6Checker = True
            Horizontal2Checker = True
            FourWay2Checker = True
            SixWay1Checker = True
            column3Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row1Checker = True
            OddChecker = True
        elif spin == 4:
            Single4Checker = True
            Vertical4Checker = True
            Vertical7Checker = True
            Horizontal3Checker = True
            FourWay1Checker = True
            FourWay3Checker = True
            SixWay1Checker = True
            SixWay2Checker = True
            column1Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row2Checker = True
            EvenChecker = True
        elif spin == 5:
            Single5Checker = True
            Vertical8Checker = True
            Vertical5Checker = True
            Horizontal3Checker = True
            Horizontal4Checker = True
            FourWay1Checker = True
            FourWay2Checker = True
            FourWay3Checker = True
            FourWay4Checker = True
            SixWay1Checker = True
            SixWay2Checker = True
            column2Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row2Checker = True
            OddChecker = True
        elif spin == 6:
            Single6Checker = True
            Vertical6Checker = True
            Vertical9Checker = True
            Horizontal4Checker = True
            FourWay2Checker = True
            FourWay4Checker = True
            SixWay1Checker = True
            SixWay2Checker = True
            column3Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row2Checker = True
            EvenChecker = True
        elif spin == 7:
            Single7Checker = True
            Vertical7Checker = True
            Vertical10Checker = True
            Horizontal5Checker = True
            FourWay3Checker = True
            FourWay5Checker = True
            SixWay2Checker = True
            SixWay3Checker = True
            column1Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row3Checker = True
            OddChecker = True
        elif spin == 8:
            Single8Checker = True
            Vertical8Checker = True
            Vertical11Checker = True
            Horizontal5Checker = True
            Horizontal6Checker = True
            FourWay3Checker = True
            FourWay4Checker = True
            FourWay5Checker = True
            FourWay6Checker = True
            SixWay2Checker = True
            SixWay3Checker = True
            column2Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row3Checker = True
            EvenChecker = True
        elif spin == 9:
            Single9Checker = True
            Vertical12Checker = True
            Vertical9Checker = True
            Horizontal6Checker = True
            FourWay6Checker = True
            FourWay4Checker = True
            SixWay3Checker = True
            SixWay2Checker = True
            column3Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row3Checker = True
            OddChecker = True
        elif spin == 10:
            Single10Checker = True
            Vertical10Checker = True
            Vertical13Checker = True
            Horizontal7Checker = True
            FourWay7Checker = True
            FourWay5Checker = True
            SixWay3Checker = True
            SixWay4Checker = True
            column1Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row4Checker = True
            EvenChecker = True
        elif spin == 11:
            Single11Checker = True
            Vertical11Checker = True
            Vertical14Checker = True
            Horizontal7Checker = True
            Horizontal8Checker = True
            FourWay5Checker = True
            FourWay6Checker = True
            FourWay7Checker = True
            FourWay8Checker = True
            SixWay3Checker = True
            SixWay4Checker = True
            column2Checker = True
            BlackChecker = True
            Third1Checker = True
            LowChecker = True
            Row4Checker = True
            OddChecker = True
        elif spin == 12:
            Single12Checker = True
            Vertical12Checker = True
            Vertical15Checker = True
            Horizontal8Checker = True
            FourWay6Checker = True
            FourWay8Checker = True
            SixWay3Checker = True
            SixWay4Checker = True
            column3Checker = True
            RedChecker = True
            Third1Checker = True
            LowChecker = True
            Row4Checker = True
            EvenChecker = True
        elif spin == 13:
            Single13Checker = True
            Vertical13Checker = True
            Vertical16Checker = True
            Horizontal9Checker = True
            FourWay7Checker = True
            FourWay9Checker = True
            SixWay4Checker = True
            SixWay5Checker = True
            column1Checker = True
            BlackChecker = True
            Third2Checker = True
            LowChecker = True
            Row5Checker = True
            OddChecker = True
        elif spin == 14:
            Single14Checker = True
            Vertical14Checker = True
            Vertical17Checker = True
            Horizontal9Checker = True
            Horizontal10Checker = True
            FourWay7Checker = True
            FourWay8Checker = True
            FourWay9Checker = True
            FourWay10Checker = True
            SixWay4Checker = True
            SixWay5Checker = True
            column2Checker = True
            RedChecker = True
            Third2Checker = True
            LowChecker = True
            Row5Checker = True
            EvenChecker = True
        elif spin == 15:
            Single15Checker = True
            Vertical15Checker = True
            Vertical18Checker = True
            Horizontal10Checker = True
            FourWay8Checker = True
            FourWay10Checker = True
            SixWay4Checker = True
            SixWay5Checker = True
            column3Checker = True
            BlackChecker = True
            Third2Checker = True
            LowChecker = True
            Row5Checker = True
            OddChecker = True
        elif spin == 16:
            Single16Checker = True
            Vertical16Checker = True
            Vertical19Checker = True
            Horizontal11Checker = True
            FourWay9Checker = True
            FourWay11Checker = True
            SixWay5Checker = True
            SixWay6Checker = True
            column1Checker = True
            RedChecker = True
            Third2Checker = True
            LowChecker = True
            Row6Checker = True
            EvenChecker = True
        elif spin == 17:
            Single17Checker = True
            Vertical17Checker = True
            Vertical20Checker = True
            Horizontal11Checker = True
            Horizontal12Checker = True
            FourWay9Checker = True
            FourWay10Checker = True
            FourWay11Checker = True
            FourWay12Checker = True
            SixWay5Checker = True
            SixWay6Checker = True
            column2Checker = True
            BlackChecker = True
            Third2Checker = True
            LowChecker = True
            Row6Checker = True
            OddChecker = True
        elif spin == 18:
            Single18Checker = True
            Vertical18Checker = True
            Vertical21Checker = True
            Horizontal12Checker = True
            FourWay10Checker = True
            FourWay12Checker = True
            SixWay5Checker = True
            SixWay6Checker = True
            column3Checker = True
            RedChecker = True
            Third2Checker = True
            LowChecker = True
            Row6Checker = True
            EvenChecker = True
        elif spin == 19:
            Single19Checker = True
            Vertical22Checker = True
            Vertical19Checker = True
            Horizontal13Checker = True
            FourWay11Checker = True
            FourWay13Checker = True
            SixWay6Checker = True
            SixWay7Checker = True
            column1Checker = True
            RedChecker = True
            Third2Checker = True
            HighChecker = True
            Row7Checker = True
            OddChecker = True
        elif spin == 20:
            Single20Checker = True
            Vertical20Checker = True
            Vertical23Checker = True
            Horizontal13Checker = True
            Horizontal14Checker = True
            FourWay11Checker = True
            FourWay12Checker = True
            FourWay13Checker = True
            FourWay14Checker = True
            SixWay6Checker = True
            SixWay7Checker = True
            column2Checker = True
            BlackChecker = True
            Third2Checker = True
            HighChecker = True
            Row7Checker = True
            EvenChecker = True
        elif spin == 21:
            Single21Checker = True
            Vertical21Checker = True
            Vertical24Checker = True
            Horizontal14Checker = True
            FourWay12Checker = True
            FourWay14Checker = True
            SixWay6Checker = True
            SixWay7Checker = True
            column3Checker = True
            RedChecker = True
            Third2Checker = True
            HighChecker = True
            Row7Checker = True
            OddChecker = True
        elif spin == 22:
            Single2Checker = True
            Vertical22Checker = True
            Vertical25Checker = True
            Horizontal15Checker = True
            FourWay13Checker = True
            FourWay15Checker = True
            SixWay7Checker = True
            SixWay8Checker = True
            column1Checker = True
            BlackChecker = True
            Third2Checker = True
            HighChecker = True
            Row8Checker = True
            EvenChecker = True
        elif spin == 23:
            Single23Checker = True
            Vertical26Checker = True
            Vertical23Checker = True
            Horizontal15Checker = True
            Horizontal16Checker = True
            FourWay13Checker = True
            FourWay14Checker = True
            FourWay15Checker = True
            FourWay16Checker = True
            SixWay7Checker = True
            SixWay8Checker = True
            column2Checker = True
            RedChecker = True
            Third2Checker = True
            HighChecker = True
            Row8Checker = True
            OddChecker = True
        elif spin == 24:
            Single24Checker = True
            Vertical24Checker = True
            Vertical27Checker = True
            Horizontal16Checker = True
            FourWay14Checker = True
            FourWay16Checker = True
            SixWay7Checker = True
            SixWay8Checker = True
            column3Checker = True
            BlackChecker = True
            Third2Checker = True
            HighChecker = True
            Row8Checker = True
            EvenChecker = True
        elif spin == 25:
            Single25Checker = True
            Vertical25Checker = True
            Vertical28Checker = True
            Horizontal17Checker = True
            FourWay15Checker = True
            FourWay17Checker = True
            SixWay8Checker = True
            SixWay9Checker = True
            column1Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row9Checker = True
            OddChecker = True
        elif spin == 26:
            Single26Checker = True
            Vertical26Checker = True
            Vertical29Checker = True
            Horizontal17Checker = True
            Horizontal18Checker = True
            FourWay15Checker = True
            FourWay16Checker = True
            FourWay17Checker = True
            FourWay18Checker = True
            SixWay8Checker = True
            SixWay9Checker = True
            column2Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row9Checker = True
            EvenChecker = True
        elif spin == 27:
            Single27Checker = True
            Vertical27Checker = True
            Vertical30Checker = True
            Horizontal18Checker = True
            FourWay16Checker = True
            FourWay18Checker = True
            SixWay8Checker = True
            SixWay9Checker = True
            column3Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row9Checker = True
            OddChecker = True
        elif spin == 28:
            Single28Checker = True
            Vertical28Checker = True
            Vertical31Checker = True
            Horizontal19Checker = True
            FourWay17Checker = True
            FourWay19Checker = True
            SixWay9Checker = True
            SixWay10Checker = True
            column1Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row10Checker = True
            EvenChecker = True
        elif spin == 29:
            Single29Checker = True
            Vertical29Checker = True
            Vertical32Checker = True
            Horizontal19Checker = True
            Horizontal20Checker = True
            FourWay17Checker = True
            FourWay18Checker = True
            FourWay19Checker = True
            FourWay20Checker = True
            SixWay9Checker = True
            SixWay10Checker = True
            column2Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row10Checker = True
            OddChecker = True
        elif spin == 30:
            Single30Checker = True
            Vertical30Checker = True
            Vertical33Checker = True
            Horizontal20Checker = True
            FourWay18Checker = True
            FourWay20Checker = True
            SixWay9Checker = True
            SixWay10Checker = True
            column3Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row10Checker = True
            EvenChecker = True
        elif spin == 31:
            Single31Checker = True
            Vertical31Checker = True
            Vertical34Checker = True
            Horizontal21Checker = True
            FourWay19Checker = True
            FourWay21Checker = True
            SixWay10Checker = True
            SixWay11Checker = True
            column1Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row11Checker = True
            OddChecker = True
        elif spin == 32:
            Single32Checker = True
            Vertical32Checker = True
            Vertical35Checker = True
            Horizontal21Checker = True
            Horizontal22Checker = True
            FourWay19Checker = True
            FourWay20Checker = True
            FourWay21Checker = True
            FourWay22Checker = True
            SixWay10Checker = True
            SixWay11Checker = True
            column2Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row11Checker = True
            EvenChecker = True
        elif spin == 33:
            Single33Checker = True
            Vertical33Checker = True
            Vertical36Checker = True
            Horizontal22Checker = True
            FourWay20Checker = True
            FourWay22Checker = True
            SixWay10Checker = True
            SixWay11Checker = True
            column3Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row11Checker = True
            OddChecker = True
        elif spin == 34:
            Single34Checker = True
            Vertical34Checker = True
            Horizontal23Checker = True
            FourWay21Checker = True
            SixWay11Checker = True
            column1Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row12Checker = True
            EvenChecker = True
        elif spin == 35:
            Single35Checker = True
            Vertical35Checker = True
            Horizontal23Checker = True
            Horizontal24Checker = True
            FourWay21Checker = True
            FourWay22Checker = True
            SixWay11Checker = True
            column2Checker = True
            BlackChecker = True
            Third3Checker = True
            HighChecker = True
            Row12Checker = True
            OddChecker = True
        elif spin == 36:
            Single36Checker = True
            Vertical36Checker = True
            Horizontal24Checker = True
            FourWay22Checker = True
            SixWay11Checker = True
            column3Checker = True
            RedChecker = True
            Third3Checker = True
            HighChecker = True
            Row12Checker = True
            EvenChecker = True
        action = 8

    if action == 8:
        if Rows == True:
            if Row1 == True and Row1Checker == True:
                Rowbet = Rowbet * 11
                currentbalance += Rowbet
                print(f'You won your bet on rows, earning you {Rowbet}!')
            elif Row2 == True and Row2Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row3 == True and Row3Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row4 == True and Row4Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row5 == True and Row5Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row6 == True and Row6Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row7 == True and Row7Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row8 == True and Row8Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row9 == True and Row9Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row10 == True and Row10Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row11 == True and Row11Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row12 == True and Row12Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            elif Row13 == True and Row13Checker == True:
                Rowbet = Rowbet * 11
                print(f'You won your bet on rows, earning you {Rowbet}!')
                currentbalance += Rowbet
            else:
                print('You did not win your bet on rows.')
                currentbalance -= Rowbet

        if Columns == True:
            if column1 == True and column1Checker == True:
                columnbet = columnbet * 2
                print(f'You won your bet on columns, earning you {columnbet}!')
                currentbalance += columnbet
            elif column2 == True and column2Checker == True:
                columnbet = columnbet * 2
                print(f'You won your bet on columns, earning you {columnbet}!')
                currentbalance += columnbet
            elif column3 == True and column3Checker == True:
                columnbet = columnbet * 2
                print(f'You won your bet on columns, earning you {columnbet}!')
                currentbalance += columnbet
            else:
                print('You did not win your bet on columns')
                currentbalance -= columnbet

        if Thirds == True:
            if Third1 == True and Third1Checker == True:
                Thirdbet = Thirdbet * 2
                print(f'You won your bet on thirds, earning you {Thirdbet}!')
                currentbalance += Thirdbet
            elif Third2 == True and Third2Checker == True:
                Thirdbet = Thirdbet * 2
                print(f'You won your bet on thirds, earning you {Thirdbet}!')
                currentbalance += Thirdbet
            elif Third3 == True and Third3Checker == True:
                Thirdbet = Thirdbet * 2
                print(f'You won your bet on thirds, earning you {Thirdbet}!')
                currentbalance += Thirdbet
            else:
                print('You lost your bet on thirds.')
                currentbalance -= Thirdbet

        if OddEven == True:
            if Odd == True and OddChecker == True:
                print(f'You won your bet on odd, earning you {OddEvenbet}!')
                currentbalance += OddEvenbet
            elif Even == True and EvenChecker == True:
                print(f'You won your bet on even, earning you {OddEvenbet}!')
                currentbalance += OddEvenbet
            else:
                print('You lost your bet on odd/even.')
                currentbalance -= OddEvenbet

        if Colours == True:
            if Red == True and RedChecker == True:
                print(f'You won your bet on odd, earning you {Colourbet}!')
                currentbalance += Colourbet
            elif Black == True and BlackChecker == True:
                print(f'You won your bet on black, earning you {Colourbet}!')
                currentbalance += Colourbet
            else:
                print('You lost your bet on colours.')
                currentbalance -= Colourbet

        if HighLow == True:
            if High == True and HighChecker == True:
                print(f'You won your bet on high, earning you {HighLowbet}!')
                currentbalance += HighLowbet
            elif Low == True and LowChecker == True:
                print(f'You won your bet on low, earning you {HighLowbet}!')
                currentbalance += HighLowbet
            else:
                print('You lost your bet on high/low.')
                currentbalance -= HighLowbet

        if Single == True:
            if Single0 == True and Single0Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 0, winning you {Singlebet}!!')
                currentbalance += Singlebet
            elif Single1 == True and Single1Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 1, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single2 == True and Single2Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 2, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single3 == True and Single3Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 3, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single4 == True and Single4Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 4, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single5 == True and Single5Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 5, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single6 == True and Single6Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 6, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single7 == True and Single7Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 7, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single8 == True and Single8Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 8, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single9 == True and Single9Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 9, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single10 == True and Single10Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 10, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single11 == True and Single11Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 11, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single12 == True and Single12Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 12, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single13 == True and Single13Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 13, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single14 == True and Single14Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 14, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single15 == True and Single15Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 15, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single16 == True and Single16Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 16, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single17 == True and Single17Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 17, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single18 == True and Single18Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 18, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single19 == True and Single19Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 19, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single20 == True and Single20Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 20, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single21 == True and Single21Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 21, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single22 == True and Single22Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 22, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single23 == True and Single23Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 23, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single24 == True and Single24Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 24, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single25 == True and Single25Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 25, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single26 == True and Single26Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 26, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single27 == True and Single27Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 27, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single28 == True and Single28Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 28, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single29 == True and Single29Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 29, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single30 == True and Single30Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 30, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single31 == True and Single31Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 31, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single32 == True and Single32Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 32, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single33 == True and Single33Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 33, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single34 == True and Single34Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 34, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single35 == True and Single35Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 35, winning you {Singlebet}!')
                currentbalance += Singlebet
            elif Single36 == True and Single36Checker == True:
                Singlebet = Singlebet * 35
                print(f'You won your bet on 36, winning you {Singlebet}!')
                currentbalance += Singlebet
            else:
                print('You lost your single number bet.')
                currentbalance -= Singlebet

        if Double == True:
            if Vertical1 == True and Vertical1Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical2 == True and Vertical2Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical3 == True and Vertical3Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical4 == True and Vertical4Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical5 == True and Vertical5Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical6 == True and Vertical6Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical7 == True and Vertical7Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical8 == True and Vertical8Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical9 == True and Vertical9Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical10 == True and Vertical10Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical11 == True and Vertical11Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical12 == True and Vertical12Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical13 == True and Vertical13Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical14 == True and Vertical14Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical15 == True and Vertical15Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical16 == True and Vertical16Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical17 == True and Vertical17Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical18 == True and Vertical18Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical19 == True and Vertical19Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical20 == True and Vertical20Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical21 == True and Vertical21Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical22 == True and Vertical22Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical23 == True and Vertical23Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical24 == True and Vertical24Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical25 == True and Vertical25Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical26 == True and Vertical26Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical27 == True and Vertical27Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical28 == True and Vertical28Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical29 == True and Vertical29Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical30 == True and Vertical30Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical31 == True and Vertical31Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical32 == True and Vertical32Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical33 == True and Vertical33Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical34 == True and Vertical34Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical35 == True and Vertical35Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Vertical36 == True and Vertical36Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your veritical bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal1 == True and Horizontal1Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal2 == True and Horizontal2Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal3 == True and Horizontal3Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal4 == True and Horizontal4Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your vhorizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal5 == True and Horizontal5Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal6 == True and Horizontal6Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal7 == True and Horizontal7Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal8 == True and Horizontal8Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal9 == True and Horizontal9Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal10 == True and Horizontal10Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal11 == True and Horizontal11Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal12 == True and Horizontal12Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal13 == True and Horizontal13Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal14 == True and Horizontal14Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal15 == True and Horizontal15Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal16 == True and Horizontal16Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal17 == True and Horizontal17Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal18 == True and Horizontal18Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal19 == True and Horizontal19Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal20 == True and Horizontal20Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal21 == True and Horizontal21Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal22 == True and Horizontal22Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal23 == True and Horizontal23Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            elif Horizontal24 == True and Horizontal24Checker == True:
                Doublebet = Doublebet * 17
                print(f'You won your horizontal bet, winning you {Doublebet}!')
                currentbalance += Doublebet
            else:
                print('You lost your 2 Way bet.')
                currentbalance -= Doublebet