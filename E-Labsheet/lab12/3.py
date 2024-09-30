nl = []
fmax = 0

while True:
    n = input()
    if n == "-1":
        break
    font, back = n.split('=' , 1)
    font = font.strip()
    back = back.strip()
    if back.isdigit():
        back = int(back)
    nl.append((font, back))
    fmax = max(fmax, len(font))

for font, back in nl:
    print(f"{font:>{fmax}} = {back}")

