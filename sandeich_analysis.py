import pandas as pd

# 1. Bread Preferences - 12 values each
bread_data = {
    'Rye': [34, 65, 58, 57, 21, 29, 36, 59, 47, 42, 41, 42],
    'Multi Grain': [47, 63, 59, 76, 26, 28, 38, 19, 60, 36, 22, 42],
    'White': [67, 65, 18, 31, 54, 48, 22, 50, 45, 36, 44, 27],
    'Whole Grain': [51, 57, 48, 21, 53, 42, 24, 66, 25, 48, 40, 59],
}

# 2. Spread Preferences - 16 values each
spread_data = {
    'Ham and Gherkins': [34, 67, 63, 65, 58, 59, 65, 76, 48, 54, 53, 36, 66, 44, 41, 59],
    'Peanut Butter': [47, 51, 57, 21, 19, 60, 48, 36, 50, 36, 24, 59, 22, 47, 27, 42],
    'Yeast Spread': [18, 31, 26, 57, 28, 21, 38, 29, 22, 45, 42, 42, 25, 48, 42, 40],
}

# 3. Yes/No Preferences - 24 values each
yes_no_data = {
    'Yes': [47, 67, 63, 58, 51, 65, 57, 76, 26, 57, 28, 60, 22, 36, 50, 45, 66, 42, 48, 41, 27, 40, 59, 42],
    'No':  [34, 65, 59, 18, 48, 31, 21, 21, 54, 38, 19, 53, 29, 48, 36, 36, 42, 24, 59, 22, 47, 44, 25, 42],
}

# Create DataFrames
df_bread = pd.DataFrame(bread_data)
df_spread = pd.DataFrame(spread_data)
df_yesno = pd.DataFrame(yes_no_data)

# Compute means and stds for each
print("Bread Means:\n", df_bread.mean())
print("\nBread Std Devs:\n", df_bread.std())

print("\nSpread Means:\n", df_spread.mean())
print("\nSpread Std Devs:\n", df_spread.std())

print("\nYes/No Means:\n", df_yesno.mean())
print("\nYes/No Std Devs:\n", df_yesno.std())
