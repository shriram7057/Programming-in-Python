import calendar

def display_calendar():
    while True:
        try:
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            
            if month < 1 or month > 12:
                print("Month must be between 1 and 12.")
                continue

            cal = calendar.TextCalendar(calendar.SUNDAY)
            month_calendar = cal.formatmonth(year, month)
            print(month_calendar)
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        again = input("Would you like to display another calendar? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# Call the function 
display_calendar()
