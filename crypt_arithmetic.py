for S in range(1, 10):
    for E in range(10):
        for N in range(10):
            for D in range(10):
                for M in range(1, 10):
                    for O in range(10):
                        for R in range(10):
                            for Y in range(10):

                                digits = [S,E,N,D,M,O,R,Y]
                                if len(set(digits)) != 8:
                                    continue

                                SEND = 1000*S + 100*E + 10*N + D
                                MORE = 1000*M + 100*O + 10*R + E
                                MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

                                if SEND + MORE == MONEY:
                                    print("Solution Found")
                                    print("SEND =", SEND)
                                    print("MORE =", MORE)
                                    print("MONEY =", MONEY)
                                    exit()
