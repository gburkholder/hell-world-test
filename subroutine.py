def square_csv(input_file, output_file):
    import csv
    reader = csv.reader(input_file)
    output_file.write("Start squares" + "\n" + "\n")
    for row in reader:
        output_file.write(str([int(i)*int(i) for i in row]) + "\n")
    output_file.write("\n" + "Done with squares!")
