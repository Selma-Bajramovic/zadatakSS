from collections import deque

def minKoraka(pocetak, cilj):
    def pronadjiSusjedne(stanje):
        susjedni = []
        pozNula = stanje.index(0) # pronalazi trenutnu nulu
        row, col = pozNula // N, pozNula % N  # pozicije reda i kolone
        
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # provjerava sve moguce smjerove
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < N and 0 <= newCol < N: # provjerava je li row i col u granicama matrice 
                novaNula = newRow * N + newCol  # racuna novu nulu
                novoStanje = list(stanje)  # postavlja novo trenutno stanje
                novoStanje[pozNula], novoStanje[novaNula] = novoStanje[novaNula], novoStanje[pozNula] # mijenja nulu sa novom pozicijom
                susjedni.append(tuple(novoStanje))  # dodaje novo stanje u listu
        
        return susjedni

    N = int(len(pocetak) ** 0.5)  # racuna dim matrice
    pocetak = tuple(pocetak)
    cilj = tuple(cilj)  # mijenjamo tip podatka u tuple
    
    if pocetak == cilj:
        return 0  # ako su pocetak i cilj isti da ne radi nista
    
    red = deque([(pocetak, 0)])  # inicijalizacija reda sa pocetnim stanjem i 0 koraka
    posjecena = set()  # prati posjecena stanja
    posjecena.add(pocetak)  # dodaje pocetak u posjecene
    
    while red:
        trenutno, koraci = red.popleft()  # uklanja trenutno stanje iz reda i vraca korake
        
        for susjedniPrvi in pronadjiSusjedne(trenutno):  # pregledava sve susjedne
            if susjedniPrvi == cilj:
                return koraci + 1  # ako je dosao do cilja dodaje +1 korak
            if susjedniPrvi not in posjecena:
                posjecena.add(susjedniPrvi)  # dodaje novo stanje u posjecene
                red.append((susjedniPrvi, koraci + 1))  # dodaje novo stanje u red i povecava brojac koraka
    
    return -1  # ako nema rjesenje vraca -1

# test na vasem primjeru
pocetak = [2, 0, 1, 3]
cilj = [3, 1, 0, 2]
print(minKoraka(pocetak, cilj))  
