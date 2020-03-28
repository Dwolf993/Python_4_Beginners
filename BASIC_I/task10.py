n = int(input("Please enter a integer: "))
n1 = n
n2 = int("%d%d" % (n,n))
n3 = int("%d%d%d" % (n,n,n))
print(n1)
print(n2)
print(n3)
rez = n1 + n2 + n3
print("Rezult of n + nn + nnn is: " + str(rez))
