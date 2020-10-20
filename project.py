
from tkinter import *

def ab():


    #explanation of converting numbers in variables m,n,o,p,q,r.
    m="=>=> BINARY TO DECIMAL: =>=> \n\
1.Get the last digit of the binary number, call this digit the INP \n\
2.Make a variable, let's call it POWER.  Set the value to 0. \n\
3.Multiply the current digit with (2^POWER), store the result. \n\
4.Increment POWER by 1. \n\
5.Set the the currentDigit to the previous digit of the binary number. \n\
6.Repeat step 3 until all digits have been multiplied.\n\
7.Sum the result of step 3 to get the answer number...\n "
    n="=>=> DECIMAL TO HEXADECIMAL: =>=> \n\
1.Divide the decimal number by 16. \n\
2.Treat the division as an integer division.\n\
3.Write down the remainder (in hexadecimal).\n\
4.Divide the result again by 16.  Treat the division as an integer division.\n\
5.Repeat step 2 and 3 until result is 0.\n\
6.The hex value is the digit sequence of the remainders from the last to first...\n"
    o="=>=> DECIMAL TO OCTAL =>=> \n\
1.Take the given decimal number\n\
2.If the number is less than 8 the octal number is the same\n\
3.If the number is greater than 7 then Divide the number with 8\n\
4.Note the remainder\n\
5.Carry on the step 3 and 4 with the qoutient till it is less than 8\n\
6.Write the remainders in reverse order(bottom to top)\n\
7.The resultant is the equivalent octal number to the given decimal number...\n"
    p="=>=> OCTAL TO DECIMAL =>=>\n\
1.Take the given octal number.\n\
2.Find out the number of digits in the number\n\
3.Let it have n digits.\n\
4.Multiply each digit in the number with 8n-1,when the digit is in the nth position.\n\
5.Add all digits after multiplication.\n\
6.The resultant is the equivalent decimal to the given octal number.\nIf octal number contains a decimal point\n\
7.Let m digits are there after the decimal \n\
8.Multiply each digit after decimal with`1/8^m`,when the digit is the mth position...\n"
    q="=>=> HEXADECIMAL TO DECIMAL =>=> \n\
1.First we find the number of hexadecimal digits in the number. Let there be n numbers.\n\
2.Then we multiply each hexadecimal digit with 16n−1,\nwhen n is equal to number of position from right side.\n\
3.Then we add each number after multiplication.\n\
4.The resultant is equivalent hexadecimal number of the given decimal number...\n"
    r="=>=> DECIMAL TO BINARY =>=>\n\
1.Divide given number starting from 2 as suitable.\n\
2.Write remainder on the right side of quotient.\n\
3.Divide untill quotient will be 0.\n\
4.Now write binary number starting from lower end of that divison.\n\
5.Now write given number including quotient of lower end.that should be starting point...\n"

    T = Text(top, height=23, width=100,bg="black",fg="orange") 
    T.place(x=450,y=320) 
    
    inp=x.get()
    w=a.get()
    if (w is 1):    # BINARY TO DECIMAL AND THEN TO OTHER SYSTEMS
        inp=int(inp,2)
        bi=bin(inp)
        oc=oct(inp)
        dec=inp
        hexa=hex(inp)
        
        T.insert(END, m)
        T.insert(END, n)
        T.insert(END, o)
        
           
    elif(w is 2):
        inp=int(inp,8)
        bi=bin(inp)
        oc=oct(inp)
        dec=inp
        hexa=hex(inp)

        T.insert(END,p)
        T.insert(END,r)
        T.insert(END,n)
        
        
            
    elif(w is 3):   
        inp=int(inp)
        bi=bin(inp)
        oc=oct(inp)
        dec=inp
        hexa=hex(inp)

        T.insert(END,r)
        T.insert(END,o)
        T.insert(END,n)
             
    else:
        inp=int(inp,16)
        bi=bin(inp)
        oc=oct(inp)
        dec=inp
        hexa=hex(inp)

        T.insert(END,q)
        T.insert(END,r)
        T.insert(END,o)
        
    result=Label(top,text="Result:").place(x=100,y=290)

    l1=Label(top,text="Binary      :",fg="green").place(x=130,y=320)
    l2=Label(top,text="octal       :",fg="green").place(x=130,y=370)
    l3=Label(top,text="decimal     :",fg="green").place(x=130,y=420)
    l4=Label(top,text="hexadecimal :",fg="green").place(x=130,y=470)
   
    e1 = Label(top,width=15,height=1,text=bi,fg="red").place(x=250,y=320)
    e2 = Label(top,width=15,height=1,text=oc,fg="red").place(x=250,y=370)
    e3 = Label(top,width=15,height=1,text=dec,fg="red").place(x=250,y=420)
    e4 = Label(top,width=15,height=1,text=hexa,fg="red").place(x=250,y=470)
   
    explain=Label(top,text="Explanation:").place(x=450,y=290)
    
   
        
      
    
    
    

    

top=Tk()
top.title("Number Convertor")
a=IntVar()
x=StringVar()


lab=Label(top,text="Enter a number").place(x=280,y=10)
number=Entry(top,bd=5,textvariable=x).place(x=380,y=10)


ti=Label(top,text="Tick the number type you have entered:").place(x=280,y=50)
C1 = Radiobutton(top, text = "Binary            ", value=1 ,var=a, height=0, width = 10).place(x=350,y=80)
C2 = Radiobutton(top, text = "Octal             ", value=2 ,var=a,height=0, width = 10).place(x=350,y=110)
C3 = Radiobutton(top, text = "Decimal        ",value=3 ,var=a,height=0, width = 10).place(x=350,y=140)
C4 = Radiobutton(top, text = "Hexadecimal",value=4 ,var=a,height=0,width = 10).place(x=350,y=170)

but=Button(top,text="Result",command=ab).place(x=390,y=220)

top.config(bg="grey")
top.geometry("1300x700")
top.mainloop()
