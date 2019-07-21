import os
import shutil
import socket

def message_file():

	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print(host_name, ":", host_ip)

	focus_user = input("Enter your focus user account:\n")
	mess_dir = "C:\\focus\\localstatus"

	try:
		shutil.rmtree(f"C:\\Users\\{focus_user}\\Desktop\\global_message")
	except OSError as e:
		print(e)

	udskt = f"C:\\users\\{focus_user}\\desktop"

	os.chdir("C:\\focus\\localstatus")

	for x in os.listdir():
		print(x)

	month = input("Enter the month you would like to get message files for ( In this format: 01 for January ):\n")
	day = input("Enter the day you would like to get message files for ( In this format: 01 for day 1 ):\n")
	

	file_name = f"MSG{str(month) + str(day)}-001"

	print("Selected file:", file_name)

	msg = f"C:\\focus\\localstatus\\{file_name}"
	print(msg)
	os.chdir(udskt)

	try:
		os.mkdir('global_message')
	except OSError as e:
		print(e)

	global_dir = f"C:\\Users\\{focus_user}\\Desktop\\global_message"

	shutil.copy2(msg, global_dir, follow_symlinks=True)

if __name__ == "__main__":
	message_file()