
filename = "PS07R25.csv"

if __debug__:
    print (filename + " was found")

results = {}


with open(filename) as file:
    i = 0
    raw_file_list = []
    for line in file:
        if __debug__:
            print (line)

        if line == '\n':
            continue

        print(i)

        raw_file_list.append(line)

        i = i + 1
        print(i)
        if __debug__:
            print (raw_file_list[i])




file.close()




