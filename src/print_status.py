from tabulate import tabulate


def tabulate_client_output(connected_clients):
	tab_clients = tabulate(connected_clients, headers="keys")
	return tab_clients


def print_status(output_strings, window):
	for output in output_strings:
		window.clear()
		window.addstr(0, 0, output)
		window.addstr('\n')
		window.refresh()