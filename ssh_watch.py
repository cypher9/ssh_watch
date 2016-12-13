import time
import curses
from src import functions, print_status

LOGPATH = ""  # path to save the LOG files
BWPATH = "black_n_white/black_n_white.xml"  # path to the black_n_white.xml

WHITELIST = True    # True for whitelisting, False for blacklisting

KILLSWITCH = False  # kill ssh server if suspicious activity is detected
KICKALIEN = True    # kill session of suspicious client




def monitor(window):
	while True:
		time.sleep(1)
		output = []
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			output.append(print_status.tabulate_client_output(connected_clients))
			if WHITELIST:
				white_list = functions.parse_whitelist(BWPATH)
				found = functions.whitelisting(connected_clients, white_list)
				if found:
					output.append("i found the ip")
		else:
			output.append("no clients connected...")

		print_status.print_status(output, window)


def main():
	window = curses.initscr()
	curses.wrapper(monitor(window))


if __name__ == "__main__":
	main()

