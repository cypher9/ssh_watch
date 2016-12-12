import time
from src import functions


def main():
	while True:
		time.sleep(1)
		connected_clients = functions.get_connected_clients()
		if connected_clients:
			print functions.print_status(connected_clients)
			functions.parse_black_n_white()
		else:
			print "no clients connected..."
	

if __name__ == "__main__":
	main()

