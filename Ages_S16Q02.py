File_name = input("Enter the file name: ")
FH = open(File_name, 'r')
all_lines = FH.readlines()
Ages = []

for line in all_lines:
    name, age = line.strip().split('-')
    Ages.append((name, int(age)))

Ages.sort(key=lambda x: x[1], reverse=True)
print(" oldest person's names list:")

for person in Ages:
    print(person[0])





