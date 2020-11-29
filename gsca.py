import numpy as np
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt



def gsca(pow,ti,tp,tl,tr,al,gam,w, woj,osoby, ur, um, dead):

    powiazanie = pd.read_csv(r'{0}.csv'.format(pow))
    generalna = pd.read_csv(r'generalna.csv')
    granice = pd.read_csv(r'granice.csv')

    P = np.arange(ti + tp + tl + tr + 1)
    t = 200
    p = 123
    k = 16
    K = np.arange(0.0, 1.01, 0.01)

    N = np.zeros(k)
    A = np.zeros(k)
    for i in range(k):
        N[i] = generalna['populacja'][i]
        A[i] = generalna['powierzchnia'][i]

    M = np.zeros((k, len(P)))
    G = np.zeros((k, len(P)))
    K = np.zeros((t,k))
    Alfa = np.zeros(len(P))
    Gamma = np.zeros(len(P))
    for i in range(len(P)):
        Alfa[i] = al
        Gamma[i] = gam

    def cij(r1, r, w, pow):
        g = granice['{0}'.format(r1)][r]
        n = powiazanie['{0}'.format(r1)][r]
        lx = generalna['obwody'][r1]
        ly = generalna['obwody'][r]
        if pow == 'brak':
            if g == 0 and n == 0:
                return 0
            if g == 0 and n == 1:
                return 0
            if g != 0 and n == 0:
                c = (1 - w) * ((g / lx + g / ly) / 2)
                return c
            if g != 0 and n == 1:
                c = np.maximum(0.3 * (1 - w), (1 - w)*((g / lx + g / ly) / 2))
                return c
        if pow == 'drogi':
            if g == 0 and n == 0:
                return 0
            if g == 0 and n == 1:
                return 0.3*(1-w)
            if g != 0 and n == 0:
                c = (1 - w)*((g / lx + g / ly) / 2)
                return c
            if g != 0 and n == 1:
                c = np.maximum(0.3 * (1 - w), (1 - w)*((g / lx + g / ly) / 2))
                return c

        if pow == 'kolej':
            if g == 0 and n == 0:
                return 0
            if g == 0 and n == 1:
                return 0.3*(1-w)
            if g != 0 and n == 0:
                c = (1 - w)*((g / lx + g / ly) / 100)
                return c
            if g != 0 and n == 1:
                return 0.3*(1-w)
        if pow == 'lotnictwo':
            if g == 0 and n == 0:
                return 0
            if g == 0 and n == 1:
                return 0.05*(1-w)
            if g != 0 and n == 0:
                c = (1 - w) * ((g / lx + g / ly) / 100)
                return c
            if g != 0 and n == 1:
                return 0.05*(1-w)

    # założenia początkowe
    for i in range(k):
        M[i][0] = 1.0

    M[woj][1] = osoby/N[woj]
    M[woj][0] = 1.0 - osoby/N[woj]

    cbaza = np.zeros((t, k, len(P)))

    for t in range(0, t):
        baza = np.zeros((k, len(P)))

        d = 0
        for i in range(0, k):

            S = M[i][0]
            I = np.zeros(ti + tp + tl + tr + 1)
            R = np.zeros(ti + tp + tl + tr + 1)
            for h in range(1, ti + tp + tl + 1):
                I[h] = M[i][h]
            for r in range(ti + tp + tl + 1, ti + tp + tl + tr + 1):
                R[r] = M[i][r]

            N[i] += N[i] * ur
            N[i] -= N[i] * um
            nS = [0]
            nI = np.zeros(len(P) + 1)
            nR = np.zeros(len(P) + 1)
            IR = I + R
            IR[0] = S
            baza[i] = IR * N[i]

            for q in range(ti + tp + tl + 2, ti + tp + tl + tr + 1):
                nR[q] = R[q - 1]

            pt = (S * N[i]) / A[i]

            a = sum(sum(((Alfa[q] * cij(i, jj, w, pow) * pt * S * M[jj][q]) / p) for q in range(1, ti + tp + tl + 1)) for jj in
                    range(k))

            b = sum(((Alfa[q] * pt * S * I[q]) / p) for q in range(1, ti + tp + tl + 1))

            nS = S - b + R[ti + tp + tl + tr] - a
            nI[1] = b + a - (b+a) * dead

            for q in range(2, ti + tp + tl + 1):
                nI[q] = (1 - Gamma[q - 1] - dead) * I[q - 1]

            nR[ti + tp + tl + 1] = I[ti + tp + tl] + sum(Gamma[q] * I[q] for q in range(1, ti + tp + tl))

            G[i][0] = nS
            for h in range(1, ti + tp + tl + 1):
                G[i][h] = nI[h]
            for r in range(ti + tp + tl + 1, ti + tp + tl + tr + 1):
                G[i][r] = nR[r]




            K[t][i] = N[i]

        for i in range(k):
            M[i][0] = G[i][0]
            for h in range(1, ti + tp + tl + 1):
                M[i][h] = G[i][h]
            for r in range(ti + tp + tl + 1, ti + tp + tl + tr + 1):
                M[i][r] = G[i][r]


        cbaza[t] = baza

    wI = np.zeros(t)
    wR = np.zeros(t)
    wS = np.zeros(t)
    x = np.arange(t)
    y = np.zeros((t, k))
    populacja = np.zeros(t)
    for i in range(0, t):
        II = 0
        RR = 0
        SS = 0
        di = np.zeros(k)
        pop = 0
        for a in range(0, k):
            DS = (100 * cbaza[i][a][0]) / 100
            DI = sum(cbaza[i][a][q] for q in range(1, ti + tp + tl + 1))
            DR = sum(cbaza[i][a][q] for q in range(ti + tp + tl + 1, ti + tp + tl + tr + 1))
            pop += K[i][a]
            II += DI
            RR += DR
            SS += DS
            di[a] = DI
        y[i] = di
        populacja[i] = pop
        wI[i] = II
        wS[i] = SS
        wR[i] = RR


    def save():
        l = []
        for i in range(0, 191, 5):
            l.append(i)
        for i in l:
            id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            t = y[i]
            infected = [t[4], t[12], t[14], t[1], t[5], t[0], t[2], t[3], t[6], t[7], t[9], t[10], t[11], t[8], t[13],
                        t[15]]

            dict = {'ID_1': id, 'infected{0}'.format(i): infected}
            df = pd.DataFrame(dict)
            df.to_csv(r'C:\Users\PC\PycharmProjects\GSCA\all_files\file{0}.csv'.format(i))
        dict2 = {'S':wS, 'I':wI, 'R':wR, 'P':populacja}
        dok = pd.DataFrame(dict2)
        dok.to_csv(r'C:\Users\PC\PycharmProjects\GSCA\SIR.csv')

    save()



    plt.style.use('seaborn')
    plt.plot(x, wI, 'r', x, wS, 'b', x, wR, 'g')
    plt.grid(True)
    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title('Spread of the disease')
    plt.legend(('Infected', 'Susceptible', 'Recovered'),
               )
    # plt.savefig(r"c://Users/PC/Desktop/image1.png")
    plt.show()

    plt.style.use('seaborn')
    plt.plot(x, wI, 'r')
    plt.legend('Infected')
    plt.grid(True)
    plt.xlabel('Days')
    plt.ylabel('Population')
    plt.title('Total active cases')
    # plt.savefig(r"c://Users/PC/Desktop/image2.png")
    plt.show()

    return'ok'

