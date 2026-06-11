game_names = []

for row in video_game_sales:
    game_names.append(row[NAME])

print(game_names)

video_game_sales.append(
    [21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo',
     7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

# A tuple is more appropriate than a list because this information should not change. 
# Tuples are immutable, so they protect the dataset details from being modified accidentally. 
dataset_info = (len(video_game_sales), 
10, 'Video Game Sales') 
print(dataset_info)
