import os
import pickle
import sys
import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list = []


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a = save(NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO)
    pickle.dump(a, f, protocol=2)
    f.close()
    listq = [str(NAME_PRO), str(ADDRESS_PRO), str(
        MOBILE_NO_PRO), str(ROOM_NO_PRO), str(PRICE_PRO)]
    myVars = {'A': NAME_PRO, "B": ADDRESS_PRO,
              "C": MOBILE_NO_PRO, "D": ROOM_NO_PRO, "E": PRICE_PRO}

    fo = open("recipt.txt", "w+")
    for h in range(0, 5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])
    restart_program()


u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
           36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
m = [9]
G = []


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
