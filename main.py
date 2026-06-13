import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw

window = tk.Tk()
window.title('Watermarks Studio')
window.geometry('900x600')
window.resizable(False, False)
window.configure(bg='#1a1a1a')
window.iconbitmap('watermark.ico')

watermark_id = None
font_size = 24
image = None
watermark_x = 100
watermark_y = 100
canvas_image_id = None

# ── Ліва панель ─────────────────────────────────────────
left_panel = tk.Frame(window, bg='#2a2a2a', width=220)
left_panel.grid(row=0, column=0, sticky='ns')
left_panel.grid_propagate(False)

tk.Label(left_panel, text='Watermark Studio', font=('Verdana', 14, 'bold'),
         fg='white', bg='#2a2a2a').pack(pady=(20, 2))
tk.Label(left_panel, text='Add watermark to your image', font=('Verdana', 8),
         fg='grey', bg='#2a2a2a').pack(pady=(0, 20))

tk.Label(left_panel, text='Watermark text', font=('Arial', 9),
         fg='white', bg='#2a2a2a').pack(anchor='w', padx=15)

entry_text = tk.Entry(left_panel, width=26, font=('Arial', 9), fg='grey',
                      bg='#3a3a3a', relief='flat', borderwidth=5)
entry_text.pack(padx=15, pady=5)

tk.Label(left_panel, text='Opacity', font=('Arial', 9),
         fg='white', bg='#2a2a2a').pack(anchor='w', padx=15, pady=(10, 0))

opacity_slider = tk.Scale(left_panel, from_=0, to=255, orient='horizontal',
                          fg='white', bg='#2a2a2a', highlightthickness=0,
                          troughcolor='#555', length=190)
opacity_slider.set(128)
opacity_slider.pack(padx=15)
opacity_slider.config(command=lambda e: update_preview())

tk.Button(left_panel, text='Open Image', font=('Arial', 9), fg='white',
          bg='#444', width=22, height=1, borderwidth=0,
          command=lambda: open_image()).pack(pady=(20, 5), padx=15)

tk.Button(left_panel, text='Apply Watermark', font=('Arial', 9), fg='white',
          bg='#555', width=22, height=1, borderwidth=0,
          command=lambda: draw_watermark()).pack(pady=5, padx=15)

tk.Button(left_panel, text='Save Image', font=('Arial', 9), fg='white',
          bg='#792CA2', width=22, height=1, borderwidth=0,
          command=lambda: save_image()).pack(pady=5, padx=15)

tk.Button(left_panel, text='Reset All', font=('Arial', 9), fg='white',
          bg='#c0392b', width=22, height=1, borderwidth=0,
          command=lambda: reset_all()).pack(pady=(20, 5), padx=15)

# ── Права панель ─────────────────────────────────────────
right_panel = tk.Frame(window, bg='#1a1a1a')
right_panel.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

tk.Label(right_panel, text='Original', font=('Arial', 9),
         fg='grey', bg='#1a1a1a').grid(row=0, column=0, pady=(0, 5))
tk.Label(right_panel, text='Preview', font=('Arial', 9),
         fg='grey', bg='#1a1a1a').grid(row=0, column=1, pady=(0, 5))

label_original = tk.Label(right_panel, bg='#2a2a2a', width=40, height=20,
                           text='No image', fg='grey')
label_original.grid(row=1, column=0, padx=10)

canvas = tk.Canvas(right_panel, width=330, height=330, bg='#2a2a2a',
                   highlightthickness=0)
canvas.grid(row=1, column=1, padx=10)


# ── Placeholder ──────────────────────────────────────────
def on_entry_click(event):
    if entry_text.get() == 'Input text...':
        entry_text.delete(0, tk.END)
        entry_text.config(fg='white')

def on_focusout(event):
    if entry_text.get() == '':
        entry_text.insert(0, 'Input text...')
        entry_text.config(fg='grey')

entry_text.insert(0, 'Input text...')
entry_text.bind('<FocusIn>', on_entry_click)
entry_text.bind('<FocusOut>', on_focusout)


# ── Функції ───────────────────────────────────────────────
def open_image():
    global image
    filename = filedialog.askopenfilename(
        title='Choose an image',
        initialdir=r'C:\Users\Slavik',
        filetypes=[('Images', '*.png *.jpg')]
    )
    if filename:
        image = Image.open(filename)
        image.thumbnail((330, 330))

        tk_image = ImageTk.PhotoImage(image)
        label_original.config(image=tk_image, text='')
        label_original.image = tk_image

        canvas.create_image(0, 0, anchor='nw', image=tk_image)
        canvas.image = tk_image


def update_preview():
    global image
    watermark_text = entry_text.get()
    if image and watermark_text and watermark_text != 'Input text...':
        image_copy = image.copy().convert('RGBA')
        txt_layer = Image.new('RGBA', image_copy.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        draw.text((watermark_x, watermark_y), watermark_text,
                  fill=(255, 255, 255, opacity_slider.get()))
        result_image = Image.alpha_composite(image_copy, txt_layer)

        result = ImageTk.PhotoImage(result_image)
        canvas.result_image = result
        if canvas_image_id:
            canvas.itemconfig(canvas_image_id, image=result)
        else:
            canvas.create_image(0, 0, anchor='nw', image=result)

        canvas.lift(watermark_id)



def draw_watermark():
    global watermark_id, watermark_x, watermark_y
    watermark_text = entry_text.get()
    if watermark_text and watermark_text != 'Input text...' and image:
        watermark_x = 100
        watermark_y = 100
        update_preview()

        if watermark_id:
            canvas.delete(watermark_id)

        watermark_id = canvas.create_text(watermark_x, watermark_y,
                                          text=watermark_text,
                                          font=('Impact', font_size),
                                          fill='white')
        canvas.tag_bind(watermark_id, '<B1-Motion>', on_drag)
        canvas.tag_bind(watermark_id, '<MouseWheel>', on_scroll)
    elif not image:
        messagebox.showerror('Error!', 'Please open an image first!')
    elif watermark_text == 'Input text...' or not watermark_text:
        messagebox.showerror('Error!', 'Please enter watermark text!')


def on_drag(event):
    global watermark_x, watermark_y,watermark_id
    watermark_x = event.x
    watermark_y = event.y
    canvas.coords(watermark_id, watermark_x, watermark_y)
    update_preview()


def on_scroll(event):
    global font_size
    if event.delta > 0:
        font_size += 1
    else:
        font_size = max(8, font_size - 1)
    canvas.itemconfig(watermark_id, font=('Impact', font_size))
    update_preview()


def save_image():
    global image
    if watermark_id is not None:
        if image:
            watermark_text = entry_text.get()
            image_copy = image.copy().convert('RGBA')
            txt_layer = Image.new('RGBA', image_copy.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt_layer)
            draw.text((watermark_x, watermark_y), watermark_text,
                      fill=(255, 255, 255, opacity_slider.get()))
            result_image = Image.alpha_composite(image_copy, txt_layer)
            result_image = result_image.convert('RGB')

            directory = filedialog.askdirectory(
                title='Choose a directory',
                initialdir='C:/Users/Slavik',
            )
            if directory:
                result_image.save(f'{directory}/watermark.jpg')
                messagebox.showinfo('Success!', 'Image saved successfully!')
    else:
        messagebox.showerror('Error!', "The image doesn't have a watermark!")


def reset_all():
    global image, watermark_id, font_size, watermark_x, watermark_y
    canvas_image_id=None
    image = None
    font_size = 24
    watermark_x = 100
    watermark_y = 100
    if watermark_id:
        canvas.delete(watermark_id)
        watermark_id = None
    canvas.delete('all')
    label_original.config(image='', text='No image')
    entry_text.delete(0, tk.END)
    entry_text.insert(0, 'Input text...')
    entry_text.config(fg='grey')


window.mainloop()