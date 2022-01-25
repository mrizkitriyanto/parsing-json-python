import requests
import csv

# Kita memakai dummy data dari url berikut
url = 'https://dummyjson.com/users'

# GET Request ke endpoint API
response = requests.get(url)

# Periksa kode HTTP selain 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Ada masalah dengan permintaan. Keluar.')
    exit()

# Load JSON encoded string ke Python object (akan mengembalikan json-encoded content dari response, jika ada.)
users = response.json()

# Definisikan key mana yang mau dipakai
user_list = users['users']

# Masukkan ke CSV
with open('list-users.csv', 'w') as t:
    writer = csv.writer(t)

    # Header CSV nya
    writer.writerow(("First Name", "Last Name", "Gender", "Home Address", "City", "Company Name", "Company Address", "Company Coordinate"))

    # Looping data yang di dapat
    for user in user_list:
        first_name = user['firstName']
        last_name = user['lastName']
        gender = user['gender']
        home_address = user['address']['address']
        city = user['address']['city']
        company_name = user['company']['name']
        company_address = user['company']['address']['address']
        lat = user['company']['address']['coordinates']['lat']
        lng = user['company']['address']['coordinates']['lng']
        geo = f'({lat},{lng})'

        # Masukkan data tsb ke CSV mengikuti format yang sudah kita tentukan
        csv_data = (first_name, last_name, gender, home_address, city, company_name, company_address, geo)
        writer.writerow(csv_data)

