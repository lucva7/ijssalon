import math

def discriminant(a, b, c):
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    except ValueError:
        D1 = D2 = "geen oplossing"
    return [D1, D2]

# Hoofdcode
print("Voor de formule ax^2 + bx + c, geef a, b en c:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

uitkomst = discriminant(a, b, c)
D1, D2 = uitkomst[0], uitkomst[1]

print(f"Voor de waarden a={a}, b={b}, en c={c}, zijn de waarden van D1 en D2 respectievelijk {D1} en {D2}.")
