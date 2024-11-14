#Задача B
def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]