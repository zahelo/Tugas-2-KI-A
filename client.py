import socket
import random
from DES2 import convertHextoBin, convertBintoHex, convertBintoDec, convertDectoBin, permute, shift_left, xor, initial_perm, exp_d, sbox, final_perm, encrypt, genKey, permut, encryptLongmsg, shift_left, xor, encrypt, genKey, permut, encryptLongmsg, decryptLongmsg, generateRoundKeys

# Key known to both server and client
key = "A1B2C3D4E5F60708"

# Generate round keys for encryption
rkb, rk = generateRoundKeys(key)

def clientProg():
    host = '127.0.0.1'
    port = 12345

    try:
        client_socket = socket.socket()
        client_socket.connect((host, port))
        print("Connected to server")

        msg = input("Enter message: ")
        encrypted_message = encryptLongmsg(msg, rkb, rk)
        print(f"Encrypted message to send: {encrypted_message}")

        client_socket.sendall(encrypted_message.encode())
        print("Encrypted message sent to server.")

        decrypted_text = client_socket.recv(1024).decode()
        print("Decrypted Text from Server:", decrypted_text)

        client_socket.close()
        print("Client socket closed.")
    except KeyboardInterrupt:
        print("\nClient stopped by user.")
    finally:
        client_socket.close()

if __name__ == '__main__':
    clientProg()
