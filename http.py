import socket


server = "localhost"
port = 8080


def send(request):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)
        client.connect((server, port))
        client.sendall(request.encode())
        response = client.recv(1024).decode()
        client.close()

    except:
        response = "server is offline!!"

    return response


def main():
    while (True):
        request = input("Enter 'GET user_id' or 'POST user_name user_age' to simulate a request:")
        if request == 'q':
            break
        response = send(request)
        print(response)


if __name__ == "__main__":
    main()
        
