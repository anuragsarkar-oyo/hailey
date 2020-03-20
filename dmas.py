import math

def run(curr, target, value, level):

  q = [[curr,'+']]
  done = []
  while len(q) > 0:
    top = q[0][0]
    op = q[0][1]
    # print(q)
    q.pop(0)
    if op != '//':
      if(top*value == target):
        break
      if top*value not in done:
        q.append([top*value, '*'])
        done.append(top*value)
    if op != '-':
      if(top+value == target):
        break
      if top+value not in done:
        q.append([top+value, '+'])
        done.append(top+value)
    if op != '+':
      if(top-value == target):
        break
      if top-value not in done:
        q.append([top-value, '-'])
        done.append(top-value)
    if op != '*':
      if(top//value == target):
        break
      if top//value not in done:
        q.append([top//value, '//'])
        done.append(top//value)
    level += 1
  print(done)
  return math.ceil(level** (1. / 3))


print(run(9, 5, 9, 1))
