import pandas as pd
from faker import Faker

def generate_random_data(num_rows):
    fake = Faker()
    data = {
        'Name': [fake.name() for _ in range(num_rows)],
        'Phone Number': [fake.phone_number() for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

def save_to_excel(dataframe, file_name):
    dataframe.to_excel(file_name, index=False)

if __name__ == "__main__":
    num_rows = 10
    random_data = generate_random_data(num_rows)
    save_to_excel(random_data, 'contacts.xlsx')
    print("Excel file generated successfully.")
