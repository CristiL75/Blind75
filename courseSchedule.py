class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creăm un dicționar care mapează fiecare curs la lista sa de precondiții.
        # Fiecare curs va avea o listă inițial goală de precondiții.
        preMap = { i:[] for i in range(numCourses)}

        # Parcurgem lista de precondiții și populăm preMap cu fiecare relație (crs -> pre)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = un set care ține evidența tuturor cursurilor aflate pe calea curentă DFS.
        visitSet = set()

        # Funcția DFS pentru verificarea ciclurilor
        def dfs(crs):
            # Dacă cursul este deja în visitSet, înseamnă că avem un ciclu (nu putem termina cursul).
            if crs in visitSet:
                return False
            # Dacă cursul curent nu are precondiții, înseamnă că îl putem finaliza.
            if preMap[crs] == []:
                return True
            
            # Adăugăm cursul curent în visitSet, indicând că suntem în proces de a-l explora.
            visitSet.add(crs)
            # Verificăm toate precondițiile pentru cursul curent.
            for pre in preMap[crs]:
                # Dacă una din precondiții nu poate fi finalizată, întoarcem False.
                if not dfs(pre): return False
            # Scoatem cursul din visitSet după ce l-am explorat.
            visitSet.remove(crs)
            # Odată ce cursul a fost validat că poate fi finalizat, setăm lista sa de precondiții ca fiind goală (marcăm că a fost procesat).
            preMap[crs] = []
            # Întoarcem True, indicând că cursul poate fi finalizat.
            return True

        # Apelăm DFS pentru fiecare curs. Dacă pentru oricare curs găsim un ciclu, întoarcem False.
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        # Dacă nu s-au găsit cicluri, putem finaliza toate cursurile.
        return True
