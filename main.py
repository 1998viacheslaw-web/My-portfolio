import tkinter as tk
import winsound
import time

window=tk.Tk()

window.title('From text to Morse')
window.geometry('800x600')
window.maxsize(800,600)
window.resizable(True,True)
window.configure(bg='black')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.iconbitmap('logo.ico')


MORSE_CODE_DICT={'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.','f':'..-.',
                 'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
                 'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
                 's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
                 'y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--',
                 '4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
                 '.':'.-.-.-',',':'--..--','?':'..--..',' ':' '}


def text_to_morse():
  result=[]
  text=entry_text_to_morse.get().lower()
  for char in text:
    if char in MORSE_CODE_DICT:
      result.append(MORSE_CODE_DICT[char])
    else:
      label_result.config(text='You have typed invalid symbol')
      return
  label_result.config(text=' '.join(result))

def clear_text():
  entry_text_to_morse.delete(0,tk.END)
  label_result.config(text='')


def morse_to_text():
  reversed_dict={v:k for k, v in MORSE_CODE_DICT.items()}
  result=[]
  morse=entry_morse_to_text.get()
  for symbol in morse.split(' '):
    if symbol=='':
        result.append(' ')
        continue
    if symbol in reversed_dict:
      result.append(reversed_dict[symbol])
    else:
      label_result1.config(text='You have typed invalid symbol')
      return
  label_result1.config(text=''.join(result))

def clear_morse():
  entry_morse_to_text.delete(0,tk.END)
  label_result1.config(text='')

def play_sound(label_result):
  for symbol in label_result:
    if symbol=='.':
      winsound.Beep(700,200)
      time.sleep(0.2)
    elif symbol=='-':
      winsound.Beep(700,600)
      time.sleep(0.2)
    else:
      time.sleep(0.6)

def copy_morse():
  window.clipboard_clear()
  window.clipboard_append(label_result.cget('text'))

def copy_text():
  window.clipboard_clear()
  window.clipboard_append(label_result1.cget('text'))



label_text_to_morse=tk.Label(window, text='Convert text to Morse',
                             font=('Arial',12),
                             fg='green', bg='black', width=20,
                             height=1, anchor='w',
                             borderwidth=0)
label_text_to_morse.grid(row=0, column=0)

entry_text_to_morse=tk.Entry(window, width=50, font=('Arial', 13),
                             fg='green', bg='black', relief='solid',
                             borderwidth=3, highlightcolor='green',
                              justify='left')
entry_text_to_morse.grid(row=1, column=0, columnspan=3)

label_result=tk.Label(window, text='',font=('Arial', 13),
                             fg='green', bg='black', relief='solid',
                             borderwidth=3, highlightbackground='green',highlightcolor='green', highlightthickness=2,
                              justify='left' )
label_result.grid(row=2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

button_convert=tk.Button(window, text='Convert', command=text_to_morse,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_convert.grid(row=3, column=0)

button_play=tk.Button(window, text='Play', command=lambda: play_sound(label_result.cget('text')),
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_play.grid(row=3, column=2)

button_clear=tk.Button(window, text='Clear', command=clear_text,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_clear.grid(row=3, column=1)

label_morse_to_text=tk.Label(window, text='Convert Morse to text',
                             font=('Arial',12),
                             fg='green', bg='black', width=20,
                             height=1, anchor='w',
                             borderwidth=0)
label_morse_to_text.grid(row=4, column=0)

entry_morse_to_text=tk.Entry(window, width=50, font=('Arial', 13),
                             fg='green', bg='black', relief='solid',
                             borderwidth=3, highlightcolor='green',
                              justify='left')
entry_morse_to_text.grid(row=5, column=0, columnspan=3)

label_result1=tk.Label(window, text='',font=('Arial', 13),
                             fg='green', bg='black', relief='solid',
                             borderwidth=3, highlightbackground='green',highlightcolor='green', highlightthickness=2,
                              justify='left' )
label_result1.grid(row=6, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

button_convert1=tk.Button(window, text='Convert', command=morse_to_text,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_convert1.grid(row=7, column=0)

button_clear1=tk.Button(window, text='Clear', command=clear_morse,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_clear1.grid(row=7, column=1)

button_copy=tk.Button(window, text='Copy morse', command=copy_morse,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_copy.grid(row=8, column=0, pady=10)

button_copy1=tk.Button(window, text='Copy text', command=copy_text,
                         font=('Arial', 12), fg='white', bg='green',
                         width=12, height=4, relief='solid',
                         borderwidth=0, state='normal')
button_copy1.grid(row=8, column=1, pady=10)



window.mainloop()


