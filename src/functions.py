import os
import re
import xml.etree.ElementTree as ET
from src.ssh_client import make_ssh_client


def get_my_ip():
	return os.popen("hostname -I").read()


def remove_my_ip(connected_ip_list):
	my_ip = get_my_ip().strip(' \n')
	for ip in connected_ip_list:
		if ip == my_ip:
			connected_ip_list.remove(ip)
		else:
			print("not found")
	return connected_ip_list


def get_established_string():
	return filter(None, os.popen("sudo lsof -i -n | egrep '\<ssh\>' | egrep '(ESTABLISHED)'").read())


def get_ip_from_string(ip_string):
	return list(set(remove_my_ip(re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_string))))


def parse_established_string(est_string):
	connection_list = []
	est_list = filter(None, est_string.split('\n'))

	for est_client in est_list:
		client_info_list = filter(None, est_client.split(' '))
		client_ip = get_ip_from_string(client_info_list[8])[0]
		client_port = client_info_list[8].split(':')[2]
		client_username = client_info_list[2]
		client_process_id = client_info_list[1]

		ssh_client = make_ssh_client(client_ip, client_port, client_username, client_process_id)

		connection_list.append(ssh_client)

	return connection_list


def get_connected_clients():
	client_list_string = get_established_string()
	return parse_established_string(client_list_string)


def whitelisting(connected_clients, whitelist):
	blacklist = []
	for client in connected_clients:
		if client.client_ip not in whitelist:
			blacklist.append(client)
	return blacklist


def parse_whitelist(whitelist_path):
	whitelist = []
	black_n_white_file = whitelist_path
	tree = ET.parse(black_n_white_file)
	root = tree.getroot()
	for child in root:
		for client in child.iter('client'):
			if child.tag == 'whitelist':
				whitelist.append(client.text)

	return whitelist


def kill_unknown_client(blacklist):
	for client in blacklist:
		os.popen("kill -9 " + str(client.client_process_id))