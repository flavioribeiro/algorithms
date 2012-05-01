MAX_INT = 10

def mult(n_1, n_2):
    global MAX_INT

    if n_1 >= MAX_INT and n_2 >= MAX_INT:
        pe, pd = quebra(n_1)
        qe, qd = quebra(n_2)

        peqe = mult(pe, qe)
        pdqd = mult(pd, qd)
        mult_gauss = (mult(pe+pd, qe+qd) - peqe - pdqd)

        return peqe * pow(10, len(str(n_1))) + ( mult_gauss * pow(10, len(str(n_1))/2)) + pdqd

    else:
        return n_1 * n_2

def quebra(n_1):
    num = str(n_1)
    meio = len(num) / 2
    return int(num[0:meio]), int(num[meio:])
