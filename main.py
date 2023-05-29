from tkinter import *
from tkinter import messagebox

color_bg = 'white'
color_fg = 'black'
menu_bg = 'white'
menu_fg = 'black'

w = Tk()
w.geometry('360x300')
w.title("Quick Notes")
w.wm_resizable(False, False)

def change_appearance(color_bg, color_fg):
    notes['bg'] = color_bg
    notes['fg'] = color_fg

def white_on_black():
    color_bg = 'black'
    color_fg = 'white'
    notes.configure(insertbackground="white")
    change_appearance(color_bg, color_fg)

def default():
    global color_bg, color_fg
    change_appearance(color_bg, color_fg)

def cyan_on_black():
    color_bg = 'black'
    color_fg = 'cyan'
    menuBar['bg'] = 'white'
    notes.configure(insertbackground="white")
    change_appearance(color_bg, color_fg)

def green_on_black():
    color_bg = 'black'
    color_fg = 'green'
    menuBar['bg'] = 'black'
    notes.configure(insertbackground="white")
    change_appearance(color_bg, color_fg)


#   text color menu

def change_color(Name, textcolor):
    notes.tag_configure(f"{Name}", foreground=textcolor)
    try:
        notes.tag_add(f"{Name}", "sel.first", "sel.last")
    except Exception as e:
        pass


def color_yellow():
    Name = "yellow_color"
    textcolor = "yellow"
    change_color(Name, textcolor)

def color_orange():
    Name = "orange_color"
    textcolor = "orange"
    change_color(Name, textcolor)

def color_lime():
    Name = "lime_color"
    textcolor = "lime"
    change_color(Name, textcolor)

#  exit menu
def exit():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to Exit")
    if confirm>0:
        w.destroy()
        return


menuBar = Menu(w, bg=menu_bg, fg=menu_fg)
appearance = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='Appearance', menu = appearance)
appearance.add_command(label= "Default", command=default)
appearance.add_command(label = "White on Black", command = white_on_black)
appearance.add_command(label= "Cyan on Black", command=cyan_on_black)
appearance.add_command(label= "Green on Black", command=green_on_black)

text_color = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Text Color", menu=text_color)
text_color.add_command(label="Yellow", command=color_yellow)
text_color.add_command(label="Orange", command=color_orange)
text_color.add_command(label="Lime", command=color_lime)

exit_option = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Exit", menu=exit_option)
exit_option.add_command(label="Exit", command=exit)

w.config(menu=menuBar)

notes = Text(w, bg=color_bg, fg=color_fg, font="monaco 11")
notes.pack(fill=BOTH)


w.mainloop()
