# import csv
# with open(r"C:\Python\File_handling.py\csv_file.csv", 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(dict(row))

# with open(r"C:\Python\File_handling.py\csv_file_1.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])

# with open(r"C:\Python\File_handling.py\csv_file_2.csv", 'w', newline='') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
