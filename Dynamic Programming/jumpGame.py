class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Inițializăm variabila goal cu ultima poziție din vector (aceasta este ținta pe care vrem să o atingem)
        goal = len(nums) - 1

        # Parcurgem vectorul de la dreapta (de la final) spre stânga (spre început)
        for i in range(len(nums) - 1, -1, -1):
            # Verificăm dacă putem ajunge de la poziția curentă 'i' la poziția goal sau mai departe
            # Dacă da, actualizăm goal la poziția curentă 'i', indicând că acum ținta este de a ajunge la 'i'
            if i + nums[i] >= goal:
                goal = i
            
        # Dacă la final goal este 0, înseamnă că putem ajunge de la începutul vectorului la capăt
        return True if goal == 0 else False
