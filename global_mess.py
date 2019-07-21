import os
import shutil
import socket
import ipaddress
import nwscan
import getpass

def message_file():

	netw_adds = []
	available_ips = []

	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	iface = ipaddress.ip_interface(f"{host_ip}/255.255.255.0")
	subnet = str(iface.network)

	focus_user = getpass.getuser()
	mess_dir = "C:\\focus\\localstatus"

	month = input("Enter the month you would like to get message files for ( In this format: 01 for January ):\n")
	day = input("Enter the day you would like to get message files for ( In this format: 01 for day 1 ):\n")
	
	os.chdir(f'C:\\users\\{focus_user}\\desktop')
	ip_addresses = os.system(f'nwscan {subnet} -o ips.txt')

	f = open('ips.txt', 'r')

	for x in f.readlines():
		netw_adds.append(x.replace("\n", ""))

	f.close()

	try:
		shutil.rmtree(f"C:\\Users\\{focus_user}\\Desktop\\global_message")
	except OSError as e:
		print(e)

	udskt = f"C:\\users\\{focus_user}\\desktop"
	os.chdir(udskt)

	try:
		os.mkdir('global_message')
	except OSError as e:
		print(e)

	global_dir = f"C:\\Users\\{focus_user}\\Desktop\\global_message"	

	for ip in netw_adds:

		message_file = None

		file_name = f"MSG{str(month) + str(day)}"
		msg_loc = f"\\\\{ip}\\c\\focus\\localstatus"

		try:
			os.chdir(msg_loc)
			mess_dir = os.listdir()
			for x in mess_dir:
				if file_name in x:
					message_file=x

		except OSError as e:
			print(e)

		msg = f"\\\\{ip}\\c\\focus\\localstatus\\{message_file}"

		try:
			shutil.copy2(msg, global_dir, follow_symlinks=True)
		except OSError as e:
			print("Could not copy:", e)

	os.chdir(udskt)
	
	shutil.make_archive('global_message', 'zip', 'global_message')

	os.remove(f"C:\\users\\{focus_user}\\desktop\\ips.txt")
	shutil.rmtree('global_message')

if __name__ == "__main__":
	message_file()