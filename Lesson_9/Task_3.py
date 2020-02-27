def print_full_name(client):
    print(client.title())

def print_full_name2(client):
    words = client.split()
    for i in range(len(words)):
        words[i] = words[i].replace(words[i][0], chr(ord(words[i][0]) - 32))
    print( ' '.join(words))

if __name__ =="__main__":
    client = input()
    print_full_name(client)
    print_full_name2(client)