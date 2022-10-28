import tkinter as Tk


jendela = Tk.Tk()
jendela.configure(bg="light blue")
jendela.geometry("310x400")
jendela.title("Calculator")
# Jendela

label =Tk.Label(text="Calculator", font="normal 25", bg="light blue")
label.pack()

jendela.mainloop()
