n, m, a = map(int, input().split())

print((n // a + int(n % a != 0)) * (m // a + int( m % a != 0)))
# or print(n//-a*(m//-a))