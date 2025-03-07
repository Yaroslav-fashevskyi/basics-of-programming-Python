def create_student_report(*students, **subjects):
    if not students:
        print("Немає студентів")
    else:
        print("Звіт успішності:")
        for student in students:
            print(f"Student: {student}")
    if not subjects:
        print("Немає предметів і оцінок")
    else:
        print("Предмети та оцінки:")
        for subject, grade in subjects.items():
            print(f"{subject.capitalize()}: {grade}")

if __name__ == "__main__":
    create_student_report("Yaroslav", "Yaroslav-2", python=12, java=2, rust=0)

