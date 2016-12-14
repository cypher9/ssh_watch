import time
import curses
from src import functions

BWPATH = "whitelist/whitelist.xml"  # path to the whitelist.xml


def main():

	window = curses.initscr()

	while True:
		time.sleep(1)
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			functions.whitelisting(connected_clients, BWPATH)

		functions.print_status(connected_clients, window)


if __name__ == "__main__":
	main()

