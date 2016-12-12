import time
import curses
from src import functions, print_status


def monitor(window):
	while True:
		time.sleep(1)
		output = []
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			output.append(print_status.tabulate_client_output(connected_clients))
			functions.parse_black_n_white()
		else:
			output.append("no clients connected...")

		print_status.print_status(output, window)


def main():
	window = curses.initscr()
	curses.wrapper(monitor(window))


if __name__ == "__main__":
	main()

