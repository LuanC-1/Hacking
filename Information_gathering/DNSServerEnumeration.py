import socket

dominio1 = input("Insira o dominio: ")

# Enumerando de subdominios, com variavel definida
nomes = ["ns", "ns1", "ns2", "www", "ftp", "intranet", "localhost", "mail", "webmail", "smtp", "pop", "webdisk",
         "whm", "cpanel", "autodiscover", "autoconfig", "m", "imap", "test", "pop3", "dev", "www2", "admin"]

for nome in nomes:
    DNS = nome + '.' + dominio1
try:
    print(DNS + ": " + socket.gethostbyname(DNS))
except socket.gaierror:
    pass

# Enumerando de subdominios, com arquivo.txt
import socket

dominio = input("Insira o dominio: ")

#Definir o diretorio do caminho do arquivo Wordlist, utilizar / ao invés de \
with open("C:/caminho/caminho") as arquivo:
    nomes = arquivo.readlines()
for nome in nomes:
    DNS = nome.strip("\n") + "." + dominio
try:
    print(DNS + ": " + socket.gethostbyname(DNS))
except socket.gaierror:
    pass