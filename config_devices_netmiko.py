## Configure Cisco routers and switches ##

# Import netmiko library
import netmiko
import time

# Establish SSH connection to device
connection = netmiko.ConnectHandler(ip="192.168.10.1",
                                    device_type="cisco_ios",
                                    username="admin",
                                    password="networks",
                                    secret="networks",
                                    session_log="my_session_log_2.txt") # Captures logs for debugging

# Defines list of interface config commands
interface_description_list = [
    "interface FastEthernet 0/1",
    "description LAN interface - used Netmiko",
    "exit",

    "interface FastEthernet 0/2",
    "description Unused interface - used Netmiko",
    "exit"
]

# Enter EXEC mode
connection.enable()



# Apply list of config commands
connection.send_config_set(interface_description_list)

# Display IOS command
print("\nIOS command:"
      "show running-config | begin interface FastEthernet0/1")
print(connection.send_command(
    "show running-config | begin interface FastEthernet0/1"))

# Close SSH connection
connection.disconnect()

# Ensure the session log is written before script
time.sleep(1)

# Flushes remaining output and closes file
if connection.session_log:
    connection.session_log.close()
