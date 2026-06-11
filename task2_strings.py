messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

game_name = video_game_sales [4] [NAME]
print(game_name[:7]) 

for name in messy_names:
    cleaned = name.strip().lower()
    print(cleaned)
    
game = "Wii Sports"
year = 2006
sales = 82.74

print(f"#1 Best Seller: {game} ({year}) - ${sales}M global sales")
