import socket
import datetime
import facilities

HOST = 'localhost'
PORT = 50011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024).decode()
    print(data)

    if data == "Password corretta":
        break

    if data == "Tentativi a disposizione terminati. Chiusura della connessione...":
        s.close()
        break

    password = input("Inserisci la password: ")
    s.send(password.encode())

while True:
    testo=s.recv(1024).decode()
    print(testo)
    scelta = input().encode()
    s.send(scelta)
    
    controllo=s.recv(1024).decode()
    if controllo == "Uscita":
        print(controllo)
        s.close()
        break

    if controllo=="C":
        nome=input(s.recv(1024).decode())
        s.send(nome.encode())
        cognome=input(s.recv(1024).decode())
        s.send(cognome.encode())
        pos_lavorativa=input(s.recv(1024).decode())
        s.send(pos_lavorativa.encode())
        data_assunzione=input(s.recv(1024).decode())
        s.send(data_assunzione.encode())
        telefono=input(s.recv(1024).decode())
        s.send(telefono.encode())
        indirizzo_casa=input(s.recv(1024).decode())
        s.send(indirizzo_casa.encode())
        nome_zona=input(s.recv(1024).decode())
        s.send(nome_zona.encode())
        num_clienti=input(s.recv(1024).decode())
        s.send(num_clienti.encode())
        num_uffici=input(s.recv(1024).decode())
        s.send(num_uffici.encode())
        print(s.recv(1024).decode())
    
    if controllo=="R":
        tabella=input(s.recv(1024).decode()+"\n")
        s.send(tabella.encode())
        data = s.recv(1024)
        data_list=facilities.bytes_to_list(data)
        if tabella =="C":
            for i in range(len(data_list[0])):
                key = data_list[0][i]
                print(f"{key}:")
                for j in range(1, len(data_list)):
                    if j==4:
                        value = data_list[j][i].strftime('%d/%m/%Y')
                    else:
                        value = data_list[j][i]
                    print(f"    {value}")
        else:
            for i in range(len(data_list[0])):
                key = data_list[0][i]
                print(f"{key}:")
    
                for j in range(1, len(data_list)):
                    value = data_list[j][i]
                    print(f"    {value}")

    if controllo == "U":
        tabella=input(s.recv(1024).decode()+"\n")
        s.send(tabella.encode())
        id=input(s.recv(1024).decode())
        s.send(id.encode())
        if tabella == "C":
            while True:
                modifica=input(s.recv(1024).decode())
                s.send(modifica.encode())
                if modifica == "U":
                    break
                valore=input(s.recv(1024).decode())
                s.send(valore.encode())

        if tabella == "Z":
            while True:
                modifica=input(s.recv(1024).decode())
                s.send(modifica.encode())
                if modifica == "U":
                    break
                valore=input(s.recv(1024).decode())
                s.send(valore.encode())
        data=s.recv(1024).decode()
        print(data)
    if controllo=="D":
        id=input(s.recv(1024).decode())
        s.send(id.encode())
        data = s.recv(1024).decode()
        print(data)


