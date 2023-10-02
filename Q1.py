from itertools import permutations

lst = [1, 2, 3, 4, 5, 6, 7, 8]

permutations_list = list(permutations(lst, len(lst)))

occurences = 0
nonOccurences = 0
for combo in permutations_list:
  abcde = 1
  fgh = 1
  
  abcde = combo[0] * combo[1] * combo[2] * combo[3] * combo[4]
  fgh = combo[5] * combo[6] * combo[7]
  if abcde < fgh:
    occurences += 1
  elif fgh <= abcde:
    nonOccurences += 1


prob = occurences/len(permutations_list)
print(prob)

