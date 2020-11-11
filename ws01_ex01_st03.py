with open("c:/work/devops/ws01_ex01_step3.txt", "r") as f:
    line = f.read().splitlines()
    visited_line = []
    done = False
    lnum = 0
    while not done:
        visited_line.append(lnum)
        arg = line[lnum].split()
        if arg[0] == "goto":
            if arg[1] == "calc":
                if arg[2] == "+":
                    lnum = int(int(arg[3]) + int(arg[4]))
                elif arg[2] == "-":
                    lnum = int(int(arg[3]) - int(arg[4]))
                elif arg[2] == "x":
                    lnum = int(int(arg[3]) * int(arg[4]))
                elif arg[2] == "/":
                    lnum = int(int(arg[3]) / int(arg[4]))
                else:
                    print("Invalid operation")
            else:
                lnum = int(arg[1])
        for ln in visited_line:
            if ln == lnum:
                print(visited_line)
                print("Already visited line: " + str(lnum))
                done = True
                break
