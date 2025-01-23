import re
import csv

# Function to extract game details
def extract_game_details(file_path, output_csv):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Adjusted regex pattern to capture game details
    pattern = r'(\d{1,2}/\d{1,2}/\d{4})\s+([\w\s&:]+)\s+€0\.00\s+.*?Sale Discount\s+-\s+€([\d.]+)'

    # Find all matches in the text
    matches = re.findall(pattern, content, re.DOTALL)

    # Process matches to ensure price is 0.00 if sale discount is not present
    processed_matches = []
    for match in matches:
        date = match[0]
        name = match[1]
        sale_discount = match[2]
        
        # If sale discount is None or '0.00', set price to '0.00', otherwise use original price
        price = '0.00' if sale_discount is None or sale_discount == '0.00' else sale_discount
        
        processed_matches.append((date, name, price))

    # Write to CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['date', 'name', 'price'])  # Write headers
        for match in processed_matches:
            writer.writerow(match)

# Path to the text file
file_path = 'jogosm.txt'

# Path to the output CSV file
output_csv = 'game_details.csv'

# Extract and write game details to CSV
extract_game_details(file_path, output_csv)
