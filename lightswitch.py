import tkinter as tk

window = tk.Tk()



# schijf hier tussen je code
window.configure(bg="black")

def input():
    if(button['text']=='light is off'):
        button.config(text="light is on")
        window.configure(bg="yellow")
        print("light is off")
    else:
        button.config(text="light is off")
        window.configure(bg="black")
        print("light is on")



# schijf hier tussen je code

button = tk.Button(text='light is off', bg="white", fg="black", command= input)
button.pack(pady = 100, padx = 100)

window.mainloop()