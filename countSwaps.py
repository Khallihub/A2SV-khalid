def countSwaps(a):
    size = len(a)
    no = 0
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                swapped = True
                no += 1
        if not swapped:
            break
    print("Array is sorted in " + str(no) + " swaps.\nFirst Element: " + str(a[0]) + "\nLast Element: "+str(a[-1]))
