import time
import curses
from src import functions


def monitor(window):
	while True:
		time.sleep(1)
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			functions.print_status(connected_clients, window)
			functions.parse_black_n_white()
		else:
			window.clear()
			window.addstr(0, 0, "no clients connected...")
			window.refresh()


def main():
	window = curses.initscr()
	curses.wrapper(monitor(window))


if __name__ == "__main__":
	main()

