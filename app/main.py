# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    sock = socket.create_server(("localhost", 6379), reuse_port=True)
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(("localhost", 6379))
    host , port  = sock.accept()
    host.recv(1024)
    host.send(b"+PONG\r\n")


   


if __name__ == "__main__":
    main()
