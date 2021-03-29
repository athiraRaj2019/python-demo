from datetime import datetime

user_input = input("Enter your goal with a deadline(DD.MM.YYYY), separate it by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = (input_list[1])
# module.function.variable
# since deadline is a string here we need to convert it to date format
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
# calculate how many days from now till the dedline

time_until_deadline = deadline_date - today_date
days_till_deadline = time_until_deadline.days
hours_till_deadline = int(time_until_deadline.total_seconds() / 60 / 60)
print(f"Dear user ! Time remaining for your goal: {goal} is {days_till_deadline} days")
# print(f"Dear user ! Time remaining for your goal: {goal} is {hours_till_deadline} hours")

# sample input --> python demo:31.3.2021
