import csv

def parse_fixed_width_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)
        
        writer.writerow(['Field1', 'Field2', 'Field3'])
        
        for line in reader:
            field1 = line[0:10].strip()
            field2 = line[10:15].strip()
            field3 = line[15:25].strip()
            
            writer.writerow([field1, field2, field3])

parse_fixed_width_file('fixed_width.txt', 'output.csv')
