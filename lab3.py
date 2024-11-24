from tkinter import *
from re import match
from random import sample
from PIL import Image, ImageTk

def generateKey():
    inputData = mainEntry.get().upper()
    if match('[A-Za-z]', inputData) is not None and len(inputData) == 6:
        errorLabel['text'] = ''
        alpha = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
        result = []
        result.append("".join([inputData[i] for i in sample(range(6), 3)]))
        result.append("".join([str(alpha.index(l)+1)[-1] for l in inputData]))
        result.append("".join([inputData[i] for i in sample(range(6), 3)]))
        keyLabel['text'] = "KEY:   " + "-".join(result)

    else: 
        errorLabel['text'] = 'Неверное значение'

def createWindow():
    main = Tk()
    img = Image.open("minecraft.png")
    bgImage = ImageTk.PhotoImage(img)
    label = Label(main, image=bgImage)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label.image = bgImage

    main.title("Minecraft KEYGEN")
    main.geometry("400x200")
    return main

if __name__ == '__main__':
    window = createWindow()

    greetLabel = Label(window)
    greetLabel.configure(text='Генерация ключа для Minecraft\nВведите набор из шести символов латинского алфавита')
    greetLabel.place(x=10, y=10, height=60, width=400)

    errorLabel = Label(window)
    errorLabel.configure(fg='red')
    errorLabel.place(x=60, y=106, height=20, width=130)

    keyLabel = Label(window)
    keyLabel.place(x=60, y=66, height=20, width=250)

    mainEntry = Entry(window)
    mainEntry.place(x=10, y=60, width=100, height=30)

    btnGen = Button(window)
    btnGen.configure(text='GEN', command=generateKey)
    btnGen.place(x=10, y=100, height=30, width=50)

    window.mainloop()


