import collections

repl = "\r\n"; split = repl + repl

ontrue = ~False

urutan = lambda sample :  dict(sorted(sample.items(), key=lambda item: item[1], reverse=ontrue))

limite = lambda sample, i : dict(list(sample.items())[:i])

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

def janit(uplist):
  if not uplist:
    return []
  total = 0
  for t in range(len(uplist) - 1):
    i = int(uplist[t].split(":")[1])
    j = int(uplist[t + 1].split(":")[1])
    if j < i:
      j += 60
    total += j - i
  rata = round(total / len(uplist), 3)
  return rata
