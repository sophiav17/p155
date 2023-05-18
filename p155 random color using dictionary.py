from tkinter import*
import random

root = Tk()

root.title("Random Colour Using Dictionary")
root.geometry("600x400")

dictionary = {'maroon1 : 0', 'lawngreen : 1', 'magenta2 : 2', 'purple1: 3', 'springgreen2 : 4', 'chocolate1 : 5', 'deeppink : 6', 'cyan : 7', 'darkorange : 8', 'crimson : 9'}

def background_color_random() :
    background_color = random.randint(0, 8)
    random_color = dictionary["colours"][background_color]
    print(random_color)
    root.configure(background = random_color)
    
btn = Button(root, text = "Click Me", command = background_color_random)    
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
root.mainloop() 