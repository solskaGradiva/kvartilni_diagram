def preberi_stevila():
    stevila = []
    print("Vnesi zaporedje števil (vsako število v novi vrstici, prazna vrstica za konec):")
    try:
        while True:
            stevila.append(int(input()))
    except:
        pass
    return stevila

def razpolovi_na_mediani(stevila):
    pol = len(stevila) // 2

    if len(stevila) % 2 == 0:
        mediana = (stevila[pol - 1] + stevila[pol]) / 2
        manjsa_polovica = stevila[:pol]
        vecja_polovica = stevila[pol:]
    else:
        mediana = stevila[pol]
        manjsa_polovica = stevila[:pol]
        vecja_polovica = stevila[pol + 1:]

    return (mediana, manjsa_polovica, vecja_polovica)

def modus(stevila):
    max_ponovitve = (None, 0)
    for n in stevila:
        n_ponovitev = stevila.count(n)
        if n_ponovitev > max_ponovitve[1]:
            max_ponovitve = (n, n_ponovitev)
    return None if max_ponovitve[1] <= 1 else max_ponovitve[0]

def main():
    stevila = preberi_stevila()
    stevila.sort()

    if len(stevila) < 2:
        print("Vnesti je potrebno vsaj 2 števili!")
        exit()

    najmanjse = stevila[0]
    najvecje = stevila[-1]

    (q2, manjsa, vecja) = razpolovi_na_mediani(stevila)
    (q1, _, _) = razpolovi_na_mediani(manjsa)
    (q3, _, _) = razpolovi_na_mediani(vecja)

    print("urejena števila: ", stevila)
    print("min: ", najmanjse)
    print("max:", najvecje)
    print("VR:", najvecje - najmanjse)
    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("Q:", q3 - q1)
    print("modus:", modus(stevila))

main()
