class Solution:
    def rob(self, nums: List[int]) -> int:
        # Inițializăm rob1 și rob2 la 0, unde rob1 reprezintă suma maximă până la casa anterioară, iar rob2 suma până la casa curentă
        rob1, rob2 = 0, 0

        # Iterăm prin fiecare casă din lista de sume
        for n in nums:
            # Alegem între a jefui casa curentă și a păstra suma maximă de până acum
            temp = max(n + rob1, rob2)
            
            # Actualizăm rob1 pentru a deveni rob2 (casa anterioară devine acum curenta pentru următoarea iterație)
            rob1 = rob2
            
            # rob2 devine temp, care este suma maximă la momentul actual (după ce am ales dacă jefuim sau nu casa curentă)
            rob2 = temp

        # La final, rob2 conține suma maximă de bani pe care hoțul o poate obține
        return rob2
