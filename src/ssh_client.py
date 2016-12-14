class SSHCLIENT():
	client_ip = ""
	client_port = ""
	client_username = ""
	client_process_id = ""

	def __init__(self, client_ip, client_port, client_username, client_process_id):
		self.client_ip = client_ip
		self.client_port = client_port
		self.client_username = client_username
		self.client_process_id = client_process_id

	def __str__(self):
		return str(self.__dict__)

	def __cmp__(self, other):
		return self.__dict__ == other.__dict__


def make_ssh_client(client_ip, client_port, client_username, client_process_id):
	ssh_client = SSHCLIENT(client_ip, client_port, client_username, client_process_id)
	return ssh_client
