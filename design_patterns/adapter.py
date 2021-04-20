class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split("-")
        )

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age

a = AgeCalculator("1989-11-21")
print(a.calculate_age("2021-04-20"))

# the above example deals with dates in string format
# we want to write an adapter which uses the logic above but takes datetime objects as inputs

import datetime 

class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

da = DateAgeAdapter(datetime.date(1989, 11, 21))
print(da.get_age(datetime.date(2021, 4, 20)))

# below is a clever hack
# AgeableDate extends datetime.date and additionally implements split() method which discards its arguments and returns year,month,day of the original datetime
# Now we can pass it to the original AgeCalculator since all it cares for is the split method and it works
class AgeableDate(datetime.date): 
    def split(self, char): 
        return self.year, self.month, self.day

a1 = AgeCalculator(AgeableDate(1989,11,21))
print(a1.calculate_age(AgeableDate(2021,4,20)))