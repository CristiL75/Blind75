class Solution:
    # Funcția principală care rezolvă problema House Robber II
    # Lista valorilor caselor (nums) este transmisă ca argument de intrare
    def rob(self, nums: List[int]) -> int:
        # Caz de margine: Dacă există doar o casă, returnează valoarea acelei case.
        if len(nums) == 1:
            return nums[0]

        # Problema principală este împărțită în două cazuri deoarece casele sunt într-un cerc:
        # 1. Fie furăm de la casa 1 la casa n-1 (adică, omitem ultima casă)
        # 2. Sau furăm de la casa 2 la casa n (adică, omitem prima casă)

        # Returnăm maximul dintre aceste două cazuri, luând în considerare și valoarea primei case
        # dacă există doar o casă.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    # Funcția helper care rezolvă problema obișnuită "House Robber" (fără constrângerea de cerc)
    @staticmethod
    def helper(nums: List[int]) -> int:
        # rob1 și rob2 păstrează evidența sumei maxime de bani care pot fi furați
        # rob1: Suma maximă furată de la prima casă până la penultima casă
        # rob2: Suma maximă furată de la prima casă până la ultima casă

        rob1, rob2 = 0, 0  # Inițializăm cu 0 deoarece inițial nu am furat nicio casă.

        # Parcurgem fiecare casă din listă
        for n in nums:
            # Pentru fiecare casă, calculăm suma maximă care poate fi furată fie:
            # - Furând de la casa curentă (rob1 + n), fie
            # - Sărind peste casa curentă (rob2)

            # newRob stochează valoarea actualizată a sumei maxime furate până acum
            newRob = max(rob1 + n, rob2)
            
            # Actualizăm rob1 cu valoarea lui rob2 (shiftăm în față)
            rob1 = rob2

            # rob2 devine suma maximă furată până acum (adică, newRob)
            rob2 = newRob
        
        # rob2 conține acum suma maximă care poate fi furată din secvența de case
        return rob2
