import threading
import time
import re



class DataStore():
    
    def __init__(self) -> None:
        self.key_map_store = {}
        self.lock = threading.Lock()

    def get_store(self,search_key) -> str:
        with self.lock:
            for key,data in self.key_map_store.items():
                if (key == search_key and data['exp'] is not None):
                    if (key == search_key and data['exp'] > (time.time()*1000)):
                        return data['value']
                    else:
                        del self.key_map_store[key]
                        break
                elif key == search_key and data['exp'] is None:
                    return data['value']
            return None

    def set_store(self, key, value, exp=None) -> str:
        with self.lock:
            self.key_map_store[key] = {'value': value, 'exp': exp}
            return "OK"
        
    def search_key(self,pattern: str,get_key_valus: bool = False) -> list:
        safe_pattern = re.escape(pattern).replace(r'\*', '.*').replace(r'\?', '.')
        reg_x = re.compile(f"^{safe_pattern}$")
        key_list: list = []
        with self.lock:
            for key,data in self.key_map_store.items():
                if reg_x.search(key):
                    if data["exp"] is None or (data["exp"] > (time.time())*1000):
                        if not get_key_valus:
                            key_list.append(key)
                        else:
                            key_list.append([key,data])
        return key_list
                    

    

if __name__ == "__main__":

    db: DataStore = DataStore()

    print(db.set_store("name1","kamal",exp=time.time() *1000 + 10000))

    time.sleep(3)

    print(db.get_store("name1"))
    