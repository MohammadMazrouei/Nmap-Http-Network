
# Port Scanner (nmap.py)

This Python script is a basic port scanner. It checks for open ports on a given host and can scan specific ports or ranges of ports.

## Features

- Check if a host is online by scanning common ports.
- Scan individual ports or a range of ports.
- Display open ports and the services running on them.

## Prerequisites

- Python 3.x
- Basic knowledge of terminal or command prompt usage.

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory containing `nmap.py`.
3. Run the script with the following command structure:

```bash
python nmap.py <host> [port/port-range]...
```

- `<host>`: The IP address or hostname you want to scan (e.g., `192.168.1.1` or `example.com`).
- `[port/port-range]`: Optional. Specify individual ports (e.g., `80`) or a range of ports (e.g., `20-25`). Multiple ports or ranges can be specified, separated by spaces.

### Examples

- To check if a host is online and scan common ports:

```bash
python nmap.py example.com
```

- To scan specific ports:

```bash
python nmap.py example.com 80 443
```

- To scan a range of ports:

```bash
python nmap.py example.com 20-25
```


# Simple HTTP Server and Client

This guide describes how to use the `server.py` and `http.py` Python scripts to simulate a basic HTTP server and client interaction.

## Features

- **server.py**: Implements a simple HTTP server that can handle basic GET and POST requests.
- **http.py**: Acts as an HTTP client sending requests to the server.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of HTTP requests and client-server architecture.

## Setup and Usage

### Server Setup

1. Open a terminal or command prompt.
2. Navigate to the directory containing `server.py`.
3. Run the server script:
   ```bash
   python server.py
   ```
   This will start the server on localhost and listen for incoming HTTP requests.

### Client Usage

1. Open another terminal or command prompt window.
2. Navigate to the directory containing `http.py`.
3. Run the client script:
   ```bash
   python http.py
   ```
4. Follow the on-screen prompts to send GET or POST requests. You can simulate requests by entering commands as prompted by the script.

### Examples of Client Requests

- To simulate a GET request:
  ```
  Enter 'GET user_id' or 'POST user_name user_age' to simulate a request: GET user1
  ```
- To simulate a POST request:
  ```
  Enter 'GET user_id' or 'POST user_name user_age' to simulate a request: POST John 30
  ```

To stop the server, press `Ctrl+C` in the terminal where the server is running.

