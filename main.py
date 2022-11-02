# # make App
# pip install tkinterdnd2
# pyinstaller main.py --name dnd --onefile --noconsole --collect-data tkinterdnd2 --add-data="icon.ico:./" --icon=icon.ico      # for windows
# pyinstaller main.py --name dnd --onefile --noconsole --collect-data tkinterdnd2 --add-data="icon.icns:./" --icon=icon.icns    # for mac


from tkinter import *
from tkinterdnd2 import *
import utility63rabbits as util
import os


def put_message(message, op='APPEND'):
    op = op.upper()
    textbox.config(state=NORMAL)
    if op == 'APPEND':
        textbox.insert(END, message)
        textbox.see(END)
    elif op == 'CLEAR':
        textbox.delete("1.0", END)
    textbox.config(state=DISABLED)


def dnd_handler(event):
    file_list = util.DND.make_file_list(event.data)
    for f in file_list:
        if os.path.isfile(f):     put_message(f'[file     ] {f}\n')
        elif os.path.isdir(f):    put_message(f'[directory] {f}\n')
        else:                     put_message(f'[???      ] {f}\n')


# Const
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200

# Main Window
root = TkinterDnD.Tk()
root.title('Drag and Drop')
# root.geometry(f'{win_width}x{win_height}+500+100')
root.geometry(util.WIN.get_pos_string_on_screen(root, WINDOW_WIDTH, WINDOW_HEIGHT, 'n', 0, 50)[0])
# set icon on the window bar
if util.PLTFORM.is_windows():
    root.iconbitmap(default=util.RSC.get_resource_path('resources\\icon.ico'))

# Drag-and-Drop
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', dnd_handler)

# Widgets
frame = Frame(root)

textbox = Text(frame, width=30, height=10)
textbox.config(state=DISABLED, wrap=NONE)
put_message('Drag and Drop files here.\n\n')

scroll_y = Scrollbar(frame, orient=VERTICAL, command=textbox.yview)
scroll_x = Scrollbar(frame, orient=HORIZONTAL, command=textbox.xview)

textbox.configure(yscrollcommand=scroll_y.set)
textbox.configure(xscrollcommand=scroll_x.set)

# Arrangement
frame.pack(fill=BOTH, expand=TRUE)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.pack(side=BOTTOM, fill=X)
textbox.pack(fill=BOTH, expand=TRUE)

root.mainloop()
