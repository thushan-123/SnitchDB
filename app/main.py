import socket
import threading
import sys
import signal
import time
import argparse
from typing import Dict,List,Optional


from .DarkWizardEncodeDecode import wizard_decode,wizard_encode,wizard_dir_encode
from .DataStore import DataStore
from .command import PingCmd, EchoCmd, SetGetCmd, KeyCmd
from .RDBFileConfig import RDBFileConfig

BUFFER_SIZE = 1024

FILE_PATH = "/tmp/redis-files"
DUMP_DB = "dump.rdb"

def signal_to_terminate(sig ,frame):
    sys.exit(0)


# SIGINT  -> ctrl + c

signal.signal(signal.SIGINT,signal_to_terminate) 


def concurrent_users(client_socket:socket.socket):

    try:
        db_cash: DataStore = DataStore()
        while True:
            
            try:
                recived_cmd = client_socket.recv(BUFFER_SIZE)
                # client set if not data  close to the client connection
                if not recived_cmd:
                    break

                print(f"client send command : {wizard_decode(recived_cmd)}")

                cmd_decode: list = wizard_decode(recived_cmd)


                # handle client ping commnd   b"*1\r\n$4\r\nPING\r\n"
                if "PING" == cmd_decode[0].upper():

                    pingCmd: PingCmd = PingCmd(cmd_decode)
                    client_socket.sendall(pingCmd.ping())
                    

                elif "ECHO" == cmd_decode[0].upper():

                    echoCmd: EchoCmd = EchoCmd(cmd_decode)
                    client_socket.sendall(echoCmd.echo())    

                elif "SET" == cmd_decode[0].upper() or "GET" == cmd_decode[0].upper():
                    cmd: SetGetCmd = SetGetCmd(cmd_decode, db_cash)
                    if "SET" == cmd_decode[0].upper():
                        client_socket.sendall(cmd.set())
                    else:
                        client_socket.sendall(cmd.get())
                
                elif "CONFIG" == cmd_decode[0].upper() and len(cmd_decode) == 3:
                    rdb_file_config: RDBFileConfig = RDBFileConfig([cmd_decode[1],cmd_decode[2]])
                    re = rdb_file_config.handle_config(FILE_PATH,DUMP_DB)
                    client_socket.sendall(re)
                
                elif "KEYS" == cmd_decode[0].upper() and len(cmd_decode) == 2:
                    key_cmd: KeyCmd = KeyCmd(db_cash)
                    result: bytes = key_cmd.get_key(str(cmd_decode[1]))
                    client_socket.sendall(result)
                else:
                    client_socket.sendall(b"-ERR unknown command\r\n")
            except Exception as e:
                print(f"ERROR - {e}")
                client_socket.sendall(b"-ERR unknown command\r\n")

    except Exception as e:
        print(f"ERROR - {e}")
        client_socket.sendall(b"-ERR unknown command\r\n")

    finally:
        client_socket.close()
    
    



def main():
    
    print("----- SNITCH_DB ----- (redis protocol) \r\n")

    host = "127.0.0.1"
    port = 6379

    server_socket = socket.create_server((host,port), reuse_port=True)

    server_socket.listen()
    
    print(f"Server Listen Port: {port}")

    while True:

        conn, _ = server_socket.accept()

        threading.Thread(target=concurrent_users, args=(conn,), daemon=True).start()



pass_arg =argparse.ArgumentParser(description= "Snich Server")
pass_arg.add_argument("--dir", type=str, default=FILE_PATH, help="Directory to store the rdb file")
pass_arg.add_argument("--dbfilename", type=str, default=DUMP_DB, help="Name of the rdb file")

if __name__ == "__main__":
    args = pass_arg.parse_args()
    FILE_PATH = args.dir
    DUMP_DB = args.dbfilename
    main()
