usernames = [
    'jimbo',
    'giltson98',
    'derekf',
    'WhatSup',
    'NicolEye',
    'swei45',
    'BaseInterpreterInterface',
    'BaseStdIn',
    'Command',
    'ExecState',
    'InteractiveConsole',
    'InterpreterInterface',
    'StartServer',
    'bob']
user_in_list = False
while not user_in_list:
    user_username = input("Enter Username: ")
    for username in usernames:
        if user_username == username:
            user_in_list = True
print("Awesome, your in.")
