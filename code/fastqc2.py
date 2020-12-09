read = open('fastqc_data.txt')
switch = False
summary = []
thing = []
things = []
for line in read:
    if line.startswith('>>'):
        if switch == True:
            switch = False
            things.append(thing)
            thing = []
            summary.append(line.strip())
        else:
            switch = True
    if switch:
        thing.append(line.strip())

dicti = {}
for a, i in enumerate(things):
    if a == 3: #het nummer van het grafiekje waar je data van wil
        for b, i in enumerate(i):
            if b > 2: #meer dan 1, laat de header en kopjes weg
                ye = i.split('\t')[0:5]
                new = []
                for c, i in enumerate(ye):
                    if c in dicti.keys():
                        dicti[c].append(float(i))
                    else:
                        dicti[c] = [float(i)]

lijst = []
for i in range(1, 5):
    for a, num in enumerate(dicti[i]):
        if not a == 0:
            diff = num - old   #prints the difference in a c t g percentages per nucleotide
            if diff > 1.5:
                print('yes')
            else:
                print('no')
        old = num
    print('')
        
        
