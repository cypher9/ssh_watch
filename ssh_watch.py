import time
import curses
from src import functions

BWPATH = "whitelist/whitelist.xml"  # path to the whitelist.xml

KILLSERVER = False  # kill ssh server if suspicious activity is detected
KILLSESSION = True    # kill session of suspicious client


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

