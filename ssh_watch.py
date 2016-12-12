from src import functions, ssh_client
import re


def main():
	str_est = functions.get_established()
	print str_est
	connected_ip_list = list(set(functions.remove_my_ip(re.findall( r'[0-9]+(?:\.[0-9]+){3}', str_est))))
	print connected_ip_list
	
	# os.system("wall 'hallo du'")
	

if __name__ == "__main__":
	main()

