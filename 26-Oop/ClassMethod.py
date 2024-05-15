class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(day, month, year)  # Returning an instance of Date class

date1 = Date(2023, 12, 25)
print(f"\nYear: {date1.year}\nMonth: {date1.month}\nDay: {date1.day}")

# with classMethod
date2 = Date.from_string("2023-12-25")
print(f"\nYear: {date2.year}\nMonth: {date2.month}\nDay: {date2.day}")
