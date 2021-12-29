import csv
from sys import argv




def main():




    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    database_file = open("./" + argv[1])
    dna_file = open("./" + argv[2])

    database_reader = csv.DictReader(database_file)
    strs = database_reader.filenames[1:]


    dna = dna_file.read()
    dna_file.close()


    dna_fingerprint = {}
    for str in strs:
        dna_fingerprint[str] = consec_repeats(str, dna)


    for row in database_reader:

        if match(strs, dna_fingerprint, row):
            print(f"{row['name']}")
            database_file.close()
            return


    print("No match")
    database_file.close()





def consec_repeats(str, dna):
    i = 0
    while str*(i + 1) in dna:
        i += 1
    return i





def match(strs, dna_fingerprint, row):
    for str in strs:
        if dna_fingerprint[str] != int(row[str]):
            return False
    return True




main()
