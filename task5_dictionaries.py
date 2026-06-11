sales_by_genre = {}

for row in video_game_sales:
    genre = row[4]
    global_sales = row[9]

    if genre not in sales_by_genre:
        sales_by_genre[genre] = 0

    sales_by_genre[genre] += global_sales

print(sales_by_genre)

games_per_publisher = {}

for row in video_game_sales:
    publisher = row[5]

    if publisher not in games_per_publisher:
        games_per_publisher[publisher] = 0

    games_per_publisher[publisher] += 1

print(games_per_publisher)

top_row = video_game_sales[0]

top_game = {
    'name': top_row[1],
    'year': top_row[3],
    'genre': top_row[4],
    'publisher': top_row[5],
    'global_sales': top_row[9]
}
