def print_section(n, w, g):  # name, weighting, grades
    l = n.ljust(18)
    l += f'{(w / (aw + bw + cw + dw + ew)) * 100:.2f}%'.ljust(18)
    l += f'{sum(g.values()):.2f}'.ljust(18)
    l += f'{len(g) * 100:.2f}'.ljust(18)
    l += f'{sum(g.values()) / len(g):.2f}'
    print(l)