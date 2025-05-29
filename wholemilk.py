def print_section(n, w, g):  # name, weighting, grades
    l = n.ljust(18)
    l += f'{(w / 36) * 100:.2f}%'.ljust(18)
    l += f'{sum(g.values()):.2f}'.ljust(18)
    l += f'{len(g) * 100:.2f}'.ljust(18)
    l += f'{sum(g.values()) / len(g):.2f}'
    print(l)

def nto4(n):
    if n > 97:
        return 4.0
    if n < 57:
        return 1.0
    return f'{(n - 57) / 10:.1f}'