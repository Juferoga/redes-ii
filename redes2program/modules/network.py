import math

powers_of_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888]

class Network:
  def __init__(self, name, hosts):
    self.name = name
    self.hosts = hosts
    
    while (True):
      print("hola")
      break

  def __str__(self):
    return f"| {self.name}  | {self.hosts}    | {self.mask} |"

  def calculeMask(self, hosts):
    cont = 0
    acu = 0
    while(acu <= math.log2(hosts+2)):
      cont = cont+1
      acu = cont**2
    return acu-1
