import os
import tkinter as tk


def upgradePIP():
    os.system('start cmd /k python -m pip install --upgrade pip')


window = tk.Tk()
bgWindow = 'grey13'
colorFontWarning = 'red'
newVersionPIP = ''
currentVersionPIP = ''

window.title('Обновление PIP')
window.iconphoto(False, tk.PhotoImage(file='images/icon.png'))

canvas = tk.Canvas(
    window,
    width=500,
    height=300,
    bg=bgWindow
)
canvas.pack()

label1 = tk.Label(
    window,
    text='Обновление PIP',
    bg=bgWindow
)
label1.config(fg='white', font=('helvetica', 20))

# if currentVersionPIP != newVersionPIP:
#     label2 = tk.Label(
#         window,
#         text='Текущая версия: ""',
#         bg=bgWindow
#     )
#     label2.config(fg=colorFontWarning, font=('helvetica', 20))
# else:
#     label2 = tk.Label(
#         window,
#         text='Текущая версия: ""',
#         bg=bgWindow
#     )
#     label2.config(fg=colorFontWarning, font=('helvetica', 20))

canvas.create_window(250, 30, window=label1)
# canvas.create_window(250, 80, window=label2)

button = tk.Button(text='Обновить PIP', command=upgradePIP, font=('helvetica', 20), fg='white', bg='SpringGreen4')
canvas.create_window(250, 180, window=button)

window.mainloop()
