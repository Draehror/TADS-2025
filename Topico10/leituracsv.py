import csv

path = "./cars.csv"

with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars = []

    for row in csv_reader:
        cars.append(dict(row))
    print(cars)
    
# print("=------------------------=")

# with open(path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     cars = []

#     for row in csv_reader:
#         cars.append(row)

    # for row in cars:
    #     print(list(row.values()))


to_update = ['1999','Chevy','Venture']
new_price = '4500.00'

with open(path, 'w') as csv_file:
    fieldnames = cars[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()

    for row in cars:
        if set(to_update).issubset(set(row.values())):
            row['Price'] = new_price
        writer.writerow(row)