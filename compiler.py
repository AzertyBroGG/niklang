from main import NikitosLanguage

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

root = Tk()
root.attributes("-fullscreen", True)
root.title('Компилятор NIKLANG')

text = Text(root, height=6, bg = 'yellow', fg = 'blue')
text2 = Text(root, height=6, bg = 'purple', fg = 'beige')



def open_text_file():
    filetypes = (
        ('NikLang Project', '*.niklang *.nl'),
    )
    f = fd.askopenfile(filetypes=filetypes)
    content = ''
    if f:
        text.insert('1.0', f.read())

def compiler():
    main_code = text.get("1.0", END)
    nik = NikitosLanguage(main_code)
    text2.insert(END, f'\n{nik.compilator()}')


open_button = Button(
    root,
    text='Открыть код',
    bg = 'red',
    fg = 'white',
    command=open_text_file
)

open_button.pack(side = LEFT)

compile_button = Button(
    root,
    text='Скомпилировать код',
    bg = 'yellow',
    fg = 'blue',
    command=compiler
)
compile_button.pack(side = RIGHT)

text.pack()
text2.pack()

root.mainloop()