class Ip:
  def __init__(self, first_octet, second_octet,  third_octet,  fourth_octet, mask):
    self.first_octet = first_octet
    self.second_octet = second_octet
    self.third_octet = third_octet
    self.fourth_octet = fourth_octet
    self.mask = mask
    self.octal_mask = ""
    self.decimal_mask = ""
    self.octet_jump = 0
    self.octet_jump_position = ""

  def __str__(self):
    return f"{self.first_octet}.{self.second_octet}.{self.third_octet}.{self.fourth_octet}/{self.mask}"
  def convIpDecimal(self):
    return f"{self.first_octet}.{self.second_octet}.{self.third_octet}.{self.fourth_octet}"
  def convIpToBinary(self):
    return f"{'{:0>8}'.format(str(bin(self.first_octet))[2:])}.{'{:0>8}'.format(str(bin(self.second_octet))[2:])}.{'{:0>8}'.format(str(bin(self.third_octet))[2:])}.{'{:0>8}'.format(str(bin(self.fourth_octet))[2:])}"
  def convMaskToBinary(self):
    self.octal_mask = ""
    for octet in range(32):
      if octet < self.mask:
        self.octal_mask+=("1")
      else:
        self.octal_mask+=("0")
    return f"{self.octal_mask[:8]}.{self.octal_mask[8:16]}.{self.octal_mask[16:24]}.{self.octal_mask[24:32]}"
  def convMaskToDecimal(self):
    self.decimal_mask = f"{int(self.octal_mask[0:8],2)}.{int(self.octal_mask[8:16],2)}.{int(self.octal_mask[16:24],2)}.{int(self.octal_mask[24:32],2)}"
    return f"{int(self.octal_mask[0:8],2)}.{int(self.octal_mask[8:16],2)}.{int(self.octal_mask[16:24],2)}.{int(self.octal_mask[24:32],2)}"
  def numberJumps(self):
    mask = self.decimal_mask.split(".")
    i=1
    for octet in mask:
      if int(octet) < 255:
        break
      i+=1
    self.octet_jump_position = i
    zeros_in_ip = str(bin(int(mask[i-1])))[2:].count("0")
    self.octet_jump=2**zeros_in_ip

    return self.octet_jump
  def validateIp(self):
    number = self.convIpDecimal().split(".")[self.octet_jump_position-1]
    if int(number)%self.octet_jump == 0:
      return("Ip valida")
    else:
      if self.octet_jump_position == 1:
        self.first_octet = self.findValidIp(int(number))
      if self.octet_jump_position == 2:
        self.second_octet = self.findValidIp(int(number))
      if self.octet_jump_position == 3:
        self.third_octet = self.findValidIp(int(number))
      if self.octet_jump_position == 4:
        self.fourth_octet = self.findValidIp(int(number))
      return f"Ip no valida úsese en cambio : {self.convIpDecimal()} en el octeto {self.octet_jump_position}\n IP info bin: {self.convIpToBinary()}" 
  def findValidIp(self, number_octet):
    acum = 0
    while(acum < number_octet):
      acum += self.octet_jump
    return acum-self.octet_jump
