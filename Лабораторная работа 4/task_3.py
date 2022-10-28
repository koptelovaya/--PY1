def delete(list_, index=None):
    if index is not None:
        c = list_[:index]
        d = list_[index+1:]
        cd_ = c + d
        return cd_
    else:
        k = list_[:-2]
        m = list_[-1:]
        km_ = k + m
        return km_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
