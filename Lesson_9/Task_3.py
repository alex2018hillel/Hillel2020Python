def print_full_name2(client):
    words = client.split()
    print(' '.join(client[:1].upper() + client[1:] for client in words))

if __name__ =="__main__":
    client = input()
    print_full_name2(client)