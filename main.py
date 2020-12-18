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


def click_checkinn():
    call(["python", "checkin.py"])


def click_list():
    call(["python", "list.py"])


def click_checkout():
    call(["python", "checkout.py"])


def click_getinfo():
    call(["python", "getinfo.py"])
