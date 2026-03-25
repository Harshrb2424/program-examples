def hcf(a, b):
    while(b != 0):
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // hcf(a, b)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(hcf(int(input()), int(input())))

print(lcm(int(input()), int(input())))

print(is_leap_year(int(input())))