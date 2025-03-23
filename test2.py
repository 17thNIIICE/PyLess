def boss_operations(n, x, y, z, a):
    def boss_min_steps_to_divisible(a, d):
        return min((d - ai % d) % d for ai in a)  
    return boss_min_steps_to_divisible(a, x) + boss_min_steps_to_divisible(a, y) + boss_min_steps_to_divisible(a, z)

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))

print(boss_operations(n, x, y, z, a))