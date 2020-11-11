opn = input("Enter operation")
opr1 = int(input("Enter operand-1"))
opr2 = int(input("Enter operand-2"))
#print(eval(f"{opr1} {opn} {opr2}"))
if opn == "+":
    result = opr1 + opr2
elif opn == "-":
    result = opr1 - opr2
elif opn == "x":
    result = opr1 * opr2
elif opn == "/":
    result = opr1 / opr2
elif opn == "^":
    result = opr1 ** opr2
else:
    print("Invalid operation")
print(str(opr1) + opn + str(opr2) + " = " + str(result))

