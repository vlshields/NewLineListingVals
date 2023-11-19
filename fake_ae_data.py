import csv
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        PatientID = fake.random_int(min=1000, max=9999)
        gender = random.choice(['Male', 'Female'])
        visit_date = fake.date_this_decade()
        AE = random.choice(['Fall', 'Chest Pain', 'Swelling', 'Headache'])
        Visit = random.choice(['1', '2', '3', '4','5',"Unscheduled"])


        row = [PatientID, gender,visit_date, AE, Visit]
        data.append(row)

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        headers = ['PatientID', 'gender','visit_date', 'AE' ,'Visit']
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

if __name__ == '__main__':
    num_records = 100  # Change this to the desired number of records
    fake_data = generate_fake_data(num_records)
    save_to_csv(fake_data, 'fake_ae1.csv')
    print(f"Fake data has been generated and saved to 'fake_aes1.csv'.")
