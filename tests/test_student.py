from student.student import (
    create_student, add_class, get_num_classes, summary, 
    get_student_with_more_classes
)

def test_init():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = ["mathematics", "foundations of computing"]

    ada = create_student(name, level, courses)

    assert ada["name"] == name
    assert ada["level"] == level
    assert ada["courses"] == courses

def test_add_class():
    new_class = 'Intro to Feminism'
    charles = create_student("Charles Babbage", "senior", ["mechanical engineering"])
    add_class(charles, new_class)
    no_courses = create_student("steve", "senior", [])

    assert len(charles["courses"]) == 2
    assert new_class in charles["courses"]
    assert no_courses =={"name": "steve", "level": "senior", "courses" :[]}

def test_get_num_classes():
    george = create_student("George Byron", "senior", ["advanced poetry"])

    assert get_num_classes(george) == 1

def test_summary():
    anne = create_student(
        "Anne Byron",
        "senior",
        ["theory of religion", "theory of morality"]
    )

    assert summary(anne) == "Anne Byron is a senior enrolled in 2 classes"

def test_get_student_with_more_classes():
    charles = create_student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = create_student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )

    mike = create_student("Charles Babbage", "senior", ["mathematics", "foundations of computing"])
    sally = create_student(
        "Ada Lovelace",
        "sophomore",
        ["mechanical engineering"]
    )

    # TODO: write assertions
    assert get_student_with_more_classes(charles, ada) == ada
    assert get_student_with_more_classes(mike, sally) == mike
    


# TODO: Write additional tests to reach 100% test coverage
