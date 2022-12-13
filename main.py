# функция, возвращающая координаты персонажа
def check_position(game_map):
     for y in range(len(game_map)):
          for x in range(len(game_map)):
               if game_map[y][x] == 'h':
                    return [y, x]


# функция, анализирующая соседей
def check_neighbour_place(game_map, pos_now):
     if pos_now[0] > 0:
          upper = game_map[pos_now[0]-1][pos_now[1]]  # проверяем что выше на 1 по y
     else:
          upper = 'b'

     if pos_now[0] < 3:
          lower = game_map[pos_now[0]+1][pos_now[1]]  # проверяем что ниже на 1 по y
     else:
          lower = 'b'

     if pos_now[1] < 3:
          righter = game_map[pos_now[0]][pos_now[1]+1]  # проверяем что правее на 1 по x
     else:
          righter = 'b'

     if pos_now[1] > 0:
          lefter = game_map[pos_now[0]][pos_now[1]-1]  # проверяем что левее на 1 по x
     else:
          lefter = 'b'

     return [upper, lower, righter, lefter]


# функция, выбирающая самый выгодный путь
def move(pos_now):
     neighbours = check_neighbour_place(A, pos_now)
     rating_ways = []

     for n in neighbours:  # составляем рейтинг выгодных путей
          if n == 'c':
               rating_ways.append(2)
          elif n == 'l':
               rating_ways.append(1)
          elif n == 'b':
               rating_ways.append(-999999)
          elif n == 'o':
               rating_ways.append(-1)
          else:
               rating_ways.append(0)

     max_index = rating_ways.index(max(rating_ways))  # находим самый выгодный путь
     print(max(rating_ways))
     global old_pos

     if max_index == max(rating_ways) == -1:
          return False

     if max_index == 0:
          A[pos_now[0]][pos_now[1]] = old_pos  # назначаем текущей позиции значение посещённой
          A[pos_now[0]-1][pos_now[1]] = 'h'  # ставим персонажа на одну клетку выше

     elif max_index == 1:
          A[pos_now[0]][pos_now[1]] = old_pos  # назначаем текущей позиции значение посещённой
          A[pos_now[0]+1][pos_now[1]] = 'h'  # ставим персонажа на одну клетку ниже

     elif max_index == 2:
          A[pos_now[0]][pos_now[1]] = old_pos  # назначаем текущей позиции значение посещённой
          A[pos_now[0]][pos_now[1]+1] = 'h'  # ставим персонажа на одну клетку правее

     elif max_index == 3:
          A[pos_now[0]][pos_now[1]] = old_pos  # назначаем текущей позиции значение посещённой
          A[pos_now[0]][pos_now[1]-1] = 'h'  # ставим персонажа на одну клетку левее
     # print(A)


# s - smell, g - gap, m - wampus (monster), w - wind, l - land (nothing), h - hero, e - exit, c - coin
# b - border
A = [['c', 'w', 'l', 'e'],
     ['w', 'g', 'ws', 'm'],
     ['l', 'w', 'c', 's'],
     ['h', 'c', 's', 'l']]

old_pos = 'o'  # уже пройденная клетка

# print(check_neighbour_place(A, check_position(A)))

count = 0
while True:
     move(check_position(A))
     count += 1
     p_n = A[check_position(A)[0]][check_position(A)[1]]
     if p_n == 'g' or p_n == 'm':
          print('U lost :(')
          break
     elif p_n == 'e':
          print('U won!')

# print(check_position(A))
# print(old_pos)
