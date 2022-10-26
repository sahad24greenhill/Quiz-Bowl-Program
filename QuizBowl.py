import os, csv
os.system('cls')

#  Create the teams (using a dictionary)
#  

number_of_teams = int(input("how many teams are there?"))


teams_trueorfalse = []
teams_points = []

for teams in range(number_of_teams):
    teams_points.append(0)
    # teams_trueorfalse.append(False)


for team in range(number_of_teams):
    input("team "+ str(team+1) +" is up, press enter when you are ready")

    answer = int(input("what is 2+2?"))
    correct_answer = 4
    if answer == correct_answer:
        teams_points[team] += 10
        print("you got the question right first try!")
    else: # re ask question
        print("you got the question wrong try again!")
        answer = int(input("what is 2+2?"))
        if answer == correct_answer:
            teams_points[team] += 5
            print("you got the question right second try!")
        else:
            print("you got the question wrong both tries!")    


print(teams_points)
