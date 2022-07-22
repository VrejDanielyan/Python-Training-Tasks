# Write a Python program to check if a specific Key and a value exist in a dictionary
students = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
           {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
           {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
           {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
           {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

def test(key, value):
    for i in students:
        if i[key] == value:
            return True
    return False



print(test('class', 'VIIT'))
