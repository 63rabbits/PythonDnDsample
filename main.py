# # make App
# pip install tkinterdnd2
# pyinstaller main.py --onefile --noconsole --icon=63rabbits.icns --collect-data tkinterdnd2

from tkinter import *
from tkinterdnd2 import *
import utility63rabbits as util


def dnd_handler(event):
    file_list = util.DND.make_file_list(event.data)
    textbox.config(state=NORMAL)
    textbox.delete("1.0", "end")
    for f in file_list: textbox.insert("end", f + "\n")
    textbox.config(state=DISABLED)


# Const
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

# Main Window
root = TkinterDnD.Tk()
root.title('Drag and Drop')
# root.geometry(f'{win_width}x{win_height}+500+100')
# root.minsize(width=50, height=50)
root.geometry(util.WIN.get_position(root, WINDOW_WIDTH, WINDOW_HEIGHT, 'n', 0, 50)[0])
# root.config(bg='#cccccc')

# Drag-and-Drop
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', dnd_handler)

# Widgets
frame = Frame(root)

textbox = Text(frame, width=30, height=10)
textbox.insert("end", "Drag and Drop files here.\n")
textbox.config(state=DISABLED, wrap=NONE)

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
