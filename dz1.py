def rgb(r, g, b):
    return f'\u001B[38;2;{r};{g};{b}m'

print(rgb(255, 0, 0) + 'A', rgb(10, 120, 200) + 'B', rgb(0, 255, 0) + '&', rgb(255, 255, 0) + '|', \
      rgb(0, 0, 255) + '^', rgb(255, 170, 0) + '~a', rgb(80, 0, 132) + 'a<<',  rgb(240, 132, 240) + 'a>>')
for a in 0,1:
    for b in 0,1:
        f1 = a & b
        f2 = a | b
        f3 = a ^ b
        f4 = ~a
        f5 = a << 1
        f6 = a >> 1
        print(rgb(255, 0, 0) + str(a), rgb(10, 120, 200) + str(b), rgb(0, 255, 0) + str(f1), \
              rgb(255, 255, 0) + str(f2), rgb(0, 0, 255) + str(f3), rgb(255, 170, 0) + str(f4), " ", rgb(80, 0, 132) + str(f5), \
                " ", rgb(240, 132, 240) + str(f6))
print(rgb(0, 0, 0))