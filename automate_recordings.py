import os
import keyboard
import shutil


data_dump = ""
recorder_path = ""
projects1 = ""


def record_move():
    os.chdir(recorder_path)
    os.system('sudo ./recorder')#Using module keyboard
    recorded = keyboard.record(until='esc')
    os.chdir(data_dump)
    os.system('sudo mv dw* ' + projects1)

def make_folders():
    os.chdir(projects1)
    usernum = range(1,11)
    for user in usernum:
        os.mkdir('user' + str(user))

def user_move():
    count = 1
    for user in os.listdir(projects1):
        if user.startswith('dw'):
            while len(os.listdir(projects1 + 'user' + str(count))) < 11:
                shutil.move(projects1 + user, projects1 + 'user' + str(count))
            count += 1


#record_move()
#make_folders()
user_move()




