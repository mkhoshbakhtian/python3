from Tkinter import *
import Tkinter as tk
import tkMessageBox as messagebox

root = Tk()

topframe = Frame(root)
mainframe = Frame(root)
botframe = Frame(root)

topframe.pack()
mainframe.pack()
botframe.pack()

thelabel = Label(topframe, text='Gas Purification Calculation')
thelabel.pack(side=TOP)


def donothing():
    print('nothink')


# ************   MENU  *************
mainmenu = Menu(topframe)
root.config(menu=mainmenu)

submenu = Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label='New', command=donothing)
submenu.add_command(label='Save', command=donothing)
submenu.add_command(label='Print', command=donothing)
submenu.add_separator()
submenu.add_command(label='Quit', command=topframe.quit)

helpmenu = Menu(mainmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label='Description', command=donothing)
helpmenu.add_command(label='Assumptons', command=donothing)
helpmenu.add_command(label='Cnotact Info.', command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label='About', command=topframe.quit)

# ************   Toolbar
toolbar = Frame(topframe, bg='dark green')
BTUButt = Button(toolbar, text='GP', command=donothing)
BTUButt.pack(side=LEFT)
SIButt = Button(toolbar, text='EO', command=donothing)
SIButt.pack(side=RIGHT)
toolbar.pack(side=TOP, fill=X)

# ***********   Status Bar
status = Label(root, text='By M_Kh @2018', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


def Dry():
    Concentration = float(entry_Concentration.get())
    Concentration_H20 = float(entry_water.get())
    Concentration_O2 = float(entry_O2.get())
    Concentration_O2_ref = float(entry_O2_ref.get())
    DryConc = Concentration/(1-(Concentration_H20/100))
    Dry_O2 = Concentration_O2/(1-(Concentration_H20/100))
    Dry_ref_Conc = DryConc *((21-Concentration_O2_ref)/(21-Dry_O2))
    return round(Dry_ref_Conc , 3)


def dry_display():
    heat = Dry()
    heat_display = Entry(mainframe)
    heat_display.grid(column=1, row=8)
    heat_display.insert(tk.END, heat)


def cond_display():
    heat = cond_gen()
    heat_display = Entry(mainframe)
    heat_display.grid(column=1, row=8)
    heat_display.insert(tk.END, heat)


def inputmessage():
    messagebox.showwarning('Wrong data entry!', 'Please inter Numbers!')
    if quitmessage() == 'yes':
        quit()
    if quitmessage() == 'no':
        print('Test')


def quitmessage():
    answer = messagebox.askokcancel('Exit!', 'Are you sure?!')
    if answer == TRUE:
        quit()


def clear_text():

    entry_Concentration.delete(0, 'end')
    entry_water.delete(0, 'end')
    entry_O2.delete(0, 'end')
    entry_O2_ref.delete(0, 'end')
    entry_result.delete(0, 'end')


# ------------       BUTTONS  ---------
butdry = Button (mainframe, text='Calculate!', command=dry_display )
butreset = Button (mainframe, text='Reset', command=clear_text)
quitbut = Button (mainframe, text='Quit', command=quitmessage)

butdry.grid(row=9, column=0)
butreset.grid(row=9, column=1)
quitbut.grid(row=9, column=3)

# ---------------         LABELS  ----------
water = Label(mainframe, text='Enter % H2O ')
conc = Label(mainframe, text='Enter Wet Gas %Conc.')
O2 = Label(mainframe, text='Enter Current %O2')
O2_ref = Label(mainframe, text='Enter Reference O2')

result = Label(mainframe, text='Dry O2 Referenced Gas Concentration Is:')


entry_water = Entry(mainframe)
entry_Concentration = Entry(mainframe)
entry_O2 = Entry(mainframe)
entry_O2_ref = Entry(mainframe)
entry_result = Entry(mainframe, highlightbackground="green")


water.grid(row=1, column=0, sticky=W)
conc.grid(row=2, column=0, sticky=W)
O2.grid(row=3, column=0, sticky=W)
O2_ref.grid(row=4, column=0, sticky=W)
result.grid(row=8, column=0, sticky=W)


entry_water.grid(row=1, column=1)
entry_Concentration.grid(row=2, column=1)
entry_O2.grid(row=3, column=1)
entry_O2_ref.grid(row=4, column=1)
entry_result.grid(row=8, column=1)


root.mainloop()

