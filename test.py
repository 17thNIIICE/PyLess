def min_corrections(n, m, a):
    good_days = 0
    corrections = 0

    for i in range(1, n - 1):
        if a[i] >= a[i - 1] and a[i] <= a[i + 1]:
            good_days += 1
    
    if good_days >= m:
        return 0 
    
    for i in range(1, n - 1):
        if good_days >= m:
            break
        
        if not (a[i] >= a[i - 1] and a[i] <= a[i + 1]):
            if a[i] < a[i - 1]:
                a[i] = a[i - 1] 
            elif a[i] > a[i + 1]:
                a[i] = a[i + 1]
            
            corrections += 1
            good_days += 1
    
    return corrections

n, m = map(int, input().split())
a = list(map(int, input().split()))

print(min_corrections(n, m, a))
