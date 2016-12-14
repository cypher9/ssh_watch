import time
import curses
from src import functions

BWPATH = "whitelist/whitelist.xml"  # path to the whitelist.xml


def main():

	window = curses.initscr()
	old_connection_list = [1, 1]

	while True:
		time.sleep(1)
		connected_clients = functions.get_connected_clients()
		new_connection_list = connected_clients
		if functions.get_hash(new_connection_list) != functions.get_hash(old_connection_list):
			functions.whitelisting(connected_clients, BWPATH)

			old_connection_list = new_connection_list
			functions.print_status(connected_clients, window)


if __name__ == "__main__":
	main()

