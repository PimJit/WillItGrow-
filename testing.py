litter = ["tom","hank","walter","wilson","jack"]
chosen =[]
total =0
while len(chosen) < 3:
    for cat in litter:
        chosen.append(cat)
        if 1 < len(chosen) < 3:
            break
    if len(chosen) < 3:
        print(chosen)
        break
