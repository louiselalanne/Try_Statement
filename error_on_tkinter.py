from tkinter import *
from tkinter import messagebox
root= Tk()
root.title("Errors and Try Statement")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    entrada = input_box.get()

    try:
        print(number + entrada)
    except(TypeError):
        messagebox.showinfo("Error", "Não podemos adicionar dois tipos de dados diferentes: numeros e strings")
        
btn = Button(root, text="Clique", command=addition)
btn.pack()

root.mainloop()