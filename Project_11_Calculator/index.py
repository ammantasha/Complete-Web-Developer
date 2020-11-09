from tkinter import *
def btnclick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
def btnclr():
    global operator
    operator=""
    text_input.set("")
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
textDisplay=Entry(cal,font=('arial',20,'bold'),
                  textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",
                  justify='right').grid(columnspan=4)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='9',bg="grey",command=lambda:btnclick(9)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='8',bg="grey",command=lambda:btnclick(8)).grid(row=1,column=1)
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='7',bg="grey",command=lambda:btnclick(7)).grid(row=1,column=2)
add=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='+',bg="powder blue",command=lambda:btnclick('+')).grid(row=1,column=3)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='6',bg="grey",command=lambda:btnclick(6)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='5',bg="grey",command=lambda:btnclick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='4',bg="grey",command=lambda:btnclick(4)).grid(row=2,column=2)
sub=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='-',bg="powder blue",command=lambda:btnclick('-')).grid(row=2,column=3)
btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='3',bg="grey",command=lambda:btnclick(3)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='2',bg="grey",command=lambda:btnclick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='1',bg="grey",command=lambda:btnclick(1)).grid(row=3,column=2)
mul=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='*',bg="powder blue",command=lambda:btnclick('*')).grid(row=3,column=3)
btnequal=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='=',bg="powder blue",command=btnequal).grid(row=4,column=2)
btnclr=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='C',bg="powder blue",command= btnclr).grid(row=4,column=1)
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='0',bg="grey",command=lambda:btnclick('0')).grid(row=4,column=0)
div=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
          text='/',bg="powder blue",command=lambda:btnclick('/')).grid(row=4,column=3)
cal.mainloop()
