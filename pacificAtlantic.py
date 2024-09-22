class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Determinăm numărul de rânduri și coloane din matricea heights.
        ROWS, COLS = len(heights), len(heights[0])
        
        # Două seturi pentru a ține evidența celulelor vizitate pentru Pacific și Atlantic.
        pac, atl = set(), set()

        # Funcție de explorare DFS (Depth First Search).
        def dfs(r, c, visit, prevHeight):
            # Condiții de stopare a recursivității:
            # - Dacă am vizitat deja această celulă
            # - Dacă celula este în afara limitelor matricei
            # - Dacă celula curentă este mai mică decât celula anterioară, ceea ce înseamnă că apa nu poate curge.
            if((r,c) in visit or
               r < 0 or c < 0 or r == ROWS or c == COLS or
               heights[r][c] < prevHeight):
                return
            
            # Adăugăm celula curentă în setul de vizite
            visit.add((r,c))
            
            # Recursiv apelăm DFS pentru vecinii din cele 4 direcții (sus, jos, stânga, dreapta).
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        # Pentru fiecare coloană de pe prima linie (Pacific) și ultima linie (Atlantic)
        # facem DFS pentru a vedea care celule pot atinge fiecare ocean.
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])             # Pacific (partea de sus)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Atlantic (partea de jos)
    
        # Pentru fiecare rând de pe prima coloană (Pacific) și ultima coloană (Atlantic)
        # facem DFS pentru a vedea care celule pot atinge fiecare ocean.
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])              # Pacific (partea din stânga)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Atlantic (partea din dreapta)
        
        # Inițializăm o listă pentru rezultatul final.
        res = []
        
        # Verificăm fiecare celulă din matrice. Dacă o celulă este vizibilă atât din Pacific, cât și din Atlantic,
        # o adăugăm la lista de rezultate.
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        
        # Returnăm lista cu celulele din care apa poate curge în ambele oceane.
        return res
