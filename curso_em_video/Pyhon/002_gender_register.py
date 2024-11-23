x = str(input("Choose a gender M/F: ")).strip()
while x not in 'mMfF':
    x = str(input(("Not an actual option, please try again: "))).strip()
print("Gender {}, saved!".format(x))
