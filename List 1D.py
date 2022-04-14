from tkinter import *
import random

root = Tk()
root.title("List")
root.geometry("400x400")
root.config(bg = "mediumorchid1")
list = (  " bottle , tiffin, bag, id card, iced box, mat, cup, plate, spoons")
labellist=Label(root, fg="violetred", bg = "mediumorchid1")

labelsorted=Label(root,fg="violetred", bg = "mediumorchid1")



def start():
    print("list")
    randomlist = random.sample(range(1,10),5)
    labellist["text"]="listed item:" + str(list)
    randomlist.sort()

btn = Button(root, text = "Which item to put in bag", command = start,fg="violetred", bg = "darkorchid4")
btn.pack()
labellist.pack()
root.mainloop()
