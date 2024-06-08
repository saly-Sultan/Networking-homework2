import socket
import threading
import json

accounts = {
    'Saly': {'password': 'password1', 'balance': 2500},
    'Linda': {'password': 'password2', 'balance': 3500},
    'Rama': {'password': 'password1', 'balance': 2000}
}

def handle_client(client_socket):
    while True:
        received_data = client_socket.recv(1024).decode('utf-8')
        if not received_data:
            break

        data = json.loads(received_data)
        command = data['command']
        username = data['username']
        password = data['password']

        if username in accounts and accounts[username]['password'] == password:
            if command == 'balance':
                response = {'status': 'success', 'balance': accounts[username]['balance']}
            elif command == 'deposit':
                amount = data['amount']
                accounts[username]['balance'] += amount
                response = {'status': 'success', 'balance': accounts[username]['balance']}
            elif command == 'withdraw':
                amount = data['amount']
                if accounts[username]['balance'] >= amount:
                    accounts[username]['balance'] -= amount
                    response = {'status': 'success', 'balance': accounts[username]['balance']}
                else:
                    response = {'status': 'error', 'message': 'Insufficient funds'}
            else:
                response = {'status': 'error', 'message': 'Invalid command'}
        else:
            response = {'status': 'error', 'message': 'Authentication failed'}

        client_socket.send(json.dumps(response).encode('utf-8'))

    client_socket.close()

def start_server():
    server_ip = '0.0.0.0'
    server_port = 6666

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()

    print(f'Server is listening on {server_ip}:{server_port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()