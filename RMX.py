import platform
import os
import socket
import subprocess
arc = None
print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mECHECKING FOR UPDATED ')
os.system('git pull --quiet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        os.system('chmod 777 RMX32 ;./RMX32')
        print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46m32BIT DETECTED')
        print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSTARTING RMX ')
        os.system('./RMX32')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        os.system('chmod 777 RMX64 ;./RMX64')
        print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46m64BIT DETECTED')
        print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSTARTING RMX')
        os.system('./RMX64')
    else:
        arc = "INVALID"
        exit("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;91mUNKNOWN DEVICE TYPE")

if __name__ == "__main__":
    main()
