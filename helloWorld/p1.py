from Tkinter import *
import tkMessageBox
'''
multi line comment???


'''
i=0


def helloWorld():
        global i
        global b
        msg="hello world %d" % (i)
        print msg
        b.configure(text=msg)
        i+=1

        
top = Tk()
b= Button(text="click me now!!!!", command=helloWorld)
b.pack()


#
#C = Canvas(top, bg="blue", height=250, width=300)
#coord = 10, 50, 240 , 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")
#C.pack()
top.mainloop()

