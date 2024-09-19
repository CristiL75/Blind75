class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # `dp[i]` va reprezenta dacă subșirul `s[i:]` poate fi divizat în cuvinte din `wordDict`.
        # Inițializăm un vector `dp` de lungime `len(s) + 1`, cu toate valorile False.
        dp = [False] * (len(s) + 1)

        # dp[len(s)] = True, deoarece un șir gol poate fi întotdeauna divizat (cazul de bază).
        dp[len(s)] = True

        # Iterăm invers prin șirul `s`, pornind de la penultimul caracter până la primul.
        for i in range(len(s) - 1, -1, -1):
            # Pentru fiecare poziție `i`, verificăm toate cuvintele din `wordDict`.
            for w in wordDict:
                # Dacă lungimea cuvântului `w` se potrivește cu secvența curentă `s[i : i + len(w)]`...
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # Dacă subșirul de la `i + len(w)` poate fi divizat, atunci și subșirul de la `i` poate fi divizat.
                    dp[i] = dp[i + len(w)]
                
                # Dacă am găsit un cuvânt care permite divizarea de la `i`, ieșim din bucla interioară.
                if dp[i]:
                    break

        # Returnăm valoarea din `dp[0]`, care ne spune dacă întregul șir poate fi divizat.
        return dp[0]
