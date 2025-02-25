from itertools import product

# Definišemo logičke operacije
def neg(x):
    return int(not x)

def impl(x, y):
    return int(not x or y)

# Generišemo sve moguće kombinacije o, s, v
truth_values = list(product([0, 1], repeat=3))

# Računamo p, q, r i p ^ q ^ r za svaku kombinaciju
table = []
for o, s, v in truth_values:
    p = o or s or v
    q = impl(o and s, v)
    r = impl(neg(v), o and neg(s))
    final = p and q and r
    table.append([o, s, v, p, o and s, q, neg(v), neg(s), o and neg(s), r, final])

# Ispisujemo tabelu istinitosti
header = ["o", "s", "v", "p = o V s V v", "o ^ s", "q = (o ^ s) => v", 
          "neg v", "neg s", "o ^ neg s", "r = neg v => (o ^ neg s)", "p ^ q ^ r"]
print("{:<3} {:<3} {:<3} {:<15} {:<7} {:<20} {:<7} {:<7} {:<12} {:<25} {:<10}".format(*header))
for row in table:
    print("{:<3} {:<3} {:<3} {:<15} {:<7} {:<20} {:<7} {:<7} {:<12} {:<25} {:<10}".format(*row))
