#       |  NOMBRE RED |  DIR. RED  |    WILDCARD   |
LAN0  = [ "DUITAMA"    ,"85.80.0.0",     "0.0.0.127"  ] # /25 11111111.11111111.11111111.10000000 
LAN1  = [ "GUTIERREZ"    ,"85.80.0.128",   "0.0.0.127"  ] # /25 11111111.11111111.11111111.10000000
LAN2  = [ "ANAPOIMA"    ,"85.80.1.0",     "0.0.0.15"   ] # /28 11111111.11111111.11111111.11110000
LAN3  = [ "TOCAIMA"    ,"85.80.1.16",    "0.0.0.7"    ] # /29 11111111.11111111.11111111.11111000
WAN1  = [ "WAN1"    ,"85.80.1.24",    "0.0.0.3"    ] # /30 11111111.11111111.11111111.11111100
WAN2  = [ "WAN2"    ,"85.80.1.28",    "0.0.0.3"    ] # /30 11111111.11111111.11111111.11111100
WAN3  = [ "WAN3"    ,"85.80.1.32",    "0.0.0.3"    ] # /30 11111111.11111111.11111111.11111100
WAN4  = [ "WAN4"    ,"85.80.1.36",    "0.0.0.3"    ] # /30 11111111.11111111.11111111.11111100
WAN5  = [ "WAN5"    ,"85.80.1.40",    "0.0.0.3"    ] # /30 11111111.11111111.11111111.11111100

redes=[LAN0,LAN1,LAN2,LAN3,WAN1,WAN2,WAN3,WAN4,WAN5]

routers={
    "DUITAMA":       [LAN0,  WAN1,  WAN4, WAN5],
    "GUTIERREZ":     [LAN1,  WAN1,  WAN2],
    "ANAPOIMA":      [LAN2,  WAN2, WAN3, WAN5],
    "TOCAIMA":       [LAN3,  WAN4, WAN3]
}

for key in routers:
    i=1
    print(f"-----------{key}--------------")
    print(f"! S{i} LAN{i} - {key}")
    print("! Modo privilegiado")
    print("enable")
    print("! configuracion global")
    print("configure terminal")
    print("!contraseña de enable")
    print(f"hostname {key}")
    print("enable password 8586")
    print("! cofiguracion consola")
    print("line console 0")
    print("password 8586")
    print("login")
    print("exit")
    print("! cofiguracion vty")
    print("line vty 0 4")
    print("password 8586")
    print("login")
    print("exit")
    print("! configuracion banner")
    print(f"banner motd # Hola soy {key}, Att. Juan Felipe Rodriguez Galindo, 20181020158, 1001088586 #")
    print("exit")
    print("! Guardar configuracion")
    print("copy running-config startup-config")
    print("! Configuracion interfaces GigabitEthernet")
    print("interface GigabitEthernet 0/0")
    print("no shutdown ")
    print("ip address ip_lan mask_lan")
    print(f"description conectado a {key}")
    print("exit")
    print("! Configuracion interfaces Serial WAN 1")
    print("configure terminal")
    print("interface serial 0/3/0")
    print("no shutdown ip_wan mask_wan")
    print("ip address ")
    print(f"description conectado a {key}")
    print("clock rate 56000")
    print("exit")
    print("configure terminal")
    print("interface serial 0/3/1")
    print("no shutdown ip_wan mask_wan")
    print("ip address ")
    print(f"description conectado a {key}")
    print("clock rate 56000")
    print("exit")
    print("! Configuracion de enrutamiento OSPF")
    print ("configure terminal")
    print("router ospf 1")
    for red in redes:
        if routers[key].__contains__(red):
            print(f"network {red[1]} {red[2]} area 0")
            if key=="ANAPOIMA" or key=="DUITAMA":
                print(f"network {red[1]} {red[2]} area 0")
    print("exit\nexit\ncopy running-config startup-config\n\n")
    print("\n")
    i=i+1