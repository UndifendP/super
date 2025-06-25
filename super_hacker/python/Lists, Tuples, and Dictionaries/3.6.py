ports_serice_dict ={'20': 'ftp', '21': 'ftp', '22': 'ssh', '23': 'telnet', '25': 'smtp', '53': 'dns', '67': 'dhcp','443': 'https', '80':'http'}
selected_port = input("Enter a port: ")
print("Port: ", selected_port, "=> service name: ",ports_serice_dict[selected_port])
