class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convertim lista de numere într-un set pentru a avea acces O(1) la fiecare element.
        numSet = set(nums)
        
        # Inițializăm variabila 'longest' care va stoca lungimea maximă a unei secvențe consecutive.
        longest = 0
        
        # Iterăm prin fiecare număr din lista originală.
        for n in nums:
            # Verificăm dacă (n - 1) nu se află în set. 
            # Acest lucru ne indică faptul că 'n' poate fi începutul unei secvențe noi.
            if (n - 1) not in numSet:
                # Inițializăm lungimea secvenței la 0.
                length = 0
                
                # Cât timp (n + length) este în set, creștem lungimea secvenței.
                # În acest fel, găsim cât de lungă este secvența consecutivă începând de la 'n'.
                while (n + length) in numSet:
                    length += 1
                
                # Actualizăm variabila 'longest' dacă lungimea secvenței curente este mai mare decât cea maximă de până acum.
                longest = max(length, longest)
        
        # Returnăm cea mai lungă secvență consecutivă găsită.
        return longest
