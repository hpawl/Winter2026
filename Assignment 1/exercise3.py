import math

# Exercise 3: The Backyard Deck Project
# Project size: 40 square meters

# Requirements per 1 sqm:
# 6 planks, 45 screws, 0.8L stain, 2 sandpaper sheets

PLANKS_SQM = 6
SCREWS_SQM = 45
STAIN_SQM = 0.8
SANDPAPER_SQM = 2
PROJECT_SIZE = 40

# Total quantities needed for 40 sqm:
total_planks = 40 * 6
# Calculate others...

# Bulk units: Planks (15), Screws (200), Stain (5), Sandpaper (10)
# Use math.ceil() for the following:
bundles_planks = math.ceil((PROJECT_SIZE * PLANKS_SQM) // 15) # Your code here
boxes_screws = math.ceil((PROJECT_SIZE * SCREWS_SQM) // 200)# Your code here
cans_stain = math.ceil((PROJECT_SIZE * STAIN_SQM) // 5)# Your code here
packs_sandpaper = math.ceil((PROJECT_SIZE * SANDPAPER_SQM) // 10)# Your code here

# Print in the table format requested
#| Item      | Requirement/m² | Needed           |
#| --------- | -------------- | ---------------- |
#| Planks    | 6              | 16 Bundle of 15  |
#| Screws    | 45             | 9 Box(es) of 200 |
#| Stain     | 0.8L           | 7 5L Can         |
#| Sandpaper | 2 sheets       | 8 Pack(s) of 10  |

print(f"| Item      | Requirement/m² | Needed           |\n| --------- | -------------- | ---------------- |\n| Planks    | 6              | {bundles_planks} Bundle of 15  |\n| Screws    | 45             | {boxes_screws} Box(es) of 200 |\n| Stain     | 0.8L           | {cans_stain} 5L Can         |\n| Sandpaper | 2 sheets       | {packs_sandpaper} Pack(s) of 10  |")