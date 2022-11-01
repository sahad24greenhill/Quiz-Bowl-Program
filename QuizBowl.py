import os, csv, random
os.system('cls')

number_of_teams = int(input("How many teams are there? "))
number_of_questions = int(input("How many questions does each team want to answer? "))

teams_trueorfalse = []
teams_points = []

for teams in range(number_of_teams):
    teams_points.append(0)

first_number = 4
second_number = 3
for question in range(number_of_questions):
    for team in range(number_of_teams):
        input("Team "+ str(team+1) +" is up. Please click enter once you are ready.")
        answer = int(input("what is "+str(first_number)+"+"+str(second_number)+"? "))
        if answer == second_number + first_number:
            teams_points[team] += 10
            print("You got the question right on the first try!")
        else:
            print("You got the question wrong. Try again!")
            answer = int(input("what is "+str(first_number)+"+"+str(second_number)+"? "))
            if answer == second_number + first_number:
                teams_points[team] += 5
                print("You got the question right on the second try!")
            else:
                print("You got the question wrong on both tries!")
        first_number += random.randint(2,7)
        second_number += random.randint(2,7)    

print(teams_points)
