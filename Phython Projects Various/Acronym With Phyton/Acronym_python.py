students_score = input("Input the score of the students \n").split()
highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score == score
        print(highest_score)