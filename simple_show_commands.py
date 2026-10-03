## Simple show command script ##

# Import netmiko library
import netmiko
import time

# Establish SSH connection to device
connection = netmiko.ConnectHandler(ip="192.168.10.1",
                                    device_type="cisco_ios",
                                    username="admin",
                                    password="networks",
                                    secret="networks",
                                    session_log="my_session_log.txt") # Captures logs for debugging

# Use connection var to send IOS commands
cmd_output = connection.send_command("show ip interface brief",strip_command=False)

# Print command "show ip interface brief"
print(connection.find_prompt(), cmd_output)

# Close SSH connection
connection.disconnect()

# Ensure the session log is written before script
time.sleep(1)

# Flushes remaining output and closes file
if connection.session_log_file:
    connection.session_log_file.close()
