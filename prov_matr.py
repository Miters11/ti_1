vhod = [[0, 1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0]]
a = []
kod_sekt=[0,1,1,1,0,1,1]
#while True:
    #a = [int(x) for x in input().split()]
    #if a == []:
        #break
    #vhod.append(a)
#print(vhod)
matr = {}
I_k={}
P = {}
stolb = [x for x in range(len(vhod[0]))][-1:len(vhod):-1]
stro=[x for x in range(len(vhod))][::-1]
pos_in_matr={stolb[i] : stro[i] for i in range(len(stro))}
for i in range(len(vhod[0])):
    kol = []
    for el in vhod:
        kol.append(el[i])
    matr[i]=kol
stolb_c=stolb
for i in matr.keys():
    if matr[i].count(1)==1 and matr[i].index(1) in stolb_c:
        stolb_c.pop(matr[i].index(1))
if len(stolb_c)!=0:
    exit()
for i in range(len(matr)-1,-1,-1):
    if matr[i].count(1)==1:
        if i in pos_in_matr.keys():
            if matr[i].index(1)==pos_in_matr[i]:
                continue
            else:
                i1 = list(pos_in_matr.keys())[list(pos_in_matr.values()).index(matr[i].index(1))]
                p1 = matr.pop(i1)
                i2 = i
                p2 = matr.pop(i2)
                matr[i2] = p1
                matr[i1] = p2
                matr = dict(sorted(matr.items()))
        else:
            i1=list(pos_in_matr.keys())[list(pos_in_matr.values()).index(matr[i].index(1))]
            p1=matr.pop(i1)
            i2=i
            p2=matr.pop(i2)
            matr[i2]=p1
            matr[i1]=p2
            matr=dict(sorted(matr.items()))
    else:
        continue
kol_in_sl=2**(len(vhod[0])-len(vhod))
P=list(matr.values())[:len(vhod[0])-len(vhod)]
I_k=list(matr.values())[len(vhod[0])-len(vhod):]
H_sys=[]
for i in range(len(vhod)):
    str_tr=[]
    for j in range(len(P)):
        str_tr.append(P[j][i])
    for j in range(len(I_k)):
        str_tr.append(I_k[j][i])
    H_sys.append(str_tr)
H_sys_t=[]
for i in range(len(H_sys[0])):
    str_tr=[]
    for j in range(len(H_sys)):
        str_tr.append(H_sys[j][i])
    H_sys_t.append(str_tr)
for i in range(len(I_k)):
    pov=len(P)-len(I_k[i])
    while pov!=0:
        I_k[i].append(0)
        pov-=1
while len(I_k)!=len(P):
    for i in range(len(P)-len(I_k)):
        new_str=[0]*len(P)
        new_str[P.index(P[-1])]=1
        I_k.append(new_str)
G_sys=[]
for i in range(len(vhod[0])-len(vhod)):
    G_sys.append(I_k[i]+P[i])
inf_sl = ['{0:b}'.format(x) for x in range(kol_in_sl)]
for i in range(len(inf_sl)):
    if len(inf_sl[i]) < max(len(y) for y in inf_sl):
        inf_sl[i] = '0' * (max(len(y) for y in inf_sl) - len(inf_sl[i])) + inf_sl[i]
inf_sl = [list(map(int, inf_sl[x])) for x in range(len(inf_sl))]
kod_sl = []
for i in range(len(inf_sl)):
    kod_slovo = []
    for j in range(len(G_sys[0])):
        pov = 0
        for k in range(len(G_sys)):
            if inf_sl[i][k] == G_sys[k][j] and inf_sl[i][k] == 1:
                pov += 1
        if pov % 2 != 0:
            kod_slovo.append(1)
        else:
            kod_slovo.append(0)
    kod_sl.append(kod_slovo)
tabl_kod_sl = {''.join(map(str, inf_sl[i])): ''.join(map(str, kod_sl[i])) for i in range(kol_in_sl)}
d_min = min([x.count(1) for x in kod_sl[1:]])
d_min_1 = d_min - 1
if d_min_1 % 2 != 0:
    d_min_1 -= 1
    t = d_min_1 / 2
else:
    t = d_min_1 / 2
vekt_osh = []
pos = 0
for i in range(len(G_sys[0])):
    e = [0] * len(G_sys[0])
    e[-1 - pos] = 1
    pos += 1
    vekt_osh.append(e)
syndr = []
for i in range(len(vekt_osh)):
    s = []
    for j in range(len(H_sys_t[0])):
        kol = 0
        pov = 0
        for k in range(len(H_sys_t)):
            if H_sys_t[k][j] == vekt_osh[i][pov] and H_sys_t[k][j] == 1:
                kol += 1
            pov += 1
        if kol % 2 != 0:
            s.append(1)
        else:
            s.append(0)
    syndr.append(s)
s = []
D = {''.join(map(str, syndr[i])): ''.join(map(str, vekt_osh[i])) for i in range(len(vhod[0]))}
for i in range(len(H_sys_t[0])):
    kol = 0
    pov = 0
    for j in range(len(H_sys_t)):
        if H_sys_t[j][i] == kod_sekt[pov] and H_sys_t[j][i] == 1:
            kol += 1
        pov += 1
    if kol % 2 != 0:
        s.append(1)
    else:
        s.append(0)
if s.count(1)==0:
    print(list(tabl_kod_sl.keys())[list(tabl_kod_sl.values()).index(''.join(map(str, kod_sekt)))])
else:
    syn=list(D[''.join(map(str, s))])
    kod_sll=[]
    for i in range(len(kod_sekt)):
        if int(kod_sekt[i])!=int(syn[i]):
            kod_sll.append(1)
        else:
            kod_sll.append(0)
    print(list(tabl_kod_sl.keys())[list(tabl_kod_sl.values()).index(''.join(map(str,kod_sll)))])
