class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Inițializăm un rând cu toate valorile 1, având dimensiunea n (numărul de coloane).
        # Acest rând reprezintă numărul de căi pentru a ajunge la orice celulă din ultima linie.
        row = [1] * n

        # Iterăm prin fiecare rând, începând de la penultimul rând (de aceea iterăm de la m - 1).
        for i in range(m - 1):
            # Cream un nou rând (newRow) unde toate valorile inițiale sunt 1.
            # Acest nou rând va stoca numărul de căi pentru celulele din rândul curent.
            newRow = [1] * n

            # Parcurgem coloanele de la dreapta la stânga (de la n - 2 la 0),
            # pentru a actualiza valorile din newRow în funcție de valorile din rândul precedent și rândul curent.
            for j in range(n - 2, -1, -1):
                # Valoarea din newRow[j] este suma dintre celula din dreapta (newRow[j+1])
                # și celula corespunzătoare din rândul anterior (row[j]).
                newRow[j] = newRow[j+1] + row[j]

            # După ce am actualizat tot rândul, înlocuim row cu newRow pentru a trece la următorul rând.
            row = newRow

        # La final, row[0] va conține numărul total de căi pentru a ajunge de la începutul grilei (colțul stânga-sus)
        # până la final (colțul dreapta-jos).
        return row[0]
