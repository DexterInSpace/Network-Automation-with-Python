## Configure Cisco switch and router (VLANs, trunk, router-on-a-stick) ##

# Import the Netmiko library
import netmiko

# Define a dictionary of connection details for each device
SW1 = {
    "ip": "192.168.10.10",
    "device_type": "cisco_ios",
    "username": "admin1",
    "password": "cisco",
    "secret": "cisco",
    "session_log": "SW1_session.log"
}

R1 = {
    "ip": "192.168.10.1",
    "device_type": "cisco_ios",
    "username": "admin2",
    "password": "networks",
    "secret": "networks",
    "session_log": "R1_session.log"
}

# List of devices to loop through
devices = [SW1, R1]

for device in devices:

    # Use dictionary unpacking (**) to pass key-value pairs from dictionary
    connection = netmiko.ConnectHandler(**device)

    # Enter EXEC mode
    connection.enable()

    # Stores command output
    cli_output = ""

    # If the device is SW1, configure VLANs and the trunk
    if device == SW1:
        cli_output = connection.send_config_set([
            "vlan 99",
            "name Native",
            "vlan 20",
            "name IT",
            "vlan 30",
            "name HR",
            "interface g0/1",
            "switchport trunk native vlan 99",
            "switchport trunk allowed vlan 10,20,30,99"
        ])

    # If the device is R1, configure router-on-a-stick
    elif device == R1:
        cli_output = connection.send_config_set([
            "interface g0/1.20",
            "encapsulation dot1Q 20",
            "ip address 192.168.20.1 255.255.255.128",
            "interface g0/1.30",
            "encapsulation dot1Q 30",
            "ip address 192.168.30.1 255.255.255.192",
            "interface g0/1.99"
        ])


    # Display IOS commands output
    print(cli_output)


    # Close SSH connection
    connection.disconnect()