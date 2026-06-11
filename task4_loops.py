for row in video_game_sales:
    name = row[1]
    global_sales = row[9]

    if global_sales > 25:
        print(name, global_sales)

pre_2000_count = 0

for row in video_game_sales:
    year = row[YEAR]
    if year < 2000:
        pre_2000_count += 1

print(pre_2000_count)

nintendo_games = []

for row in video_game_sales:
    if row[5] == 'Nintendo':      # publisher column
        nintendo_games.append(row[1])   # game name column

print(nintendo_games)
print(len(nintendo_games))
for game in nintendo_games:
    print(game)
