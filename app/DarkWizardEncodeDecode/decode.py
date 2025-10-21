
#s.strip("\r\n")

# print(s.strip().split(b"\r\n"))


def wizard_decode(byte_str: bytes) -> list[str]:

         #   [b'*2', b'$4', b'ECHO', b'$3', b'hey'] byte array convert string array   -> ['*2', '$4', 'ECHO', '$3', 'hey']

    string_list = [x.decode() for x in byte_str.strip().split(b"\r\n")]    # ['*2', '$4', 'ECHO', '$3', 'hey']

    """
        *<number> is number of commands and arument
        $<number> is represent length of each cmd or Argument
    """

    size_string_list = len(string_list)

    num_of_words = int(string_list[0][1:])

    output_list: list[str] = []

    for x in range(1,size_string_list,2):

        # if we check word size is equal to $<number>
        n : int = int(string_list[x][1:])
        word_size: int = len(string_list[x+1])

        if n == word_size:
            output_list.append(string_list[x+1])

    if num_of_words == len(output_list):
        return output_list
    else:
        return [""]


if __name__ == "__main__":
    print(wizard_decode(b"*1\r\n$4\r\nPING\r\n"))



