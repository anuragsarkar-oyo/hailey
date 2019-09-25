

def uniqchar(st):
  last_value = {c : i for i,c in enumerate(st)}
  seen = set()
  stack = []
  for i,char in enumerate(st) : 
    if char not in seen: 
      print(stack, seen)
      while stack and char < stack[-1] and i < last_value[stack[-1]]: 
        seen.remove(stack.pop())
      seen.add(char)
      stack.append(char)
  return stack,seen
      
st = "ksajndkojdas"
a, b = uniqchar(st)
print(a, b)
