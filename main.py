"""
This python script finds saved Wi-Fi profile names and their passwords.
For Windows OS only.
"""
import subprocess

data = subprocess.getoutput('netsh wlan show profiles').split('\n')
user_input = ""
print("Enter 'List' to get a list of all the saved Wi-Fi Profile Names.\n"
      "Enter 'Q' to cancel the program.\n"
      "This program will assume any other text entered is a Wi-Fi Profile Name.")
while user_input != 'Q':
    user_input = input(">> ")
    if user_input == 'List':
        wifi_list = [line.split(': ')[-1] for line in data if 'All User Profile' in line]
        print(wifi_list)
    elif user_input == 'Q':
        break
    else:
        x = ['netsh', 'wlan', 'show', 'profile', user_input, 'key=clear']
        try:
            result = subprocess.check_output(x).decode('utf-8').split('\n')
            for i in result:
                if "Key Content" in i:
                    password = i.split(':')[-1][1:]
                    print(f'Name: {user_input}\n'
                          f'Password: {password}')
            user_input = input(">> ")
        except Exception as e:
            print(f"Error:=:[{e}]")
            print("**Help** : Are you sure that's a Wi-Fi Profile Name?")
