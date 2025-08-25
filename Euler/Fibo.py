if __name__ == "__main__":
    i = 1
    sum = j = 2
    k = i + j
    while k < 4000000:
        if k % 2 == 0:
            sum += k
        i, j, k = j, k, j + k
    print(sum)