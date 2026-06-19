# This line will import tkinter bu we would not use the word tkinter bu we will use it tk beacause we have written tha import tkinter as tk that as will make that thing true like we canuse the tk instead of the longer word tkinter when it is needed .
import tkinter as tk
# This line will create a fuction that will create an user defined function change_colour with a variable known(named(defined)) as color .
def change_colour(color):
  # This line will change the baground colour when a specific colour button is pressed .
  root.configure(bg=color)
  # This line will create the window
root=tk.Tk()
# This line will set the window width and height to 700x700
root.geometry("700x700")
# These lines will create four buttons that will chane the baground colour when the button is pressed. 
button1=tk.Button(root,bg="green",text="Green",command=lambda:change_colour("green"))
button2=tk.Button(root,bg="orange",text="Orange",command=lambda:change_colour("orange"))
button3=tk.Button(root,bg="teal",text="Teal",command=lambda:change_colour("teal"))
button4=tk.Button(root,bg="sky blue",text="sky blue",command=lambda:change_colour("sky blue"))

'''button1.pack(pady=10,padx=10,side="left")
button2.pack(pady=10,padx=10,side="left")
button3.pack(pady=10,padx=10,side="left")
button4.pack(pady=10,padx=10,side="left")'''

# These lines will place the buttons at the given x and y coordinates.
button1.place(x=100,y=300)
button2.place(x=180,y=300)
button3.place(x=260,y=300)
button4.place(x=330,y=300)


'''button1.grid(row=6,column=10)
button2.grid(row=10,column=7)
button3.grid(row=8,column=12)
button4.grid(row=12,column=8)'''

# This line will hold the screen.
root.mainloop()