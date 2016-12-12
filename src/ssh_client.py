class ssh_client():
	client_ip = ""
	client_port = ""
	client_name = ""
	client_id = ""
	client_process_id = ""
	def __init__(self, client_ip, client_port, client_name, client_id, client_process_id):
		self.client_ip = client_ip
		self.client_port = client_port
		self.client_name = client_name
		self.client_id = client_id
		self.client_process_id = client_process_id
