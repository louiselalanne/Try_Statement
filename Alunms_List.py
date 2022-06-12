from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x400")

lista_nomes = ["Minguelito", "Thom", "Malu", "Mulan", "Elsa"]
dict_nomes = {"name":"vovó", "age":"28"}

try:
    print(lista_nomes[3])
    print(dict_nomes["Kawaii"])
except IndexError:
    messagebox.showinfo("Error","Esse indice não existe.")
except KeyError:
    messagebox.showinfo("Error","Essa key não existe.")

root.mainloop()