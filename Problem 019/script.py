import datetime
from dateutil.relativedelta import relativedelta

def isSunday(date):
    if date.isoweekday() == 7:
        return True
    return False 

begin_date = datetime.date(year=1901, month=1, day=1)
end_date = datetime.date(year=2001, month=1,day=1)

one_month = relativedelta(months=1)

def main():

    temp_date = begin_date

    how_many_sundays = 0

    while temp_date < end_date:
        if isSunday(temp_date):
            how_many_sundays += 1
        temp_date += one_month

    print("how_many_sundays:", how_many_sundays)


if __name__ == "__main__":
    main()