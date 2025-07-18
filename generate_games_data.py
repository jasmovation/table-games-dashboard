import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_rows = 200
start_date = datetime(2025, 1, 1)
game_types = ['Chess', 'Checkers', 'Dominoes', 'Poker', 'Go', 'Mahjong']
regions = ['North', 'South', 'East', 'West']

# Optional color mapping by game (if you want it)
colors = {
    'Chess': 'Black',
    'Checkers': 'Red',
    'Dominoes': 'Gray',
    'Poker': 'Green',
    'Go': 'White',
    'Mahjong': 'Teal'
}

# Generate data
data = []
for _ in range(num_rows):
    date = start_date + timedelta(days=random.randint(0, 90))
    game = random.choice(game_types)
    color = colors[game]
    region = random.choice(regions)
    quantity = random.randint(1, 20)
    revenue = quantity * random.randint(80, 150)  # Assume $80–$150 per game session

    data.append({
        'Date': date.strftime('%Y-%m-%d'),
        'GameType': game,
        'Color': color,
        'Region': region,
        'QuantitySold': quantity,
        'Revenue': revenue
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("table_games_data.csv", index=False)
print("✅ Synthetic Table Games data saved as table_games_data.csv")
