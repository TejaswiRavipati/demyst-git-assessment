import pandas as pd
from faker import Faker

fake = Faker()

# Number of rows needed to generate a 2GB CSV
rows = 10000000  

def generate_large_csv(file_path, num_rows):
    # Generate data
    data = {
        "first_name": [fake.first_name() for _ in range(num_rows)],
        "last_name": [fake.last_name() for _ in range(num_rows)],
        "address": [fake.address() for _ in range(num_rows)],
        "date_of_birth": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_rows)]
    }

    df = pd.DataFrame(data)

    df.to_csv(file_path, index=False)

file_path = "large_2gb_sample.csv"

generate_large_csv(file_path, rows)
