import csv

with open("test.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["user_id", "user_name", "qty"])
    writer.writerow([1, "John", 1352])
    writer.writerow([2, "Jane", 246])
    writer.writerow([3, "Bobbi", 73])

with open("test.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        print(reader.line_num, line)
