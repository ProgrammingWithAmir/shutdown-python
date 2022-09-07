"""
    Shutdown program using Python
"""
# importing modules
import os
import platform


def shutdown():
	# identifying os
    if platform.system() == "Windows":
    	# shutdown command on windows
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
    	# shutdown command on linux and mac os
        os.system("shutdown -h now")
    else:
        print("Os not supported!")


command = input("Do you really want to shutdown? (y/n): ").lower()

if command == 'y':
	print('run')


