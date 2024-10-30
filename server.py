import socket
from DES2 import convertHextoBin, convertBintoHex, convertBintoDec, convertDectoBin, permute, shift_left, xor, initial_perm, exp_d, sbox, final_perm, encrypt, genKey, permut, encryptLongmsg, shift_left, xor, encrypt, genKey, permut, encryptLongmsg, decryptLongmsg, generateRoundKeys

key = "A1B2C3D4E5F60708"

rkb, rk = generateRoundKeys(key)
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]

def serverProg():
    host = '127.0.0.1'
    port = 12345 

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        conn, address = server_socket.accept()
        print(f"Server connected to {address}")

        while True:
            msg = conn.recv(1024)
            if not msg:
                print("No message received, closing connection.")
                break
            
            cipher_text = msg.decode()
            print(f"Received Cipher text from client: {cipher_text}")
            
            plain_text = decryptLongmsg(cipher_text, rkb_rev, rk_rev)
            print(f"Decrypted Plain text: {plain_text}")

            conn.send(plain_text.encode())
            print("Decrypted message sent back to client.")

        conn.close()
        print("Connection closed.")
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        server_socket.close()
        print("Server socket closed.")

if __name__ == '__main__':
    serverProg()
