from Tkinter import *
import Tkinter as tk
import tkMessageBox as messagebox
from math import log


root = Tk()

topframe = Frame(root)
mainframe = Frame(root)
botframe = Frame(root)

topframe.pack()
mainframe.pack()
botframe.pack()

thelabel = Label(topframe, text='Heat Exchanger Cost Estimation widget')
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
BTUButt = Button(toolbar, text='BTU', command=donothing)
BTUButt.pack(side=LEFT)
SIButt = Button(toolbar, text='SI', command=donothing)
SIButt.pack(side=RIGHT)
toolbar.pack(side=TOP, fill=X)

# ***********   Status Bar
status = Label(root, text='Please Fill in the Fields...', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


def main_cost():
    THOUT = float(entry_THOUT.get())
    THIN = float(entry_THIN .get())
    TCIN = float(entry_TCIN.get())
    TCOUT = float(entry_TCOUT.get())
    U = float(entry_U.get())
    mcphot = float(entry_mcphot.get())
    mcpcold = float(entry_mcpcold.get())
    Deltamin = float(entry_Deltamin.get())
    NewTHout = THOUT + Deltamin
    TCOUTcalculated = TCIN + (THIN - NewTHout)*(mcphot/mcpcold)
    DeltaT1 = THIN - TCOUTcalculated
    DeltaT2 = NewTHout - TCIN
    deltalm_EX = (DeltaT1 - DeltaT2) / (log(DeltaT1/DeltaT2)+0.001)
    Qex = (THIN - NewTHout) * mcphot
    Areaex = Qex /(U*deltalm_EX+1)
    Cost_EX = 40000 + 180000 * Areaex ** 0.6

    return round(Cost_EX, 3)


def steam_cost():

    SteamTemp  = float(entry_SteamTemp.get())
    THIN = float(entry_THIN .get())
    THOUT = float(entry_THOUT.get())
    TCOUT = float(entry_TCOUT.get())
    TCIN = float(entry_TCIN.get())
    U = float(entry_U.get())
    mcpcold = float(entry_mcpcold.get())
    mcphot = float(entry_mcphot.get())
    steamcost = float(entry_steamcost.get())
    Period = float(entry_Period.get())
    Deltamin = float(entry_Deltamin.get())
    NewTHout = THOUT + Deltamin
    TCOUTcalculated = TCIN + (THIN - NewTHout)*(mcphot/mcpcold)
    DeltaT1 = SteamTemp - TCOUTcalculated
    DeltaT2 = SteamTemp - TCOUT
    deltalm_EX = (DeltaT1 - DeltaT2) / log(DeltaT1 / DeltaT2)
    Qsteam = (TCOUT - TCOUTcalculated) * mcpcold
    Areaex = abs(Qsteam / (U * deltalm_EX))
    Cost_st = (Qsteam * steamcost * Period) + (40000 + 180000 * Areaex ** 0.6)
    return round(Cost_st, 3)


def cw_cost():
    CWTemp = float(entry_CWTemp.get())
    THOUT = float(entry_THOUT.get())
    U = float(entry_U.get())
    mcphot = float(entry_mcphot.get())
    CWcost = float(entry_CWcost.get())
    Period = float(entry_Period.get())
    Deltamin = float(entry_Deltamin.get())
    NewTHout = THOUT + Deltamin
    DeltaT1 = NewTHout - CWTemp
    DeltaT2 = THOUT - CWTemp
    deltalm_EX = (DeltaT1 - DeltaT2) / log(DeltaT1 / DeltaT2)
    Qcw = (NewTHout - THOUT ) * mcphot
    Areaex = Qcw / (U * deltalm_EX)
    Cost_CW = (Qcw * CWcost * Period) + (40000 + 180000 * Areaex ** 0.6)
    return round(Cost_CW, 3)


def tot_gen():
    qtot = cw_cost()+steam_cost()+main_cost()
    return round(qtot, 3)


def main_display():
    cost = main_cost()
    cost_display = Entry(mainframe)
    cost_display.grid(column=1, row=18)
    cost_display.insert(tk.END, cost )


def cond_display():
    cost = steam_cost()
    cost_display = Entry(mainframe)
    cost_display.grid(column=1, row=18)
    cost_display.insert(tk.END, cost )


def rad_display():
    cost = cw_cost()
    cost_display = Entry(mainframe)
    cost_display.grid(column=1, row=18)
    cost_display.insert(tk.END, cost )


def tot_display():
    cost = tot_gen()
    cost_display = Entry(mainframe)
    cost_display.grid(column=1, row=18)
    cost_display.insert(tk.END, cost )


def inputmessage():
    messagebox.showwarning('Wrong data entry!', 'Please inter Integers!')
    if quitmessage() == 'yes':
        quit()
    if quitmessage() == 'no':
        print('cancle')


def quitmessage():
    answer = messagebox.askokcancel('Exit!', 'Are you sure?!')
    if answer == TRUE:
        quit()


def clear_text():
    entry_THOUT.delete(0, 'end')
    entry_THIN.delete(0, 'end')
    entry_TCIN.delete(0, 'end')
    entry_U.delete(0, 'end')
    entry_mcpcold.delete(0, 'end')
    entry_mcphot.delete(0, 'end')
    entry_steamcost.delete(0, 'end')
    entry_SteamTemp.delete(0, 'end')
    entry_CWTemp.delete(0, 'end')
    entry_CWcost.delete(0, 'end')
    entry_Period.delete(0, 'end')
    entry_TCOUT.delete(0, 'end')
    entry_Deltamin.delete(0, 'end')
    entry_result.delete(0, 'end')


# ------------       BUTTONS  ---------
butconv = Button (mainframe, text='Main Ex Cost [Kr.]', command=main_display )
butcond = Button (mainframe, text='Steam Cost [Kr.]', command=cond_display )
butrad = Button (mainframe, text='Cooling Water Cost [Kr.]', command=rad_display)
butreset = Button (mainframe, text='Reset', command=clear_text)
buttotal = Button (mainframe, text='Total', command=tot_display)
quitbut = Button (mainframe, text='Quit', command=quitmessage)

butconv.grid(row=2, column=3)
butcond.grid(row=3, column=3)
butrad.grid(row=4, column=3)
butreset.grid(row=14, column=2)
buttotal.grid(row=13, column=3)
quitbut.grid(row=14, column=3)

# ---------------         LABELS  ----------
THIN = Label(mainframe, text='Hot In Temperature [C]')
THOUT = Label(mainframe, text='Hot Out Temperature [C]')
TCIN = Label(mainframe, text='Cold In Temperature [C]')
TCOUT = Label(mainframe, text='Cold Out Temperature [C]')
U = Label(mainframe, text='Heat Transfer Coef. U[kw/m2C]')
mcpcold = Label(mainframe, text='mcp cold stream [kw/c]')
mcphot = Label(mainframe, text='mcp hot stream [kw/c]')
SteamTemp = Label(mainframe, text='Steam Temperature [C]')
Steamcost = Label(mainframe, text='Steam Cost [Kroner/kwh]')
CWTemp = Label(mainframe, text='Cooling Water Temperature [C]')
CWcost = Label(mainframe, text='Cooling water Cost [Kroner/kwh]')
Period = Label(mainframe, text='Operation Period [hr]')
Deltamin = Label(mainframe, text='Delta T min [C]')
result = Label(mainframe, text='Total Cost [Kr.]')


entry_THIN = Entry(mainframe)
entry_THOUT = Entry(mainframe)
entry_TCIN = Entry(mainframe)
entry_TCOUT = Entry(mainframe)
entry_U = Entry(mainframe)
entry_mcpcold = Entry(mainframe)
entry_mcphot = Entry(mainframe)
entry_SteamTemp = Entry(mainframe)
entry_steamcost = Entry(mainframe)
entry_CWTemp = Entry(mainframe)
entry_CWcost = Entry(mainframe)
entry_Period = Entry(mainframe)
entry_Deltamin = Entry(mainframe)
entry_result = Entry(mainframe, background="green")


THIN.grid(row=1, column=0, sticky=W)
THOUT.grid(row=2, column=0, sticky=W)
TCIN.grid(row=3, column=0, sticky=W)
TCOUT.grid(row=4, column=0, sticky=W)
U.grid(row=5, column=0, sticky=W)
mcpcold.grid(row=6, column=0, sticky=W)
mcphot.grid(row=7, column=0, sticky=W)
SteamTemp.grid(row=9, column=0, sticky=W)
Steamcost.grid(row=10, column=0, sticky=W)
CWTemp.grid(row=11, column=0, sticky=W)
CWcost.grid(row=12, column=0, sticky=W)
Period.grid(row=13, column=0, sticky=W)
Deltamin.grid(row=14, column=0, sticky=W)
result.grid(row=18, column=0, sticky=W)


entry_THIN.grid(row=1, column=1)
entry_THOUT.grid(row=2, column=1)
entry_TCIN.grid(row=3, column=1)
entry_TCOUT.grid(row=4, column=1)
entry_U.grid(row=5, column=1)
entry_mcpcold.grid(row=6, column=1)
entry_mcphot.grid(row=7, column=1)
entry_SteamTemp.grid(row=9, column=1)
entry_steamcost.grid(row=10, column=1)
entry_CWTemp.grid(row=11, column=1)
entry_CWcost.grid(row=12, column=1)
entry_Period.grid(row=13, column=1)
entry_Deltamin.grid(row=14, column=1)
entry_result.grid(row=18, column=1)


root.mainloop()

