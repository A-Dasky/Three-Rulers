imp = 'hero_house'
with open(imp + '.w', 'w') as w:
    # height
    for i in range(11):
        # width
        for j in range(14):
            w.write('F')
        w.write('\n')
