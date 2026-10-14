import tkinter as tk

root = tk.Tk()
root.title("TIC TAC TOE")
root.geometry("400x300")

Canvas = tk.Canvas(root, width=400, height=260, bg="#D6F0FF")
Canvas.pack()

Canvas.create_line(140, 40, 140, 260, width=3)
Canvas.create_line(260, 40, 260, 260, width=3)

Canvas.create_line(60, 113, 340, 113, width=3)
Canvas.create_line(60, 187, 340, 187, width=3)

def handel_click(event):
    print("we have detected a click!")

Canvas.bind("<Button-1>", handel_click)

root.mainloop()


