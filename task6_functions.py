def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

result = calculate_total_sales(video_game_sales[0])
print(result)

def filter_by_genre(data, genre='Platform'):
    filtered = []
    for row in data:
        if row[4] == genre:   # genre column
            filtered.append(row)
    return filtered
    platform_games = filter_by_genre(video_game_sales)
print(PLATFORM)

def get_summary(game):
    name = game[1]
    year = game[3]
    genre = game[4]
    global_sales = game[9]
    return f"{name} ({year}) - {genre} - ${global_sales}M"
