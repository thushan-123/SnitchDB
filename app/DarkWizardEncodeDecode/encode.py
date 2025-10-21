#   [b'*2', b'$4', b'ECHO', b'$3', b'hey'] byte array convert string array   -> ['*2', '$4', 'ECHO', '$3', 'hey']

#   ["ECHO","hey"]  *2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n

def wizard_dir_encode (arr_data: list) -> str:

    encoded_str: str = f"*{len(arr_data)}\r\n"

    for item in arr_data:
        if not isinstance(item, str):
            item =str(item)
        encoded_str+= f"${len(item)}\r\n{item}\r\n"

    return encoded_str.encode()

def wizard_encode(arr_data: list) -> bytes:
    encoded_str = ""
    for item in arr_data:
        if not isinstance(item, str):
            item = str(item)
        encoded_str += f"${len(item)}\r\n{item}\r\n"
    return encoded_str.encode()



# def wizard_encode(arr_data: list) -> bytes:

#     encoded_str: str = ""
#     for item in arr_data:
#         if not isinstance(item, str):
#             item = str(item)
            
#         encoded_str += f"${len(item)}\r\n{item}\r\n"  
#     return encoded_str.encode()

if __name__ == "__main__":
    print(wizard_dir_encode(["dir","/tmp/redis-files"]))

    if b"*2\r\n$4\r\nECHO\r\n$3\r\nhey\r\n" == wizard_encode(["ECHO","hey"]):
        print("ok")









