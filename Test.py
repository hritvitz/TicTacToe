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

board = ["", "", "", "", "", "", "", "", ""]#empty list to store the data of the grid

def handel_click(event):
    if event.x < 140:
        col=0
    elif event.x < 260:
        col=1
    else:
        col=2

    if event.y < 113:
        row=0
    elif event.y < 187:
        row=1
    else:
        row=2
    '''print(col, row)'''

    #finding left and right of each box

    if col==0:
        left = 60
        right = 140
    elif col==1:
        left = 140
        right = 260
    else:
        left = 260
        right = 340

    #finding top and bottom of each box

    if row==0:
        top = 40
        bottom = 113
    elif row==1:
        top = 113
        bottom = 187
    else:
        top = 187
        bottom = 260

    #finiding mid point of the boxes

    x = (left + right)/2
    y = (top + bottom)/2

    cell = row*3+col    #numbers all cells in order

    print(cell)

    if board[cell]=="":
        print("this cell is empty")
        board[cell] = "x"
        Canvas.create_line(left+15, top+15, right-15, bottom-15, width=4)
        Canvas.create_line(right-15, top+15, left+15, bottom-15, width=4)
    else:
        print("this cell is full")

    
Canvas.bind("<Button-1>", handel_click)

root.mainloop()

