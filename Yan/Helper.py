import collections

repl = "\r\n"; split = repl + repl

ontrue = ~False

urutan = lambda sample :  dict(sorted(sample.items(), key=lambda item: item[1], reverse=ontrue))

limite = lambda sample, i : dict(list(sample.items())[:i])

faili = lambda uplist : [] if not uplist else uplist

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
  "Jasa":"Jasa Utama", "Agung":"Agung Bhakti",
  "Mayasari":"Mayasari Bakti", "Steady":"Steady Safe", 
  "Pahala":"Pahala Kencana", "Megah":"Megah Langgeng",
  "Sinar":"Sinar Jaya ML"
}

def replator(uplist):
  uplist = [zele[i] if i in zele else i for i in uplist]
  return uplist

def motol(sanlist):
  if not sanlist:
    return ([], 0)
  mota = ansplit(sanlist)
  moti = replator(titler(mota))
  singleti = {moti[i]: len(mota[i].split(",")) for i in range(len(moti))}
  return list(singleti.keys()), sum(singleti.values())

def jalister(uplist):
  if not uplist:
    return []
  uplist = [ja.strip() for ja in uplist.split(",")]
  return uplist

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
  rata = int(total / len(uplist))
  return rata

def imsplit(uplist, l, split):
  fail = []
  for i in range(len(uplist)):
    if len(uplist[i]) != l:
      key = i
      fail = uplist[i].split(split)
      fail.remove("")
  uplist = uplist[:key] + fail + uplist[key+1:]
  return uplist