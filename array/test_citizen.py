"""The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old."""


def find_passenger_number(details):
    count = 0
    for item in details:
        age = item[11:13]
        if int(age) > 60:
            count += 1
    return count


if __name__ == '__main__':
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    print(find_passenger_number(details))
