import pytest
from src.grade import Grade
from src.student import Student

def test_should_create_an_student():
    student = Student()
    assert isinstance(student, Student)

def test_should_create_an_student_with_name():
    student_name = "Rafael"
    student = Student(student_name)
    assert student.name == student_name

def test_should_add_student_grades():
    grades = [ 7, 9, 8, 7.5]
    student = Student()
    for grade in grades:
        student.add_grade(grade)
    assert student.grades == grades

def test_should_throw_an_error_when_try_to_add_an_invalid_grades():
    grades = [-1, -10, 11, 100, "A"]
    student = Student()
    for grade in grades:
        with pytest.raises(Exception):
            student.add_grade(grade)

def test_should_calculate_mean():
    list_of_grades = [[10, 9, 8.5, 7], [5, 5, 5], [7.4, 8, 2, 9]]
    expected_mean = [8.6, 5.0, 6.6]
    for idx, grades in enumerate(list_of_grades):
        result_mean = Grade.calculate_mean(*grades)
        assert result_mean == expected_mean[idx]    

    

