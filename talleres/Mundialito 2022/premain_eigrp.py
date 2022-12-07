LAN0  = [ "BRASIL"      ,"10.16.0.0",       "0.0.127.0"  ]
LAN1  = [ "ALEMANIA"    ,"10.16.128.0",     "0.0.63.0"  ]
LAN2  = [ "ESPANA"      ,"10.16.192.0",     "0.0.63.0"  ]
LAN3  = [ "FRANCIA"     ,"10.17.0.0",       "0.0.31.0"  ]
LAN4  = [ "JAPON"       ,"10.17.32.0",      "0.0.15.0"  ]
LAN5  = [ "ARGENTINA"   ,"10.17.48.0",      "0.0.7.0"  ]
LAN6  = [ "PORTUGAL"    ,"10.17.56.0",      "0.0.3.0"  ]
LAN7  = [ "QATAR"       ,"10.17.60.0",      "0.0.1.0"  ]
LAN8  = [ "CANADA"      ,"10.17.62.0",      "0.0.0.0"  ]
LAN9  = [ "SENEGAL"     ,"10.17.63.0",      "0.0.0.0"  ]
LAN10 = [ "COSTA_RICA"  ,"10.17.64.0",      "0.0.0.127"]
LAN11 = [ "URUGUAY"     ,"10.17.64.128",    "0.0.0.127"]
LAN12 = [ "ECUADOR"     ,"10.17.65.0",      "0.0.0.63"]
LAN13 = [ "IRAN"        ,"10.17.65.64",     "0.0.0.63"]
WAN1  = [ "WAN1"        ,"10.17.65.128",    "0.0.0.3"]
WAN2  = [ "WAN2"        ,"10.17.65.132",    "0.0.0.3"]
WAN3  = [ "WAN3"        ,"10.17.65.136",    "0.0.0.3"]
WAN4  = [ "WAN4"        ,"10.17.65.140",    "0.0.0.3"]
WAN5  = [ "WAN5"        ,"10.17.65.144",    "0.0.0.3"]
WAN6  = [ "WAN6"        ,"10.17.65.148",    "0.0.0.3"]
WAN7  = [ "WAN7"        ,"10.17.65.152",    "0.0.0.3"]
WAN8  = [ "WAN8"        ,"10.17.65.156",    "0.0.0.3"]
WAN9  = [ "WAN9"        ,"10.17.65.160",    "0.0.0.3"]
WAN10 = [ "WAN10"       ,"10.17.65.164",    "0.0.0.3"]
WAN11 = [ "WAN11"       ,"10.17.65.168",    "0.0.0.3"]
WAN12 = [ "WAN12"       ,"10.17.65.172",    "0.0.0.3"]
WAN13 = [ "WAN13"       ,"10.17.65.176",    "0.0.0.3"]
WAN14 = [ "WAN14"       ,"10.17.65.180",    "0.0.0.3"]
WAN15 = [ "WAN15"       ,"10.17.65.184",    "0.0.0.3"]
WAN16 = [ "WAN16"       ,"10.17.65.188",    "0.0.0.3"]
WAN17 = [ "WAN17"       ,"10.17.65.192",    "0.0.0.3"]

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
    print(f"!-----------{key}--------------")
    print("router eigrp 1")
    for red in redes:
        if routers[key].__contains__(red):
            print(f"network {red[1]} {red[2]} area 0")
            if key=="japon" or key=="senegal" or key=="francia" or key=="portugal":
                print(f"network {red[1]} {red[2]} area 0")
            if key=="canada" or key=="iran":
                print(f"network {red[1]} {red[2]} area 0")
        print("no auto-summary")
    print("exit\nexit\ncopy running-config startup-config\n\n")
    print("\n")