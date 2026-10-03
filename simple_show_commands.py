# Simple show command script

# Import netmiko library
import netmiko

# Establish SSH connection to device
connection = netmiko.ConnectHandler(ip="192.168.10.1",
                                    device_type="cisco_ios",
                                    username="admin",
                                    password="networks",
                                    secret="networks",)

# Use connection var to send IOS commands
cmd_output = connection.send_command("show ip interface brief",strip_command=False)

# Print command "show ip interface brief"
print(connection.find_prompt(), cmd_output)

# Close SSH connection
connection.disconnect()
