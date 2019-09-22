#!/user/bin/python
from Tkinter import *


def hi():
        numDisplay.insert(END, 1)
        
def two():
        numDisplay.insert(END, 2)
        
        
def three():
        numDisplay.insert(END, 3)
def four():
        numDisplay.insert(END, 4)
def five():
        numDisplay.insert(END, 5)
def six():
        numDisplay.insert(END, 6)
def seven():
        numDisplay.insert(END, 7)
def eight():
        numDisplay.insert(END, 8)
def nine():
        numDisplay.insert(END, 9)
def zero():
        numDisplay.insert(END, 0)
def mult():
        numDisplay.insert(END, "*")
def add():
        numDisplay.insert(END, "+")
def subtract():
        numDisplay.insert(END, "-")
def divide():
        numDisplay.insert(END, "/")
def equal():
        answer = number.get()
        if answer.count("*") == 1:
                fnum= float(answer[:-(len(answer)-(answer.index("*")))])
                snum= float(answer[-(len(answer)- (answer.index("*")+1)):])
                final = float(fnum*snum)
                numDisplay.delete(0, END)
                numDisplay.insert(0, final)
        elif answer.count("+") == 1:
                fnum= float(answer[:-(len(answer)-(answer.index("+")))])
                snum= float(answer[-(len(answer)- (answer.index("+")+1)):])
                final = float(fnum+snum)
                numDisplay.delete(0, END)
                numDisplay.insert(0, final)
        elif answer.count("-") == 1:        
                fnum= float(answer[:-(len(answer)-(answer.index("-")))])
                snum= float(answer[-(len(answer)- (answer.index("-")+1)):])
                final = float(fnum-snum)
                numDisplay.delete(0, END)
                numDisplay.insert(0, final)
        elif answer.count("/") == 1:        
                fnum= float(answer[:-(len(answer)-(answer.index("/")))])
                snum= float(answer[-(len(answer)- (answer.index("/")+1)):])
                final = float(fnum/snum)
                numDisplay.delete(0, END)
                numDisplay.insert(0, final)
        elif answer.count("+" and "-" and "*" and "/") == 0:
                return
        else:
                numDisplay.delete(0, END)
                numDisplay.insert(0, "ERROR")
def allclear():
        numDisplay.delete(0, END)
def delete():
        answer = number.get()
        number_left = answer[:-1]
        numDisplay.delete(0, END)
        numDisplay.insert(0, number_left)
def decimal():
        numDisplay.insert(END, ".")
        
root = Tk()

frame = Frame(root)
frame.pack()
root.geometry("185x340")
root.title("Mini Calculator")

number = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

numDisplay = Entry(frame, textvariable = number, bd = 20, insertwidth = 1, font = 30)
numDisplay.pack(side = TOP)
frame1 = Frame(root)
frame1.pack(side = TOP)
button1 = Button(frame1, padx=16, pady=16, text="1", fg="black", command = hi)
button1.pack(side = LEFT)
button2 = Button(frame1, padx=16, pady=16, text="2", fg="black", command = two).pack(side = LEFT)
button3 = Button(frame1, padx=16, pady=16, text="3", fg="black", command = three).pack(side = LEFT)
button_mult = Button(frame1, padx=16, pady=16, text="*", fg="black", command = mult).pack(side = LEFT)

frame2= Frame(root)
frame2.pack(side = TOP)
button4 = Button(frame2, padx=16, pady=16, text="4", fg="black", command = four).pack(side = LEFT)
button5 = Button(frame2, padx=16, pady=16, text="5", fg="black", command = five).pack(side = LEFT)
button6 = Button(frame2, padx=16, pady=16, text="6", fg="black", command = six).pack(side = LEFT)
button_equal = Button(frame2, padx=16, pady=16, text="/", fg="black", command = divide).pack(side = LEFT)

frame3= Frame(root)
frame3.pack(side = TOP)
button4 = Button(frame3, padx=16, pady=16, text="7", fg="black", command = seven).pack(side = LEFT)
button5 = Button(frame3, padx=16, pady=16, text="8", fg="black", command = eight).pack(side = LEFT)
button6 = Button(frame3, padx=16, pady=16, text="9", fg="black", command = nine).pack(side = LEFT)
button_plus = Button(frame3, padx=16, pady=16, text="+", fg="black", command = add).pack(side = LEFT)

frame4= Frame(root)
frame4.pack(side = TOP)
button_decimal = Button(frame4, padx=17.5, pady=16, text=".", fg="black", command = decimal).pack(side = LEFT)
button_zero = Button(frame4, padx=16, pady=16, text="0", fg="black", command = zero).pack(side = LEFT)
button_equals = Button(frame4, padx=15, pady=16, text="=", fg="black", command = equal).pack(side = LEFT)
button_subtract = Button(frame4, padx=16, pady=16, text="-", fg="black", command = subtract).pack(side = LEFT)

frame5 = Frame(root).pack(side = TOP)
button_delete = Button(frame5, padx=35, pady=16, text="DEL", fg="black", command=delete).pack(side = LEFT)
button_allclear = Button(frame5, padx=35, pady=16, text="AC", fg="black", command=allclear).pack(side = LEFT ) 
 

root.mainloop()
