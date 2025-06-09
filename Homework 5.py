# PRG 501
# Haixiang Yu

import json

def read_grade(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                print(f"Skip invalid line: {line}")
                continue
            name, grade = parts
            try:
                students.append({'name': name, 'grade': int(grade)})
            except ValueError:
                print(f"Skip line for invalid grade: {line}")
    return students

def calculate_statistics(students):
    grades = [student['grade'] for student in students]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    return average, highest, lowest

def write_results(file_path, average, highest, lowest):
    with open(file_path, 'w') as file:
        file.write(f"Class Average: {average:.2f}\n")
        file.write(f"Highest Grade: {highest}\n")
        file.write(f"Lowest Grade: {lowest}\n")

def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    students = read_grade('students.txt')

    if not students:
        print("No valid data. Please check 'students.txt'.")
        return

    average, highest, lowest = calculate_statistics(students)
    write_results('results.txt', average, highest, lowest)
    write_json('students.json', students)
    print("completed check 'results.txt'")


if __name__ == "__main__":
    main()

