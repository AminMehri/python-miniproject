import os
import time
import shutil
import tempfile
from subprocess import call


'''
orders: ls, exit, cd, pwd, pidhis, mkdir, rm, rm -r, clear, cat, mv, whoami, vi, nano
'''

class Shell():
    def do_pwd(inp):
        if inp == '':
            print(os.getcwd())
        elif inp == '--help':
            print("NAME:")
            print("\tpwd - print name of current/working directory")
            print("DESCRIPTION:")
            print("\tPrint the full filename of the current working directory.\n")
        else:
            print('order is not recognized! \nuse pwd --help')
        
    def do_ls(inp):
        if inp == '':
            for file in os.listdir():
                print(file, end='    ')
            print('')
        elif inp == '--help':
            print("NAME:")
            print("\tls - list directory contents")
            print("DESCRIPTION:")
            print("\tList information about the FILEs (the current directory by default).\n")
        else:
            try:
                for file in os.listdir(inp):
                    print(file, end='    ')
                print('')
            except FileNotFoundError as e:
                print(e)

    def do_clear(inp):
        if inp == '--help':
            print("NAME:")
            print("\tclear - clear the terminal screen\n")
        elif inp == '':
            os.system('clear')
        else:
            print('order is not recognized! \nuse clear --help')

    def do_cd(inp):
        if inp == '--help':
            print("NAME:")
            print("\tchange the current working directory\n")
        elif inp != '':
            try:
                os.chdir(inp)
            except FileNotFoundError as e:
                print(e)
        else:
            print('order is not recognized! \nuse cd --help')

    def do_cat(inp):
        if inp == '--help':
            print("NAME:")
            print("\tcat - concatenate files and print on the standard output")
            print("DESCRIPTION:")
            print("\tConcatenate FILE to standard output.\n")
        elif inp != '':
            try:
                f = open(inp, "r")
                print(f.read())
            except FileNotFoundError as e:
                print(e)
        else:
            print('order is not recognized! \nuse cat --help')

    def do_mkdir(inp):
        if inp == '--help':
            print("NAME:")
            print("\tmkdir - make directories")
            print("DESCRIPTION:")
            print("\tCreate the DIRECTORY(ies), if they do not already exist.\n")
        elif inp != '':
            if os.path.exists(inp):
                print('there is a directory with the same name.')
            else:
                os.mkdir(inp)
        else:
            print('order is not recognized! \nuse mkdir --help')

    def do_mv(inp):
        if inp == '--help':
            print("NAME:")
            print("\tmv - move (rename) files")
            print("DESCRIPTION:")
            print("\tRename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.\n")
        elif inp != '':
            try:
                inp = str(inp).split()
                shutil.move(inp[0], inp[1])
            except IndexError as e:
                print('your order is not right. please see "mv --help"')
        else:
            print('order is not recognized! \nuse mv --help')
    
    def do_rm(inp):
        if inp == '--help':
            print("NAME:")
            print("rm - remove files or directories")
            print("DESCRIPTION:")
            print("This  manual  page documents the GNU version of rm.  rm removes each specified file.  By default, it does not remove directories.\n")
        elif inp[0:2] == '-r':
            shutil.rmtree(inp[3:])
        elif inp != '':
            if os.path.isdir(inp):
                os.rmdir(inp)
            elif os.path.isfile(inp):
                os.remove(inp)
        else:
            print('order is not recognized! \nuse rm --help')

    def do_whoami(inp):
        os.system('whoami')

    def do_exit(inp):
        exit()
    
    def do_vi(inp):
        with tempfile.NamedTemporaryFile() as tf:
            tf.flush()
            call(['vi', inp])
            tf.seek(0)

    def do_nano(inp):
        with tempfile.NamedTemporaryFile() as tf:
            tf.flush()
            call(['nano', inp])
            tf.seek(0)
    
    
    global pcbs
    pcbs = []
    def save_pcb(name, pcb_number):
        t = time.strftime("%H:%M:%S", time.localtime())
        pcbs.append({'name': name, 'number': pcb_number, 'time': t})

    pcb_number = 1

    def do_pidhis(inp):
        if inp == '':
            for pcb in pcbs:
                print(pcb)
        elif inp == '--help':
            print("NAME:")
            print("\tShows the commands used.\n")
        else:
            print('order is not recognized! \nuse pidhis --help')

    while True:
        print("Amin@fedora" + os.getcwd() + ">>", end=' ')
        inp = input()

        if inp[0:3] == 'pwd':
            do_pwd(inp[4:])
            save_pcb('pwd', pcb_number)
            pcb_number += 1
        elif inp[0:2] == 'ls':
            do_ls(inp[3:])
            save_pcb('ls', pcb_number)
            pcb_number += 1
        elif inp[0:5] == 'clear':
            do_clear(inp[6:])
            save_pcb('clear', pcb_number)
            pcb_number += 1
        elif inp[0:2] == 'cd':
            do_cd(inp[3:])
            save_pcb('cd', pcb_number)
            pcb_number += 1
        elif inp[0:3] == 'cat':
            do_cat(inp[4:])
            save_pcb('cat', pcb_number)
            pcb_number += 1
        elif inp[0:5] == 'mkdir':
            do_mkdir(inp[6:])
            save_pcb('mkdir', pcb_number)
            pcb_number += 1
        elif inp[0:2] == 'rm':
            do_rm(inp[3:])
            save_pcb('rm', pcb_number)
            pcb_number += 1
        elif inp[0:2] == 'mv':
            do_mv(inp[3:])
            save_pcb('mv', pcb_number)
            pcb_number += 1
        elif inp[0:6] == 'pidhis':
            do_pidhis(inp[7:])
            save_pcb('pidhis', pcb_number)
            pcb_number += 1
        elif inp[0:4] == 'exit':
            do_exit(inp[5:])
        elif inp[0:6] == 'whoami':
            do_whoami(inp[7:])
            save_pcb('whoami', pcb_number)
            pcb_number += 1
        elif inp[0:2] == 'vi':
            do_vi(inp[3:])
            save_pcb('vi', pcb_number)
            pcb_number += 1
        elif inp[0:4] == 'nano':
            do_nano(inp[5:])
            save_pcb('nano', pcb_number)
            pcb_number += 1
        else:
            print("Unknown syntax")