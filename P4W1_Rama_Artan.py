def get_scores(num_scores):
    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score #{i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("INVALID Score entered!!!!")
                    print("Score should be between 0 and 100")
            except ValueError:
                print("Please enter a valid score!")
    return scores

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

def main():
    num_scores = int(input("How many scores do you want to enter? "))
    scores = get_scores(num_scores)
    lowest_score = min(scores)
    modified_scores = scores.copy()
    modified_scores.remove(lowest_score)
    average = sum(modified_scores) / len(modified_scores)
    grade = calculate_grade(average)

    print("\n-----Results------------")
    print(f"Lowest Score: {lowest_score}")
    print(f"Modified List: {modified_scores}")
    print(f"Scores Average: {average:.2f}")
    print("Grade: ", grade)

if __name__ == "__main__":
    main()