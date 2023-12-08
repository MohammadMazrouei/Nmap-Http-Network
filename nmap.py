import socket
import sys


def check_port_range(host: str, start_port: int, end_port: int) -> dict:
    open_ports = {}
    for port in range(start_port, end_port + 1):
        service = check_port(host, port)
        if service:
            open_ports[port] = service 

    return open_ports


def check_port(host: str, port: int) -> str:
    service = ""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set the timeout to 5 seconds
        s.settimeout(5)

        # Try to connect to the host
        s.connect((host, port))

        # Get the service name
        service = socket.getservbyport(port)

        # Close the socket
        s.close()

    except:
       return service

    return service 


if __name__ == '__main__':

    host = sys.argv[1]

    # check port 80 for host is online
    if check_port(host, 80)[0]:
        print(f'{host} is online')
    else:
        print(f'{host} is offline')

    if (len(sys.argv) > 2):
        print('open port detected:')
    for i in range(2, len(sys.argv)):

        port = sys.argv[i]
        open_ports = dict()

        if '-' in port:
            start_port, end_port = map(int, port.split('-'))
            open_ports = check_port_range(host, start_port, end_port)
        else:
            service = check_port(host, int(port))
            if service:
                open_ports[port] = service

        for port, service in open_ports.items():
            print(f'Port: {port}    Service: {service}')

