import time
from src import functions


def main():
	while True:
		time.sleep(1)
		print functions.get_connected_clients()
		functions.parse_black_n_white()
		break
	

if __name__ == "__main__":
	main()

