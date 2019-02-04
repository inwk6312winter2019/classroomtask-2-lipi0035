class ipaddr():
  def __init__(self,ip = [0,0,0,0],nm = [0,0,0,0]):
    self.ip = ip
    self.nm = nm
  def __str__(self):
    ipformat = ""
    for ips in self.ip:
      ipformat = ipformat + str(ips) + '.'
    return ("The address is "+ipformat)
  def __add__(self,other):
    return (self.ip[0]+other.ip[0],self.ip[1]+other.ip[1],self.ip[2]+other.ip[2],self.ip[3]+other.ip[3])


myip = ipaddr([192,168,1,1],[255,255,255,0])
addip = ipaddr([2,1,1,1])
result = myip+addip
print(myip)
print(result)
