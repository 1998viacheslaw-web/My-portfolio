import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("500x500")
window.resizable(False, False)

current_player = "X"
button=[]

def press_button(btn):
    global current_player
    if btn['text']=='':
        btn.configure(text=current_player, font=("Arial", 9))
        check_win()
        check_defeat()
        next_player()

def next_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_win():
    global current_player
    for row in button:
        if row[0]['text']==row[1]['text']==row[2]['text']!='':
            messagebox.showinfo('Winner!',f'Player "{current_player}" wins!')
            reset()
    for col in range(3):
        if button[0][col]['text']==button[1][col]['text']==button[2][col]['text']!='':
            messagebox.showinfo('Winner',f'Player "{current_player}" wins!')
            reset()

    if button[0][0]["text"] == button[1][1]["text"] == button[2][2]["text"] != "":
        messagebox.showinfo('Winner',f'Player "{current_player}" wins!')
        reset()

    if button[0][2]["text"] == button[1][1]["text"] == button[2][0]["text"] != "":
        messagebox.showinfo('Winner',f'Player "{current_player}" wins!')
        reset()

def check_defeat():
    for row in button:
        for btn in row:
            if btn['text'] == '':
                return
    messagebox.showinfo('Draw!', 'Friendship wins')
    reset()


def reset():
    global current_player
    current_player = "X"
    for row in button:
        for btn in row:
            btn.configure(text="")


for row in range(3):
    row_list=[]
    for col in range(3):
        btn=tk.Button(window, width=20, height=10, text='', highlightcolor='black',
                         highlightthickness=3, highlightbackground='black')
        btn.configure(command=lambda b=btn: press_button(b))
        btn.grid(row=row, column=col)
        row_list.append(btn)
    button.append(row_list)














window.mainloop()
