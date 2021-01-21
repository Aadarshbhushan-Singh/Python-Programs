days_input=int(input())
year=days_input//365
remaining_days=days_input%365
month=remaining_days//30
remaining_days_02=remaining_days%30
print("year ",year,"month: ",month,"days: ",remaining_days_02)