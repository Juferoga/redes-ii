from modules.ip import Ip
from modules.network import Network
import math
from utils.twoPower import powers_of_two

initial_ip = list(map(int,input("Ingresa la IP inicial : ").split(".")))
mask_ip = int(input("Ingresa la mascara de red : /"))
ip = Ip(initial_ip[0],initial_ip[1],initial_ip[2],initial_ip[3],mask_ip)

print("IP information")
print("Ip : ",ip)
print("Binary ip : ",ip.convIpToBinary())
print("MASK information")
print("Binary mask: ",ip.convMaskToBinary())
print("Decimal mask: ",ip.convMaskToDecimal())
# print("JUMPS information")
# print("Number Jumps : ",ip.numberJumps())
# print("Number Jumps in octet -> # of octet: ",ip.octet_jump_position)
# print("Valid IP information")
# print("Valid IP \n",ip.validateIp())

# subnet_lan = int(input("Escriba el número de subredes LAN > "))
# subnet_wan = int(input("Escriba el número de subredes WAN > "))

# networks = []
# for network in range(subnet_lan):
#   subnet_name = input("Nombre de la subred: ")
#   subnet_host = int(input("Número de hosts: "))
#   networks.append(Network(subnet_name,subnet_host))

# for network in range(subnet_wan):
#   networks.append(Network("WAN "+str(network),2))

# networks = sorted(networks, key=lambda x:x.hosts, reverse=True)

# print(f"\n| Nombre | # de hosts | bits de host |")
# for network in networks:
#   print(network)


