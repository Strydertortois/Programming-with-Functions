import csv


def main():
    students_dictionary = read_dictionary("students.csv")
    i_number = input("Enter an I-Number: ")
    if i_number in students_dictionary :
        name = students_dictionary[i_number]
        print(name)
    else :
        print("No such student")



def read_dictionary(students_file):
    dictionary = {}
    with open (students_file, "rt") as students_file :
        reader = csv.reader(students_file)
        # Skip the first line:
        next(reader)
        
        for row in reader :
            key  = row[0]
            name = row[1]
            dictionary[key] = name
            

    return dictionary

if __name__ == "__main__" :
    main()