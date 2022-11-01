import os, csv
os.system('cls')

number_of_teams = int(input("How many teams are there? "))

teams_trueorfalse = []
teams_points = []

for teams in range(number_of_teams):
    teams_points.append(0)

for team in range(number_of_teams):
    input("Team "+ str(team+1) +" is up, press enter when you are ready.")

    answer = int(input("what is 2+2?"))
    correct_answer = 4
    if answer == correct_answer:
        teams_points[team] += 10
        print("You got the question right on the first try!")
    else: # re ask question
        print("You got the question wrong. Try again!")
        answer = int(input("what is 2+2?"))
        if answer == correct_answer:
            teams_points[team] += 5
            print("You got the question right on the second try!")
        else:
            print("You got the question wrong on both tries!")    

print(teams_points)
