#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
import subprocess
bit = os.uname().machine
changes = subprocess.getoutput("git status --porcelain")
if changes:
    os.system("git reset --hard")
    os.system("git clean -fd")
    os.system("git pull")
os.system("chmod 777 *")
if '32' in bit:
    os.system("clear")
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46m32BIT FOUND')
    import RMXX
else:
    os.system("clear")
    print("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mTOOL NOT AVAILABLE FOR 64 BIT DEVICE")
