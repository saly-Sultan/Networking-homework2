import socket
import json

def bank_client():
    server_ip = '127.0.0.3'
    server_port = 6666

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # User authentication
    username = input('Enter username: ')
    password = input('Enter password: ')

    # Banking operations
    while True:
        command = input('Enter command (balance/deposit/withdraw/exit): ')
        if command in ['deposit', 'withdraw']:
            amount = float(input('Enter amount: '))
        else:
            amount = 0

        # Send command to the server
        data = {
            'command': command,
            'username': username,
            'password': password,
            'amount': amount
        }
        client_socket.send(json.dumps(data).encode('utf-8'))

        # Receive response from the server
        response = json.loads(client_socket.recv(1024).decode('utf-8'))
        if response['status'] == 'success':
            print(f"Balance: {response['balance']}")
        else:
            print(f"Error: {response['message']}")

        if command == 'exit':
            break

    client_socket.close()

if __name__ == '__main__':
    bank_client()