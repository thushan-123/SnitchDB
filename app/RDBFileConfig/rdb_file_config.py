from ..DarkWizardEncodeDecode import wizard_dir_encode
from typing import List, Dict
import re
import struct
import os

class RDBFileConfig():

    def __init__(self,args:List):
        self.list = args

    def handle_config(self ,dir_path: str, db_file_name: str) -> bytes:
        if len(self.list) < 2:
            return b"-ERR wrong number of arg for CONFIG cmd\r\n"
        
        if self.list[0].upper() == "GET":
            if self.list[1].lower() == "dir":
                return wizard_dir_encode([self.list[1],dir_path])
            elif self.list[1].lower() == "dbfilename":
                return wizard_dir_encode(["dbfilename",db_file_name])
        else:
            return b"-ERR for CONFIG cmd\r\n"
        
class RemoveComents():
    def __init__(self,data:str):
        self.data =data
    
    def remove_comment(self):
        text = re.sub(r'/\*.*?\*/', '', self.data, flags=re.DOTALL)
    
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            
            stripped_line = line.strip()
            
            # remove #, //, or ---
            if (stripped_line and 
                not stripped_line.startswith('#') and 
                not stripped_line.startswith('//') and 
                not stripped_line.startswith('---')):
                cleaned_lines.append(line)

        return '\n'.join(cleaned_lines)
        
        
class RDBpasser():

    def __init__(self,dir_path:str, db_file_name: str):
        self.path = dir_path
        self.db_file_name = db_file_name
        self.header =[]
        self.meta_data =[]
        self.database =[]
        self.eof_sec = []
        self.file = f"{self.path}/{self.db_file_name}"
        # self.clean_file = RemoveComents(f"{self.path}/{self.db_file_name}").remove_comment()
        

    """
    Header section
        RDB files begin with a header section, which looks something like this:

        52 45 44 49 53 30 30 31 31  // Magic string + version number (ASCII): "REDIS0011".
        The header contains the magic string REDIS, followed by a four-character RDB version number. 
        In this challenge, the test RDB files all use version 11. So, the header is always REDIS0011.
    """
    




# if __name__ == "__main__":
#     rdb_file_config: RDBFileConfig = RDBFileConfig(["GET", "dir"])
#     print(rdb_file_config.handle_config("app/RDBFileConfig", "dump.rdb"))
    
#     rdb_file_config = RDBFileConfig(["GET", "dbfilename"])
#     print(rdb_file_config.handle_config("app/RDBFileConfig", "dump.rdb"))
    
    