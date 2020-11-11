with open("c:/work/devops/ws01_ex01_step2.txt", "r") as f:
    for line in f.read().splitlines():
        arg = line.split()
        if arg[0] == "calc":
            if arg[1] == "+":
                result = int(arg[2]) + int(arg[3])
            elif arg[1] == "-":
                result = int(arg[2]) - int(arg[3])
            elif arg[1] == "x":
                result = int(arg[2]) * int(arg[3])
            elif arg[1] == "/":
                result = int(arg[2]) / int(arg[3])
            else:
                print("Invalid operation")
            print(arg[2] + arg[1] + arg[3] + " = " + str(result))
