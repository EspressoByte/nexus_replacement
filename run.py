from netmiko import ConnectHandler
from datetime import datetime

# Update with your switch details
switch = {
    "device_type": "cisco_nxos",
    "host": "192.168.1.1",  # Change to your switch's IP
    "username": "admin",
    "password": "YourPassword",
    "secret": "YourEnablePassword",  # If needed for enable mode
}

# List of commands to collect data
commands = [
    "show version",
    "show system resources",
    "show module",
    "show inventory",
    "show running-config",
    "show startup-config",
    "show vlan brief",
    "show vlan",
    "show spanning-tree",
    "show interface status",
    "show running-config interface all",
    "show mac address-table",
    "show port-channel summary",
    "show ip route",
    "show ip arp",
    "show cdp neighbors detail",
    "show lldp neighbors detail",
    "show logging last 100",
    "show archive config differences",
    "show system uptime",
    "show vpc",
    "show system redundancy status",
]

# Establish connection
try:
    connection = ConnectHandler(**switch)
    connection.enable()  # Enter enable mode if needed

    # Filename with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"nexus_backup_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write(f"Cisco Nexus Backup - {timestamp}\n")
        file.write("=" * 50 + "\n\n")

        for command in commands:
            output = connection.send_command(command)
            file.write(f"\nCommand: {command}\n")
            file.write("=" * 50 + "\n")
            file.write(output + "\n\n")

    connection.disconnect()
    print(f"Backup completed. Output saved to {filename}")

except Exception as e:
    print(f"Error: {e}")
