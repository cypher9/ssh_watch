from tabulate import tabulate


def tabulate_client_output(connected_clients):
	client_dict_list = []
	for client in connected_clients:
		client_dict_list.append(client.__dict__)
	tab_clients = tabulate(client_dict_list, headers="keys")
	return tab_clients


def print_status(output_strings, window):
	window.clear()
	first = True
	for output in output_strings:
		if first:
			window.addstr(0, 0, output)
			first = False
		else:
			window.addstr(output)
		window.addstr('\n')
		window.addstr('\n')
		window.refresh()