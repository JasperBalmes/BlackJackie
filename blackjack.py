fname = "probability.txt"
handle = open(fname)
htot = input('\nEnter draw here:')
htot = int(htot)

try:
    if htot == 21:
        print('\n\nWinner Winner Chicken Dinner! \n')
    elif 11 <= htot <= 20 :
        print('\nYour probability of winning with')
    elif htot < 11  :
        print('Thats too low \n')
    else:
        print('Invalid')
except:
    print('Invalid')
word = list()
cp = dict()
hlp = dict()
hgp = dict()
for line in handle:
    if line.startswith('cp'):
        words = line.rstrip().split(' ')
        word = words[0].split()
        word[1] = int(word[1])
        cp[word[1]] = word[2]
    if line.startswith('hw'):
        hwords = line.rstrip().split(' ')
        hword = hwords[0].split()
        hword[1] = int(hword[1])
        hlp[hword[1]] = hword[2]
        hgp[hword[1]] = hword[3]
for k,v in cp.items():
    if k == htot:
        htotprob = v
        print ('\nHand:', htot)
        print ('is at ', htotprob)

if htot < 17:
    print ('\n\nI suggest you hit \n')
if 21> htot > 17:
    print ('\n \n Your cards are high enough, I suggest you dont hit \n')
hit = input("Do you want to hit? \n")
hit = hit.lower()
if hit == "yes":
    dc = input("What is the dealers card? \n")
    dc = int(dc)
    hprob = 0
    lprob = 0
    for k,v in hlp.items():
        if k == dc:
            lprob = v
            print("If the dealers card is less than",dc, "your probability of winning on the hit is \n", lprob )
    for k,v in hgp.items():
        if k == dc:
            gprob = v
            print("If the dealers SECOND card is greater than or equal to",dc, "your probability of winning on the hit is \n", gprob )
            print('Good luck!')
else:
    print('Good luck!')
