import collections

repl = "\r\n"; split = repl + repl

def ansplit(uplist):
  if not uplist:
    return []
  uplist = [ta.replace(repl, " ") for ta in uplist.split(split)]
  return uplist

def titler(uplist):
  if len(uplist) == 0:
    return []
  uplist = [up.split(",")[0].split(" ")[0] for up in uplist]
  return uplist

zele = {
  "Jasa":"Jasa Utama", 
  "Mayasari":"Mayasari Bakti", 
  "Steady":"Steady Safe", 
  "Pahala":"Pahala Kencana"
}

def jarly(jasplit):
  if not jasplit:
    return []
  result = [ja.split(":")[0] for ja in jasplit]
  result =  [int(ja) for ja in result]
  result = collections.Counter(result)
  return result
