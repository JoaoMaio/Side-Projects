import re
import csv

# Path to the text file
file_path = 'jogosm.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Define regex patterns
entry_pattern = r'(\d{1,2}/\d{1,2}/\d{4})\s+(.*?)€\d+\.\d{2}'
discount_pattern = r'Sale Discount\s+- €\d+\.\d{2}'

# Compile regex patterns
entry_regex = re.compile(entry_pattern, re.DOTALL)
discount_regex = re.compile(discount_pattern)

# Initialize CSV writer
csv_filename = 'epic_games_purchases.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date', 'Name', 'Discount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find all game entry matches
    matches = entry_regex.finditer(content)

    # Extract information and write to CSV
    for match in matches:
        date = match.group(1).strip()
        name = match.group(2).strip()

        # Find discount within this specific entry
        discount_match = discount_regex.search(content, match.end())
        if discount_match:
            discount = discount_match.group(0).strip()
        else:
            discount = ''

        # Write to CSV
        writer.writerow({'Date': date, 'Name': name, 'Discount': discount})

print(f'CSV file "{csv_filename}" has been created successfully.')
