from collections import namedtuple
# house_prices = ['$140,000', '$550,000', '$480,000']
# house_prices.append('$1,000,000')
# print(house_prices)
# house_prices.pop(0)
# print(house_prices)

# midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
# final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]
#
# #Combine the scores into a single list
# all_scores = midterm_scores + final_scores
#
# num_midterm_scores = len(midterm_scores)
# num_final_scores = len(final_scores)
#
# print(num_midterm_scores, 'students took the midterm.')
# print(num_final_scores, 'students took the final.')
#
# #Calculate the number of students that took the midterm but not the final
# dropped_students = num_midterm_scores - num_final_scores
# print(dropped_students, 'students must have dropped the class.')
# average_midterm = sum(midterm_scores) / 9
# average_final_scores = sum(final_scores) / 7
# print("{} is the average of the midterm scores".format(average_midterm))
# print("{} is the average of the final scores!".format(average_final_scores))

# feb_temps = [56,67,89]
# jan_temps = [58,23,45]
# combinetemps = jan_temps + feb_temps
# print(combinetemps)

# point = ('X string', 'Y string')
# print(point)
# friends = ('Cleopatra', 'Marc', 'Seneca')
# print(len(friends))

# Car = namedtuple('Car',['make', 'model', 'price', 'horsepower', 'seats'])
# chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)
# chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)
# print(chevy_impala)
# print(chevy_blazer)
# print(chevy_blazer.price)


# Player = namedtuple('Player',['name', 'number', 'position', 'team'])
#
# cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
# lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')
#
# print(cam.name + '(#' + cam.number + ')' + ' is a ' + cam.position + ' for the ' + cam.team + '.')
# print(lebron.name + '(#' + lebron.number + ')' + ' is a ' + lebron.position + ' for the ' + lebron.team + '.')

# players = {
#     'lionel messi': 10,
#     'Chiristano ronaldo': 7
# }
# print(players)
# print({players['lionel messi']})
# prices = {}  # Create empty dictionary
# prices['banana'] = 1.49  # Add new entry
# print(prices)
#
# prices['banana'] = 1.69  # Modify entry
# print(prices)
#
# del prices['banana']  # Remove entry
# print(prices)
# prices = {
#     'Laptop': 799,
#     'Desktop': 1000
# }
# print(prices)
# print({prices['Laptop']})
# prices['Laptop'] = 699
# print({prices['Laptop']})
# car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}
#
# # Add the key Tesla with value USA to car_makers
# # Modify the car maker of Fiat to Italy
#
# car_makers['Tesla'] = 'USA'
#
# print('Acura made in', car_makers['Acura'])
# print('Fiat made in', car_makers['Fiat'])
# print('Tesla made in', car_makers['Tesla'])
exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50 :\n'))
exam1_grade_avg = exam1_grade / 50
exam2_grade_avg = exam2_grade / 50
exam3_grade_avg = exam3_grade / 50
exam
overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 4

print('Your overall grade is:', overall_grade)



