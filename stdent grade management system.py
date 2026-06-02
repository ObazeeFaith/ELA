def student_grade_management_system():
    # PART 2: Initializing the dictionary data structure
    student_records = {}

    print("Student Grade Management System")
    print("Enter the student details below. Type 'exit' as the student name to finish entry.\n")

    while True:
        # Prompt for student name
        name = input("Enter student name: ").strip()

        # Check for break condition
        if name.lower() == 'exit':
            break

        if name == "":
            print("Name cannot be empty. Please try again.")
            continue

        # Collecting scores for the student
        scores = []
        print(
            f"Enter scores for {name}. Enter a negative number or non-numeric value to stop adding scores for this student.")

        while True:
            score_input = input("  Enter score: ").strip()

            # Input validation and boundary control
            try:
                score = float(score_input)
                if score < 0:
                    print(
                        "  Negative score entered. Finalizing scores for this student.")
                    break
                elif score > 100:
                    print("  Score cannot exceed 100. Please enter a valid score.")
                    continue
                scores.append(score)
            except ValueError:
                print("  Non-numeric value entered. Finalizing scores for this student.")
                break

        # Handle case where a student is created with zero scores
        if len(scores) == 0:
            print(
                f"Warning: No valid scores entered for {name}. This record will not be saved.")
            continue

        # Save records into the dictionary (Key: Name, Value: List of Scores)
        student_records[name] = scores
        print(f"Successfully saved records for {name}.\n")

    # PART 3: Analysis and Formatted Reporting
    if not student_records:
        print("\nNo student data was recorded.")
        return

    print(f"{'Student Name':<20} | {'Average Score':<15} | {'Status':<12}")

    # Performance evaluation criteria variables
    PASSING_THRESHOLD = 50.0

    for name, scores in student_records.items():
        # Mathematical derivation of average score
        average_score = sum(scores) / len(scores)

        # Logic gate condition to determine pass/fail outcome
        if average_score >= PASSING_THRESHOLD:
            status = "PASS"
        else:
            status = "FAIL"

        # Dynamic console formatting using f-string string alignment flags
        print(f"{name:<20} | {average_score:<15.2f} | {status:<12}")


student_grade_management_system()
