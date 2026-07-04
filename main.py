import tkinter as tk
import datetime
import random

window=tk.Tk()

window.title('Typing Speed Test')
window.geometry('300x300')
window.resizable(True,True)
window.configure(bg='white')

text_var=tk.StringVar()


texts=["The quick brown fox jumps over the lazy dog.","Python is a great programming language.",
       "Practice makes perfect every single day."]

text=''
mistakes=0
right_answers=0
start_time = None
timer_running = False

entry_field=tk.Entry(window,font=('Arial',14),fg='black',bg='white',borderwidth=2,
                     textvariable=text_var)
entry_field.grid(row=2,column=0,sticky='we',columnspan=3)

def on_text_change(*args):
  global mistakes, right_answers, timer_running
  typed=text_var.get()
  mistakes=0
  right_answers = 0

  for i, char in enumerate(typed):
    if i <len(text):
        if char!=text[i]:
          mistakes+=1
        else:
          right_answers+=1

  if typed == text and text!='':
        timer_running = False
        elapsed = datetime.datetime.now() - start_time
        seconds = int(elapsed.total_seconds())
        word_count = len(typed.split())
        minutes = seconds / 60
        wpm = int(word_count / minutes) if minutes > 0 else 0
        total = right_answers + mistakes
        accuracy = round(100 * right_answers / total, 1) if total > 0 else 0
        result_label.config(text=f"Time: {seconds} sec\nWPM: {wpm}\nAccuracy: {accuracy}%\nMistakes: {mistakes}")

text_var.trace_add("write", on_text_change)



def tick():
  if not timer_running:
    return
  elapsed = datetime.datetime.now() - start_time
  seconds = int(elapsed.total_seconds())
  timer_label.config(text=f"{seconds//60:02}:{seconds%60:02}")
  window.after(1000, tick)

def start_test():
  global text, mistakes, right_answers, start_time, timer_running
  record=entry_field.get()
  if record!='':
    entry_field.delete(0,tk.END)
  text=random.choice(texts)
  text_label.config(text=text)
  timer_running = True
  start_time=datetime.datetime.now()
  tick()

def reset_all():
  global text, mistakes, right_answers, start_time, timer_running
  text=''
  mistakes=0
  right_answers=0
  start_time = None
  timer_running = False
  timer_label.config(text='00:00')
  entry_field.delete(0,tk.END)
  result_label.config(text='Time:   \nWPM:  \nAccuracy:  \nMistakes:  ')



timer_label=tk.Label(window,text='00:00',font=('Consolas',24),fg='black',bg='white',borderwidth=0,pady=5)
timer_label.grid(row=0,column=0)

text_label=tk.Label(window,text='',font=('Times New Roman',14),fg='black',bg='white',
                    anchor='center',borderwidth=0,pady=5)
text_label.grid(row=1,column=0,sticky='we',columnspan=3)


start_button=tk.Button(window,text='Start Test',command=start_test,font=('Arial',12),
                       width=10,height=3,state='normal')
start_button.grid(row=3,column=0,pady=10)

result_label=tk.Label(window,text='Time:   \nWPM:  \nAccuracy:  \nMistakes:  ',
                      font=('Times New Roman',14),
                      fg='black',bg='white',borderwidth=0,pady=5)
result_label.grid(row=4,column=0,rowspan=2)

reset_button=tk.Button(window,text='Reset All',command=reset_all,font=('Arial',12),
                       width=10,height=3,state='normal')
reset_button.grid(row=3,column=1,pady=10)




window.mainloop()
