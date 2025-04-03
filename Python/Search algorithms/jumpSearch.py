jumpSearch = lambda a,n,s = None,b = 0, c = None: jumpSearch(a,n,int(len(a) ** (0.5)),b,c) if s == None else jumpSearch(a,n,s,b,s) if c == None else -1 if b >= len(a) else jumpSearch(a,n,s,b+s,c+s) if a[c] < s else -1 if b == len(a) else jumpSearch(a,n,s,b+1,c) if a[b] < n else b if a[b] == n else -1
a = [1,2,3,4,5,12,23,43,56,67,78,123,234,345,456,567,678,789]
print(jumpSearch(a,567))