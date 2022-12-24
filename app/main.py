# Uncomment this to pass the first stage
import socket
import threading

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    sock = socket.create_server(("localhost", 6379), reuse_port=True)
    def holder(host):
        while True:
            try:
                host.recv(1024)
                host.send(b"+PONG\r\n")
            except ConnectionError:
                break;


    while True:
        host , port  = sock.accept()
        threading.Thread(target=holder, args=(host,)).start()
   
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(("localhost", 6379))
    


   


if __name__ == "__main__":
    main()
