from datetime import date, timedelta

from typing import Optional
 
 
class Employment:

    def __init__(self, start_date: date, end_date: Optional[date]):

        """
 
        Parameters

        ----------

        start_date

            The date the employment started.

        end_date

            The date the employment ended (set to None if the employment is still active).

        """

        self.start_date = start_date

        self.end_date = end_date
 
 
class EmploymentHistory:

    def __init__(self, employments: list[Employment]):
        employments.sort(key=lambda x: x.start_date)
        self.employments = employments
 
    @property

    def earliest(self) -> Employment:

        """Returns the employment started the earliest."""
        if len(self.employments) == 0:
            raise ValueError
        
        return self.employments[0]
 
    @property

    def current(self) -> list[Employment]:

        """Return a list of ongoing employments."""
        current_employments = [employment  for employment in self.employments if employment.end_date is None]
        return current_employments


    @property

    def is_empty(self) -> bool:

        """Return True if the employment history is empty, False otherwise"""
        if len(self.employments) == 0:
            return True
        return False
 
    @property

    def total_time_employed(self) -> timedelta:

        """Returns the total amount of time spent employed..

        If working multiple jobs concurrently, they should not be double counted."""

        total_employment_time = timedelta(0)
        maximum_end_date_until_now = date(1900, 1, 1) # add a minium time in here

        for employment in self.employments:
            # current_employment_time = timedelta(0)
            
            if employment.start_date >= maximum_end_date_until_now:  # easy part. start date is bigger that the end date of previous one
                total_employment_time += employment.end_date - employment.start_date
                maximum_end_date_until_now = employment.end_date
            elif employment.end_date > maximum_end_date_until_now:  # start date is less than the end date of previous one
                total_employment_time += employment.end_date - maximum_end_date_until_now
                maximum_end_date_until_now = employment.end_date
            # else:  
            #     current_employment_time = 0
            
            # total_employment_time += current_employment_time
        
        return total_employment_time
 
 
# A quick summary of the behaviour of timedelta:

# d1 = date(2021, 4, 23)

# d2 = date(2023, 5, 21)

# 

# td1 = d2-d1

# td2 = td1 + timedelta(days=5)

# assert td1 == timedelta(days=758)

# assert td2 == timedelta(days=763)

# January 1st-30th 
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 20))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))
 
january_no_overlap_employment_hist = EmploymentHistory([emp1, emp2])
 
# January 1st-10th 20th-30th (testing for gaps)
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 10))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))
 
january_gap_employment_hist = EmploymentHistory([emp1, emp2])
 
# January 1st-10th 20th-30th 1st-30th (testing for gaps & overlap)
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 10))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))
emp3 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 30))
 
january_gap_and_overlap_employment_hist = EmploymentHistory([emp1, emp2, emp3])
 
# Dense overlapping (answer should be 365 days for total_time_employed)
employments = [
    Employment(start_date=date(2020, 1, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 7, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 8, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 9, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 10, 1), end_date=date(2020, 12, 31)),
]
 
densely_overlapping_employment_hist = EmploymentHistory(employments=employments)

if __name__ == '__main__':
    print(january_no_overlap_employment_hist.total_time_employed)
    print(january_gap_employment_hist.total_time_employed)
    print(january_gap_and_overlap_employment_hist.total_time_employed)
    print(densely_overlapping_employment_hist.total_time_employed)

