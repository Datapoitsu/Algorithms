linearSearch = lambda a,n,i = 0: i if a[i] == n else linearSearch(a,n, i + 1) if i < len(a) - 1 else -1

a = [1,2,5,7,8,123,34,5,6,7,8,9]
print(linearSearch(a,9))