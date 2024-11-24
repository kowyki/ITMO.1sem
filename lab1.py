import os, time

def start():
    colorWhite = '\u001b[47m'
    colorRed = '\u001b[41m'
    colorBreak = '\u001b[0m'
    cH, cW = 20, 9 # consoleHeight, consoleWidth
    draw(cH, cW, colorRed, colorWhite, colorBreak)
    
    
def draw(cH, cW, cRed, cWhite, cBreak):
    os.system('cls')
    drawFlag(cH, cW, cRed, cWhite, cBreak)
    time.sleep(2)
    os.system('cls')
    drawPattern(cH, cW, cRed, cBreak)
    time.sleep(2)
    os.system('cls')
    drawFunction(cH, cW, cRed, cBreak)
    time.sleep(2)
    os.system('cls')
    chart(cWhite, cBreak)


def drawFlag(cH, cW, cRed, cWhite, cBreak, fH=2, fW=3): #flagHeight, flagWidth
    for y in range(fH*cW):
        for x in range(fW*cH):
            if (cW * (x - (fW * cH)/2))**2 + (cH*(y - (fH*cW)/2))**2 <= ((3*fH/5) * (cH*cW/2))**2:
                print(f'{cRed} ', end=cBreak)
            else: print(f'{cWhite} ', end=cBreak)
        print()


def drawPattern(cH, cW, cRed, cBreak, fH=2, fW=3):
    for y in range(fH*cW):
        for x in range(fW*cH):
            rhomb_first = abs(round(cH*y - cH*6)) + abs(round(cW*x - cH*6)) 
            rhomb_second = abs(round(cH*y - cH*6)) + abs(round(cW*x - cH*18)) 

            if rhomb_first in range(6*cH - 10, 6*cH + 10) or rhomb_second in range(6*cH - 10, 6*cH + 10):
                print(f'{cRed} ', end=cBreak)
            else: print(' ', end='')
        print()


def drawFunction(cH, cW, cRed, cBreak, fH=2, fW=3):
    for y in range(fH*cW):
        for x in range(fW*cH):
            if y-0.6 <= (fH*cW - 3*cW*x/cH) <= y+0.7:
                print(f'{cRed} ', end=cBreak)
            else: print(' ', end='')
        print()


def chart(cWhite, cBreak):
    nums = [float(x.strip()) for x in open('sequence.txt') if float(x.strip()) < 0]
    belowPerc = round(len([x for x in nums if x < -5])/len(nums), 1)*100
    abovePerc = round(len([x for x in nums if x > -5])/len(nums), 1)*100
    elements_group = {'>-5': belowPerc, '<-5': abovePerc}
    
    print()
    for row_num in range(11):
        percentage = (10-row_num)*10
        print(str(percentage).ljust(4, " "), end='')
        for elem in elements_group.values():
            if percentage <= elem: print(f'{cWhite} ', end=f'{cBreak}   ')
            else: print(' ', end='   ')
        print()
    print(''.ljust(3, " "), end='')
    for name in elements_group.keys():
        print(name.ljust(4, " "), end='')
    print()

if __name__ == '__main__':
    start()



