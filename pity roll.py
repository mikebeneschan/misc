import random
pity = 0
for i in range(99):
  x=random.uniform(0,1)
  if pity==20:
    print("success: pity roll activated")
    pity=0
    continue 
  if x<=0.10:
    print("success")
    pity=0
  else:
    print("failure")
    pity += 1
