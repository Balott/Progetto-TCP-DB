import threading 
import socket
import mysql.connector
import facilities

PASSWORD = "CIAO"

def connessione_server():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="tepsit",
        port=3306,
    )
    return conn

def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    cont = 0
    while data != PASSWORD:
        cont = cont + 1
        if cont == 3:
            conn.send("Tentativi a disposizione terminati. Chiusura della connessione...".encode())
            conn.close()
            return
        conn.send("Password ERRATA, reinserisci password: ".encode())
        data = conn.recv(1024).decode()

    conn.send("Password corretta".encode())

    while True:
        conn.send("Opzioni disponibili:\nC - Creare nuovi dipendenti e nuove zone associate ai dipendenti tramite l'ID\nR - Leggere dati relativi a zone e/o dipendenti\nU - Modificare le anagrafiche dei dipendenti o delle zone\nD - Cancellare dati relativi a dipendenti e/o zone\nE - Uscita\nFai una scelta: ".encode())
        scelta = conn.recv(1024).decode()

        if scelta == "C":
            conn.send("C".encode())
            testo=db_create(conn)
            conn.send(testo.encode())
        elif scelta == "R":
            conn.send("R".encode())
            conn.send("Selezionare la tabella desiderata: \nC - Clienti\nZ - Zone di lavoro".encode())
            tabella=conn.recv(1024).decode()
            dati = db_get(tabella)
            dati_bytes=facilities.list_to_bytes(dati)
            conn.send(dati_bytes)
        elif scelta == "U":
            conn.send("U".encode())
            conn.send("Selezionare la tabella desiderata: \nC - Clienti\nZ - Zone di lavoro".encode())
            tabella=conn.recv(1024).decode()
            conn.send("Inserire l'id presente in un record da modificare: ".encode())
            id=conn.recv(1024).decode()
            modifica=db_update(tabella, id, conn)
            conn.send(modifica.encode())
        elif scelta == "D":
            conn.send("D".encode())
            conn.send("Inserire l'id presente in una riga da eliminare: ".encode())
            id=conn.recv(1024).decode()
            cancellazione=db_delete(id)
            conn.send(cancellazione.encode())
        elif scelta == "E":
            conn.send("Uscita".encode())
            conn.close()
            return

def db_create(conn):
    conn.send("Inserire il nome del nuovo record: ".encode())
    nome=conn.recv(1024).decode()
    conn.send("Inserire il cognome del nuovo record: ".encode())
    cognome=conn.recv(1024).decode()
    conn.send("Inserire la posizione lavorativa del nuovo record: ".encode())
    pos_lavorativa=conn.recv(1024).decode()
    conn.send("Inserire la data di assunzione del nuovo record: ".encode())
    data_assunzione=conn.recv(1024).decode()
    conn.send("Inserire il telefono del nuovo record: ".encode())
    telefono=conn.recv(1024).decode()
    conn.send("Inserire l'indirizzo di casa del nuovo record: ".encode())
    indirizzo_casa=conn.recv(1024).decode()
    conn.send("Inserire il nome della zona del nuovo record: ".encode())
    nome_zona=conn.recv(1024).decode()
    conn.send("Inserire il numero dei clienti del nuovo record: ".encode())
    num_clienti=conn.recv(1024).decode()
    conn.send("Inserire il numero di uffici del nuovo record: ".encode())
    num_uffici=conn.recv(1024).decode()

    conn = connessione_server()

    cur = conn.cursor()
    

    query= "INSERT INTO clienti_francesco_balotta (nome, cognome, pos_lavorativa, data_assunzione, telefono, indirizzo_casa) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nome, cognome, pos_lavorativa, data_assunzione, telefono, indirizzo_casa)
    cur.execute(query, values)
    conn.commit()

    query3 = "SELECT * FROM clienti_francesco_balotta WHERE nome = %s"
    cur.execute(query3, (nome,))
    dati = cur.fetchall()
    #print(dati)
    

    query2 = "INSERT INTO zone_di_lavoro_francesco_balotta (nome_zona, num_clienti, id_dipendente, num_uffici) VALUES (%s, %s, %s, %s)"
    values2 = (nome_zona, num_clienti,dati[0][0], num_uffici)
    cur.execute(query2, values2)
    conn.commit()

    return "Dati inseriti correttamente"

def db_get(scelta):
    conn = connessione_server()

    cur = conn.cursor()


    if scelta == "C":
        query = "SELECT * FROM clienti_francesco_balotta"
        query2 = f"SHOW COLUMNS FROM clienti_francesco_balotta"

    if scelta == "Z":
        query = "SELECT * FROM zone_di_lavoro_francesco_balotta"
        query2 = f"SHOW COLUMNS FROM zone_di_lavoro_francesco_balotta"
    cur.execute(query)
    dati = cur.fetchall()
    cur.execute(query2)
    dati_attributi=cur.fetchall()
    nomi_attributi=[]
    for riga in dati_attributi:
        nomi_attributi.append(riga[0])
    dati.insert(0, nomi_attributi)
    print(dati)
    return dati

def db_update(tabella, id, connessione):
    conn = connessione_server()

    cur = conn.cursor()

    if tabella == "C":
        while True:
            connessione.send("Selezionare il dato da modificare: \nnome\ncognome\npos_lavorativa\ndata_assunzione\ntelefono\nindirizzo_casa\nU - Uscire dalla modifica\n".encode())
            modifica=connessione.recv(1024).decode()
            if modifica == "U":
                break
            connessione.send("Inserire il nuovo valore: ".encode())
            valore=connessione.recv(1024).decode()
            query = f"UPDATE clienti_francesco_balotta SET {modifica} = %s WHERE id = %s"
            values = (valore, id)
            cur.execute(query, values)
            conn.commit()

    if tabella == "Z":
        while True:
            connessione.send("Selezionare il dato da modificare: \nnome_zona\nnum_clienti\nnum_uffici\nU - Uscire dalla modifica\n".encode())
            modifica=connessione.recv(1024).decode()
            if modifica == "U":
                break
            connessione.send("Inserire il nuovo valore: ".encode())
            valore=connessione.recv(1024).decode()
            query = f"UPDATE zone_di_lavoro_francesco_balotta SET {modifica} = %s WHERE id_zona = %s"
            values = (valore, id)
            cur.execute(query, values)
            conn.commit()
        
    return "I dati inerenti agli input forniti sono stati modificati"

def db_delete(id):
    conn = connessione_server()

    cur = conn.cursor()

    query = "DELETE FROM zone_di_lavoro_francesco_balotta where id_dipendente='%s' " % id
    print(query)
    cur.execute(query)
    conn.commit()

    query = "DELETE FROM clienti_francesco_balotta where id='%s' " % id
    print(query)
    cur.execute(query)
    conn.commit()
    
    return "I dati inerenti all'id inserito sono stati eliminati"

if __name__ == '__main__':
    print("Server in ascolto: ")
    HOST = ''
    PORT = 50011
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    thread = []
    lista_connessioni = []
    i = 0

    while True:
        lista_connessioni.append(s.accept())
        print('Connected by', lista_connessioni[i][1])
        thread.append(threading.Thread(target=gestisci_comunicazione, args=(lista_connessioni[i][0],)))
        thread[i].start()
        i += 1
