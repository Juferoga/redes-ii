LAN0=["Brasil","10.16.0.0","255.255.128.0"]
LAN1=["Alemania","10.16.128.0","255.255.192.0"]
LAN2=["Espana","10.16.192.0","255.255.192.0"]
LAN3=["Francia","10.17.0.0","255.255.224.0"]
LAN4=["Japon","10.17.32.0","255.255.240.0"]
LAN5=["Argentina","10.17.48.0","255.255.248.0"]
LAN6=["Portugal","10.17.56.0","255.255.252.0"]
LAN7=["Qatar","10.17.60.0","255.255.254.0"]
LAN8=["Canada","10.17.62.0","255.255.255.0"]
LAN9=["Senegal","10.17.63.0","255.255.255.0"]
LAN10=["Costa Rica","10.17.64.0","255.255.255.128"]
LAN11=["Uruguay","10.17.64.128","255.255.255.128"]
LAN12=["Ecuador","10.17.65.0","255.255.255.192"]
LAN13=["Iran","10.17.65.64","255.255.255.192"]
WAN1=["WAN1","10.17.65.128","255.255.255.252"]
WAN2=["WAN2","10.17.65.132","255.255.255.252"]
WAN3=["WAN3","10.17.65.136","255.255.255.252"]
WAN4=["WAN4","10.17.65.140","255.255.255.252"]
WAN5=["WAN5","10.17.65.144","255.255.255.252"]
WAN6=["WAN6","10.17.65.148","255.255.255.252"]
WAN7=["WAN7","10.17.65.152","255.255.255.252"]
WAN8=["WAN8","10.17.65.156","255.255.255.252"]
WAN9=["WAN9","10.17.65.160","255.255.255.252"]
WAN10=["WAN10","10.17.65.164","255.255.255.252"]
WAN11=["WAN11","10.17.65.168","255.255.255.252"]
WAN12=["WAN12","10.17.65.172","255.255.255.252"]
WAN13=["WAN13","10.17.65.176","255.255.255.252"]
WAN14=["WAN14","10.17.65.180","255.255.255.252"]
WAN15=["WAN15","10.17.65.184","255.255.255.252"]
WAN16=["WAN16","10.17.65.188","255.255.255.252"]
WAN17=["WAN17","10.17.65.192","255.255.255.252"]

redes=[LAN0,LAN1,LAN2,LAN3,LAN4,LAN5,LAN6,LAN7,LAN8,LAN9,LAN10,LAN11,LAN12,LAN13,WAN1,WAN2,WAN3,WAN4,WAN5,WAN6,WAN7,WAN8,WAN9,WAN10,WAN11,WAN12,WAN13,WAN14,WAN15,WAN16,WAN17]

routers={
    "BRASIL":       [LAN0,  WAN1,  WAN7],
    "ALEMANIA":     [LAN1,  WAN3,  WAN9],
    "ESPANA":       [LAN2,  WAN13, WAN14],
    "FRANCIA":      [LAN3,  WAN9,  WAN8, WAN14],
    "JAPON":        [LAN4,  WAN1,  WAN4,  WAN2],
    "ARGENTINA":    [LAN5,  WAN10,  WAN11],
    "PORTUGAL":     [LAN6,  WAN7,  WAN10,  WAN8],
    "QATAR":        [LAN7,  WAN4,  WAN5],
    "CANADA":       [LAN8,  WAN17, WAN12, WAN11],
    "SENEGAL":      [LAN9,  WAN2,  WAN3,  WAN6],
    "COSTA_RICA":   [LAN10, WAN5,  WAN6],
    "URUGUAY":      [LAN11, WAN12, WAN13],
    "ECUADOR":      [LAN12, WAN15, WAN16],
    "IRAN":         [LAN13, WAN12, WAN13, WAN15],
}

for key in routers:
    print(f"-----------{key}--------------")
    print ("configure terminal")
    for red in redes:
        if not routers[key].__contains__(red):
            print(f"ip route {red[1]} {red[2]} se0/3/0")
            print(f"ip route {red[1]} {red[2]} se0/3/1")
            if key=="japon" or key=="senegal" or key=="francia" or key=="portugal":
                print(f"ip route {red[1]} {red[2]} se0/2/0")
            if key=="canada" or key=="iran":
                print(f"ip route {red[1]} {red[2]} se0/2/1")
    print("exit\ncopy running-config startup-config\n\n")
    print("\n")