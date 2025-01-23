def process_game_file(input_file, output_file):
    # Read the entire input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Prepare an empty list to collect modified lines
    modified_lines = []
    
    # Iterate through each line
    for line in lines:
        # Check if the line contains "Total"
        if "Total" in line:
            modified_lines.append(line.strip())  # Add the Total line
            modified_lines.append("\n-----------------\n")  # Add the separator line
        else:
            modified_lines.append(line)  # Add the original line
    
    # Write the modified content back to the output file
    with open(output_file, 'w') as f:
        f.writelines(modified_lines)

# Example usage:
input_filename = "jogos.txt"
output_filename = "jogosm.txt"
process_game_file(input_filename, output_filename)
