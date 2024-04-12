numAcl = int(input("Ingrese número ACL "))
if numAcl >= 1 and numAcl <= 99:
    print("Esta es una ACL estándar")
elif numAcl >=100 and numAcl <= 199:
    print("Esta es una ACL extendida")
else:
    print("El valor ingresado no corresponde a una ACL")
