def check_airport_code(S, T):
        from itertools import combinations
        
    
        S_upper = S.upper()
        
    
        for comb in combinations(range(len(S)), 3):
            if S_upper[comb[0]] + S_upper[comb[1]] + S_upper[comb[2]] == T:
                return "Yes"
        
        for comb in combinations(range(len(S)), 2):
            if S_upper[comb[0]] + S_upper[comb[1]] + "X" == T:
                return "Yes"
        
        return "No"

import sys
input = sys.stdin.read
data = input().split()
S = data[0]
T = data[1]

print(check_airport_code(S, T))