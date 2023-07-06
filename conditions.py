# logical operators
has_high_income=True
has_good_credit=False
has_criminalrec=False
# ->AND operator gives true when both the conditions are true
if has_high_income and has_good_credit:
    print("eligible")
# ->OR operator gives true when either of the one values is true
if has_high_income or has_good_credit:
    print("eligible")
# ->NOT operator changes the value of a value to it's inverse(true to false, false to true)
if has_good_credit and not has_criminalrec:
    print("eligible")