import os
import re
from src import ssh_client


def get_my_ip():
	return os.popen("hostname -I").read()


def remove_my_ip(connected_ip_list):
	my_ip = get_my_ip().strip(' \n')
	for ip in connected_ip_list:
		if ip == my_ip:
			connected_ip_list.remove(ip)
			print "found and removed"
		else:
			print "not found"
	return connected_ip_list


def get_established_string():
	return filter(None, os.popen("sudo lsof -i -n | egrep '\<ssh\>' | egrep '(ESTABLISHED)'").read())


def parse_established_string(est_string):
	connection_list = []

	return connection_list


def get_connected_ip():
	return list(set(remove_my_ip(re.findall( r'[0-9]+(?:\.[0-9]+){3}', str_est))))


def get_connected_clients():
	client_list_string = get_established_string()