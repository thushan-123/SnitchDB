
import time
from typing import Optional, Dict, List
import socket

from .DarkWizardEncodeDecode import wizard_encode, wizard_dir_encode, wizard_decode
from .DataStore import DataStore

BUFFER_SIZE = 1024

class PingCmd:
    def __init__(self, lst: List = None):
        self.lst: list = lst

    def ping(self) -> bytes:
        print(f"ping class {self.lst}")

        
        if len(self.lst) >= 2:
            
            data = " ".join(self.lst[1:])
            return wizard_encode([data])
        return b"+PONG\r\n"
    


class EchoCmd:
    def __init__(self,lst: list):
        self.lst = lst

    def echo(self) -> bytes:
        if len(self.lst) > 1:
            value: str = self.lst[1]
                    
            res: bytes = wizard_encode([value])
            # s = f"${len(value)}\r\n{value}\r\n"

            #print(f"response : {res}")
            return res
        else:
            return b"-ERR wrong number of arguments for 'echo' command\r\n"
        


import time
from typing import List

class SetGetCmd:
    def __init__(self, lst: list, db_cash):
        self.lst = lst
        self.db_cash = db_cash

    def set(self) -> bytes:
        # Syntax: SET key value
        if len(self.lst) == 3:
            status = self.db_cash.set_store(str(self.lst[1]), str(self.lst[2]))
            return b"+OK\r\n" if status == "OK" else b"-ERR failed to set key\r\n"

         
        elif len(self.lst) == 5 and self.lst[3].upper() == "PX":    #PX milliseconds
            try:
                current_time = time.time() * 1000      
                exp_time = current_time + float(self.lst[4])   # current time ms
                status = self.db_cash.set_store(str(self.lst[1]), str(self.lst[2]), exp=exp_time)
                return b"+OK\r\n" if status == "OK" else b"-ERR failed to set key\r\n"
            except:
                return b"-ERR PX value is not a valid integer\r\n"

        
        elif len(self.lst) == 5 and self.lst[3].upper() == "EX": #EX seconds
            try:
                current_time = time.time() * 1000      
                exp_time = current_time + (float(self.lst[4]) * 1000)  
                status = self.db_cash.set_store(str(self.lst[1]), str(self.lst[2]), exp=exp_time)
                return b"+OK\r\n" if status == "OK" else b"-ERR failed to set key\r\n"
            except:
                return b"-ERR EX value is not a valid integer\r\n"

        else:
            return b"-ERR unknown command\r\n"

    def get(self) -> bytes:
        if len(self.lst) == 2:
            data = self.db_cash.get_store(str(self.lst[1]))
            if data is not None:
                return wizard_encode([data])
            else:
                return b"$-1\r\n"
        else:
            return b"$-1\r\n"

            

class KeyCmd: 

    def __init__(self,data_store:DataStore):
         self.data_store = data_store

    def get_key(self,key_expression:str) -> bytes:
         
        try:
            lst: list = self.data_store.search_key(key_expression)
            if len(lst) > 0:
                return wizard_dir_encode(lst)
            else:
                return b"$-1\r\n"
        except Exception as e:
            return b"-ERR invalid pattern\r\n"

    