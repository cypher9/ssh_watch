import os
import re
from src.ssh_client import make_ssh_client, SSHCLIENT


def get_my_ip():
	return os.popen("hostname -I").read()


def remove_my_ip(connected_ip_list):
	my_ip = get_my_ip().strip(' \n')
	for ip in connected_ip_list:
		if ip == my_ip:
			connected_ip_list.remove(ip)
		else:
			print "not found"
	return connected_ip_list


def get_established_string():
	return filter(None, os.popen("sudo lsof -i -n | egrep '\<ssh\>' | egrep '(ESTABLISHED)'").read())


def get_ip_from_string(ip_string):
	return list(set(remove_my_ip(re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip_string))))


def parse_established_string(est_string):
	connection_list = []
	est_list = filter(None, est_string.split('\n'))
	# print est_list

	for est_client in est_list:
		client_info_list = filter(None, est_client.split(' '))
		client_ip = get_ip_from_string(client_info_list[8])[0]
		# print client_ip
		client_port = client_info_list[8].split(':')[2]
		# print client_port
		client_username = client_info_list[2]
		# print client_username
		client_process_id = client_info_list[1]
		# print client_process_id

		ssh_client = make_ssh_client(client_ip, client_port, client_username, client_process_id)
		# print ssh_client
		connection_list.append(ssh_client)

	return connection_list


def get_connected_clients():
	client_list_string = get_established_string()
	return parse_established_string(client_list_string)