from tabulate import tabulate

# Define your table data as a list of lists (each inner list represents a row)
table_data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"],
]

# Specify the table format (e.g., "grid", "fancy_grid", "pipe", "orgtbl", "simple", etc.)
table_format = "grid"

# Print the table
table = tabulate(table_data, headers="firstrow", tablefmt=table_format)
print(table)