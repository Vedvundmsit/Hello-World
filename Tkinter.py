import tkinter as tk

window = tk.Tk() #Used to initiate Window
window.title("GUI")
label = tk.Label(window, text="Hello World!")
canvas = tk.Canvas(window, width = 500, height=500) 

label.pack()
canvas.pack()
window.mainloop()