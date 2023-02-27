vhod = []
a = []
while True:
    a = [int(x) for x in input().split()]
    if a == []:
        break
    vhod.append(a)
pam = {}
zam = {}
stolb = [x for x in range(len(vhod))]
for i in range(len(vhod[0])):
    kol = []
    for el in vhod:
        kol.append(el[i])
    if kol.count(1) == 1 and kol.index(1) in stolb:
        zam[i] = kol
    else:
        pam[i] = kol
for i in stolb:
    if i in zam.keys():
        continue
    else:
        pam[list(zam.keys())[i]] = pam[i]
        del pam[i]
        zam[i] = zam[list(zam.keys())[i]]
        del zam[list(zam.keys())[i]]
        pam = dict(sorted(pam.items()))
        zam = dict(sorted(zam.items()))
vhod_pov = []
for i in range(len(vhod)):
    st = []
    for key in zam.keys():
        st.append(zam[key][i])
    for key in pam.keys():
        st.append(pam[key][i])
    vhod_pov.append(st)

if len(vhod) % 2 != 0 and len(pam) - len(zam) > 0:
    for key in zam.keys():
        pov = len(pam) - len(zam)
        while pov != 0:
            zam[key].append(0)
            pov -= 1
    while len(zam) != len(pam):
        for i in range(len(pam) - len(zam)):
            new_str = [0] * len(pam)
            new_str[list(zam.keys())[-1] + 1] = 1
            zam[list(zam.keys())[-1] + 1] = new_str
    h_sys = []
    for i in range(len(zam)):
        h_sys.append(pam[list(pam.keys())[i]] + zam[list(zam.keys())[i]])
    h_sys_t = []
    for i in range(len(pam[list(pam.keys())[0]])):
        strok = []
        for j in pam.keys():
            strok.append(pam[j][i])
        h_sys_t.append(strok)
    for i in range(len(zam)):
        h_sys_t.append(zam[list(zam.keys())[i]])
    kol_in_sl = 2 ** len(vhod)
    inf_sl = ['{0:b}'.format(x) for x in range(kol_in_sl)]
    for i in range(len(inf_sl)):
        if len(inf_sl[i]) < max(len(y) for y in inf_sl):
            inf_sl[i] = '0' * (max(len(y) for y in inf_sl) - len(inf_sl[i])) + inf_sl[i]
    inf_sl = [list(map(int, inf_sl[x])) for x in range(len(inf_sl))]
    kod_sl = []
    for i in range(len(inf_sl)):
        kod_slovo = []
        for j in range(len(vhod_pov[0])):
            pov = 0
            for k in range(len(vhod_pov)):
                if inf_sl[i][k] == vhod_pov[k][j] and inf_sl[i][k] == 1:
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
    # print(int(t))
    vekt_osh = []
    pos = 0
    for i in range(kol_in_sl - 1):
        e = [0] * len(vhod[0])
        e[-1 - pos] = 1
        pos += 1
        vekt_osh.append(e)
    syndr = []
    for i in range(len(vekt_osh)):
        s = []
        for j in range(len(h_sys_t[0])):
            kol = 0
            pov = 0
            for k in range(len(h_sys_t)):
                if h_sys_t[k][j] == vekt_osh[i][pov] and h_sys_t[k][j] == 1:
                    kol += 1
                pov += 1
            if kol % 2 != 0:
                s.append(1)
            else:
                s.append(0)
        syndr.append(s)
    kod_sekt = [int(x) for x in input().split()]
    s = []
    D = {''.join(map(str, syndr[i])): ''.join(map(str, vekt_osh[i])) for i in range(kol_in_sl - 1)}
    for i in range(len(h_sys_t[0])):
        kol = 0
        pov = 0
        for j in range(len(h_sys_t)):
            if h_sys_t[j][i] == kod_sekt[pov] and h_sys_t[j][i] == 1:
                kol += 1
            pov += 1
        if kol % 2 != 0:
            s.append(1)
        else:
            s.append(0)
    c = bin(int(''.join(map(str, kod_sekt)), 2) + int(''.join(map(str, D[''.join(map(str, s))])), 2))
    c = '0' * (len(vekt_osh[0]) - len(c[2:])) + c[2:]
    print(list(tabl_kod_sl.keys())[list(tabl_kod_sl.values()).index(c)])
