input = input()

row=int(input[1])
col=input[0]

collist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = collist.index(col) + 1

steps = [
  (-2, -1), (-2, 1), (2, -1), (2, 1),
  (-1, 2), (1, 2), (-1, -2), (1, -2)
]

result = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <= 8:
    result += 1

print(result)