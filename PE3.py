print("anything")
a = 600851475143
i = 1
while i * i < a:
  print("first")
  while a%i == 0:
    a = a/i
    print("second")
  i += 1

print(a)
