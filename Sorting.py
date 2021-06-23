#module for implementing and testing the sort of player values, isolated.

def quick_score_sort(file_name):
    with open(file_name, 'r+') as file:
        initial_scores = file.readlines() #creates a list with each element being a line in the file.
        raw_scores = []
        toSort = []
        result = []
        for pair in initial_scores:
            print("pair: " + pair)
            raw_pair = pair.replace("\n",'')
            split_pair = raw_pair.split(sep=" ", maxsplit= 1)
            raw_scores.append(split_pair)
        for line in raw_scores:
            print(line)
            toSort.append(int(line[1]))

        print("to sort")
        print(toSort)

        result = sort_aux(toSort)
        print("result")
        print(result)

        result_wnames = []
        for element in result:
            for line in raw_scores:
                if int(line[1]) == element:
                    print("Name:" + line[0])
                    print("pair:" + line[1])
                    print("element: " + str(element))
                    tmp = line[0] + ' ' + str(element)
                    print(tmp)
                    result_wnames.append(tmp) #termina como la lista ordenada con nombres incluidos
        print(result)
        print(result_wnames)

        #escribe la nueva lista de puntajes
        file.truncate(0)
        file.seek(0)

        #escribir la lista en el orden inverso del que están en el result_wnames
        result_wnames.reverse()

        for line in result_wnames:
            line = line + '\n'
            file.write(line)
        file.close()

def sort_aux(list):
    elems = len(list)

    #base case
    if elems < 2:
        return list

    current = 0
    for i in range(1, elems): #splitting or partitioning loop
        if list[i] <= list[0]:
            current += 1
            temp = list[i]
            list[i] = list[current]
            list[current] = temp

    temp = list[0]
    list[0] = list[current]
    list[current] = temp #places pivot in its proper position

    left = sort_aux(list[0:current]) #sorts from left to pivot
    right = sort_aux(list[current + 1:elems])#sorts from right of pivot to end

    result = left + [list[current]] + right
    return result

def find_score_position(Name):
    i = 1
    with open("scores.txt", 'r') as file:
        list = file.readlines()
        for score in list:
            #score.replace('\n','')
            sublist = score.split(' ')
            if sublist[0] == Name:
                break
            i += 1
    return i

#quick_score_sort("scores.txt")