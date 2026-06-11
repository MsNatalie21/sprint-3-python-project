total_games = len(video_game_sales)
print(total_games)

total_global_sales = 0

for game in video_game_sales:
    total_global_sales += game[GLOBAL_SALES]

avg_global_sales = total_global_sales / len(video_game_sales)
print("Avg global sales:", avg_global_sales)

top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_global_sales) * 100
print(top_game_share)
