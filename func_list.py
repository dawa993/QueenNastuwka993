def yvel_v_n_raz(lst: list, n):
    return [i * n for i in lst]


lst = [1, 4, 6, 7, 9]
a = 7
print(lst)
print(yvel_v_n_raz(lst, a))
