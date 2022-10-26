import os, csv
os.system('cls')

#  Create the teams (using a dictionary)
#  

number_of_teams = int(input("how many teams are there?"))


teams_trueorfalse = []
teams_points = []

for teams in range(number_of_teams):
    teams_points.append(0)
    teams_trueorfalse.append(False)


for team in range(number_of_teams):
    input("team "+ str(team+1) +" is up, press enter when you are ready")

    


print(teams_trueorfalse)
print(teams_points)



