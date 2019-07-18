APPLE=100

def fun():
  global a
  a=APPLE
  
  return a+100
fun()
print(APPLE)
print(a)

