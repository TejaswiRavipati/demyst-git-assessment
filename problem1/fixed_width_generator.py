def generate_fixed_width_file(filename):
    data = [
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04"),
        ("John Doe", "12345", "2024-09-03"),
        ("Jane Smith", "67890", "2024-09-04")
        
    ]
    
    with open(filename, 'w') as f:
        for record in data:
            field1 = f"{record[0]:<10}"
            field2 = f"{record[1]:<5}"
            field3 = f"{record[2]:<8}"
            f.write(f"{field1}{field2}{field3}\n")

generate_fixed_width_file('fixed_width.txt')
