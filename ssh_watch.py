import time
import curses
from src import functions, print_status

LOGPATH = ""  # path to save the LOG files
BWPATH = "whitelist/whitelist.xml"  # path to the whitelist.xml

WHITELIST = True    # True for whitelisting, False for blacklisting

KILLSERVER = False  # kill ssh server if suspicious activity is detected
KILLSESSION = True    # kill session of suspicious client


def monitor(window):
	while True:
		time.sleep(1)
		output = []
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			output.append(print_status.tabulate_client_output(connected_clients))
			if WHITELIST:
				white_list = functions.parse_whitelist(BWPATH)
				blacklist = functions.whitelisting(connected_clients, white_list)
				if blacklist:
					output.insert(len(output), "unknown IP is connected to SSH Server")
					functions.kill_unknown_client(blacklist)
					for client in blacklist:
						output.insert(len(output), "killed session of: " + client.client_ip)

		else:
			output.append("no clients connected...")

		print_status.print_status(output, window)


def main():
	window = curses.initscr()
	curses.wrapper(monitor(window))


if __name__ == "__main__":
	main()

