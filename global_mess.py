import os
import shutil
import socket
import ipaddress
import getpass

try:
	os.system('pip install nwscan')
except:
	print("")

import nwscan

def message_file():
	netw_adds = []
	hst_names = []

	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	iface = ipaddress.ip_interface(f"{host_ip}/255.255.255.0")
	subnet = str(iface.network)

	focus_user = getpass.getuser()
	mess_dir = "C:\\focus\\localstatus"

	month = input("Enter Month ( In this format: 01 for January ):\n")
	day = input("Enter Day ( In this format: 01 for day 1 ):\n")
	
	os.chdir(f'C:\\users\\{focus_user}\\desktop')
	ip_addresses = os.system(f'nwscan {subnet} -o ips.txt')

	f = open('ips.txt', 'r')

	for x in f.readlines():
		netw_adds.append(x.replace("\n", ""))
		try:
			term_ip = socket.gethostbyaddr(x.replace("\n", ""))
			hst_names.append(term_ip[0])
		except:
			print("Host name not available.")

	f.close()

	try:
		shutil.rmtree(f"C:\\Users\\{focus_user}\\Desktop\\global_message")
	except OSError as e:
		print("Creating global message folder.")

	udskt = f"C:\\users\\{focus_user}\\desktop"
	os.chdir(udskt)

	try:
		os.mkdir('global_message')
	except OSError as e:
		print("Global directory active.")

	global_dir = f"C:\\Users\\{focus_user}\\Desktop\\global_message"

	print("Scanning located addresses for message files")

	for hst in hst_names:

		message_file = None

		file_name = f"MSG{str(month) + str(day)}"
		msg_loc = f"\\\\{hst}\\c\\focus\\localstatus"

		try:
			os.chdir(msg_loc)
			mess_dir = os.listdir()
			for x in mess_dir:
				if file_name in x:
					message_file=x
					print('Message file: ', x, 'added!')
		except OSError as e:
			print('Could not locate message file at path:', msg_loc)

		msg = f"\\\\{hst}\\c\\focus\\localstatus\\{message_file}"

		try:
			shutil.copy2(msg, global_dir, follow_symlinks=True)
		except OSError as e:
			print("Could not copy message file from path:", msg)

	os.chdir(udskt)
	
	shutil.make_archive('global_message', 'zip', 'global_message')

	os.remove(f"C:\\users\\{focus_user}\\desktop\\ips.txt")
	shutil.rmtree('global_message')
        
if __name__ == "__main__":
	message_file()
