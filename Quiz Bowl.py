import os, csv, random, winsound
os.system('cls')

number_of_teams = int(input("How many teams are there? "))
number_of_easy_questions = int(input("How many easy questions does each team want to answer? "))

teams_trueorfalse = []
teams_points = []

for teams in range(number_of_teams):
    teams_points.append(0)

for question in range(number_of_easy_questions):
    for team in range(number_of_teams):
        first_number = random.randint(0,100)
        second_number = random.randint(0,100)
        input("Team "+ str(team+1) +" is up. Please click enter once you are ready. ")
        answer = int(input("What is "+str(first_number)+" + "+str(second_number)+"? "))
        if answer == second_number + first_number:
            teams_points[team] += 10
            print("You got the question right on the first try!")
        else:
            print("You got the question wrong. Try again!")
            answer = int(input("what is "+str(first_number)+" + "+str(second_number)+"? "))
            if answer == second_number + first_number:
                teams_points[team] += 5
                print("You got the question right on the second try!")
            else:
                print("You got the question wrong on both tries!")

last_team_hard_questions = input("Hard questions now - just for the last team that took part! Please type Y if you'd like to give them a shot. ")

if last_team_hard_questions == "Y":
    bonus_answer_1 = input("Allan Bloom infamously claimed that young people enjoyed rock music and this classical work because of their sexual rhythm. From about halfway in this composition onward, the theme is progressively doubled in the keys of the tonic's first through fourth overtones. This piece is the most popular to call for the F major sopranino saxophone. Though this piece's composer apocryphally praised a woman at its premiere for shouting that he was mad, he also rebuked Toscanini for performing it too fast. This piece emerged from a commission from ballerina Ida Rubinstein to orchestrate parts of Isaac Albeniz's Iberia. The composer's progressive aphasia may have inspired this piece's structure of one very long, gradual crescendo. For 10 points, a repetitive snare ostinato underlines what piece named for a Spanish dance by Maurice Ravel? ")   
    winsound.PlaySound('2022 NASAT Round 1 - Question 1.wav', winsound.SND_FILENAME)
    if bonus_answer_1 == "Bolero":
        teams_points[team] += 10
        print("You got the question right on the first try!")
    else:
        print("You got the question wrong. Try again!")
        bonus_answer_1 = input("Allan Bloom infamously claimed that young people enjoyed rock music and this classical work because of their sexual rhythm. From about halfway in this composition onward, the theme is progressively doubled in the keys of the tonic's first through fourth overtones. This piece is the most popular to call for the F major sopranino saxophone. Though this piece's composer apocryphally praised a woman at its premiere for shouting that he was mad, he also rebuked Toscanini for performing it too fast. This piece emerged from a commission from ballerina Ida Rubinstein to orchestrate parts of Isaac Albeniz's Iberia. The composer's progressive aphasia may have inspired this piece's structure of one very long, gradual crescendo. For 10 points, a repetitive snare ostinato underlines what piece named for a Spanish dance by Maurice Ravel? ")   
        if bonus_answer_1 == "Bolero":
            teams_points[team] += 5
            print("You got the question right on the second try!")
        else:
            print("You got the question wrong on both tries!")
    
    bonus_answer_2 = input("Eberhard Grün measured the distribution in sizes in this substance. Venetia Burney names a device used to detect this substance, which was collected in the first phase of the Tanpopo experiment. One of this substance's components is abbreviated GEMS (gee ee em ess). A perfect fluid modeled as a configuration of this substance with vanishing pressure is a namesake solution to the Einstein field equations. A NASA probe launched in 1999 collected this substance using silica aerogel. This substance loses angular momentum due to radiation pressure in the Poynting-Robertson effect. This substance scatters sunlight to produce zodiacal light. Interstellar reddening occurs due to scattering by this substance, which makes up the interstellar medium along with gas and cosmic rays. For 10 points, name this substance made up of particles in outer space. ")
    winsound.PlaySound('2022 NASAT Round 1 - Question 2.wav', winsound.SND_FILENAME)
    if bonus_answer_2 == "Cosmic Dust":
        teams_points[team] += 10
        print("You got the question right on the first try!")
    else:
        print("You got the question wrong. Try again!")
        bonus_answer_2 = input("Eberhard Grün measured the distribution in sizes in this substance. Venetia Burney names a device used to detect this substance, which was collected in the first phase of the Tanpopo experiment. One of this substance's components is abbreviated GEMS (gee ee em ess). A perfect fluid modeled as a configuration of this substance with vanishing pressure is a namesake solution to the Einstein field equations. A NASA probe launched in 1999 collected this substance using silica aerogel. This substance loses angular momentum due to radiation pressure in the Poynting-Robertson effect. This substance scatters sunlight to produce zodiacal light. Interstellar reddening occurs due to scattering by this substance, which makes up the interstellar medium along with gas and cosmic rays. For 10 points, name this substance made up of particles in outer space. ")
        if bonus_answer_2 == "Cosmic Dust":
            teams_points[team] += 5
            print("You got the question right on the second try!")
        else:
            print("You got the question wrong on both tries!")

print("That's the end of the game. Well done to all of the teams!")
print("All teams points (in order that teams played): ", teams_points)