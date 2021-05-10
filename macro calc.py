age = int(input('What is your age: '))
gender = input('What is your gender (m or f): ')
weight = int(input('What is your weight in kgs?: '))
height = int(input('What is your height in cm?: '))
levels = input('what would you say your activity level is?'
               ' a - little to no exercise, '
               'b - 1-3 times a week, '
               'c - 4-5 times a week, '
               'd - 5+ times a week,')
if levels == 'a':
    levels = 330
if levels == 'b':
    levels = 650
if levels == 'c':
    levels = 850
if levels == 'd':
    levels = 1125

protein = weight*1.95
fat = weight*.4
calories = 13.397*weight + 4.799*height - 5.677*age + 88.362

BMR = (13.397*weight + 4.799*height - 5.677*age)
print ('The bare amount of calories your body needs to fucntion and stay healthy is',BMR , "KCAlS!")

macro =input ('Would you like a macro nutrient breakdown of your daily calorie consumption? yes or no')
if macro == 'yes':
    print (protein, 'G, This is your daily reccomended protein intake for maintanence')
    print (fat, 'G, This is your daily reccomended fat intake for maintanence')
    sum = calories + levels

    print ('This is your maintanence calorie goal is',sum)


