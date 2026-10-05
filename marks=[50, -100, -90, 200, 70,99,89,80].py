marks=[50, -100, -90, 200, 70,99,89,80]

for mark in marks:
    if mark<0 or mark>100:
        print(f"invalid for {mark}")

    else:
        print(f"Valid for {mark}")

        if mark>=97 and mark<=100:
            print(f"Grade A+ for {mark}")

        elif 93<=mark<=96:
            print(f"Grade A for {mark}")

        elif 90<=mark<=92:
            print(f"Grade A- for {mark}")

        elif 87<=mark<=89:
            print(f"Grade B+ for {mark}")

        elif 83<=mark<=86:
            print(f"Grade B for {mark}")

        elif 80<=mark<=82:
            print(f"Grade B- for {mark}")

        elif 77<=mark<=79:
            print(f"Grade C+ for {mark}")

        elif 73<=mark<=76:
            print(f"Grade C for {mark}")

        elif 70<=mark<=72:
            print(f"Grade C- for {mark}") 

        elif 67<=mark<=69:
            print(f"Grade D+ for {mark}")

        elif 60<=mark<=66:
            print(f"Grade D for {mark}")

        else:
            print (f"Fail for {mark}")

