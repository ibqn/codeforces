
king_pos = input()
target_pos = input()

fields = "abcdefgh"

kx = fields.index(king_pos[0]) + 1
ky = int(king_pos[1])

tx = fields.index(target_pos[0]) + 1
ty = int(target_pos[1])

x_diff = tx - kx
y_diff = ty - ky

# left or right
lor = 'R' if x_diff > 0 else 'L'
# down or up
dou = 'U' if y_diff > 0 else 'D'

x_diff = abs(x_diff)
y_diff = abs(y_diff)
num_moves = max(x_diff, y_diff)

print(num_moves)

for i in range(num_moves):
    if x_diff > 0: print(lor, end='') 
    if y_diff > 0: print(dou, end='')
    print('')
    x_diff -= 1
    y_diff -= 1

