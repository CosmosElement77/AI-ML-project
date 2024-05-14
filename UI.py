from Imports import *

# from Movie_Recommendation_System import *
from tkinter import Label,Entry ,Button


global movie
def store():
    movie=textbox.get()
root=tkinter.Tk()
text = tkinter.StringVar()
root.title("Movie Recommendation System Using Machine Learning")
Heading=Label(root , text="Movie Recommendation System Using Machine Learning" ,font=("Arial", 25))
Heading.place(x=235,y=100)

textbox=Entry(root,font=("Comic Sans MS",15,"bold"),textvariable=text,width=70,bd=2,bg="white")
textbox.place(x=240,y=350)       #The input box#
textbox.focus()
button=Button(root,text="Search",font=("Times",15,"bold"),width=10,bd=2,bg="white",command=store)
button.place(x=560,y=398)
root.mainloop()