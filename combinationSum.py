class Solution:
    def combinationSum4(self, candidates: List[int], target: int) -> int:
        # dp[i] va reprezenta numărul de moduri în care putem obține suma `i` folosind elementele din `candidates`.
        dp = [0] * (target + 1)
        dp[0] = 1  # Există 1 mod de a obține suma 0 (prin a nu lua nimic).

        # Parcurgem toate sumele de la 1 până la `target`
        for i in range(1, target + 1):
            for num in candidates:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
