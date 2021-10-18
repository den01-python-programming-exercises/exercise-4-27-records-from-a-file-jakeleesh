import csv

def main():
    #write your code below this line
    file_name = input("Name of the file:")
    try:
        f = open(file_name, "r")
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            if int(row[1]) > 1:
                print(row[0] + ", age: " + row[1] + " years")
            else:
                print(row[0] + ", age: " + row[1] + " year")
    except:
        print("Error")

if __name__ == '__main__':
    main()
