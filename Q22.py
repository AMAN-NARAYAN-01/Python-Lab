import xml.etree.ElementTree as ET

def manage_student_xml(input_file, output_file):
    # Parse the existing XML document
    tree = ET.parse(input_file)
    root = tree.getroot()

    # 1. Modify an existing student's record
    # Updating the CGPA for student ID '101' (Rahul Sharma)
    for student in root.findall('student'):
        if student.get('id') == '101':
            cgpa_element = student.find('cgpa')
            if cgpa_element is not None:
                cgpa_element.text = '8.6'  # New CGPA value
            print(f"Updated CGPA for {student.find('name').text}.")

    # 2. Add a new student record to the XML structure
    new_student = ET.Element('student', id='111')
    ET.SubElement(new_student, 'name').text = 'Pooja Iyer'
    ET.SubElement(new_student, 'department').text = 'ECE'
    ET.SubElement(new_student, 'year').text = '1'
    ET.SubElement(new_student, 'email').text = 'pooja.iyer@example.com'
    ET.SubElement(new_student, 'cgpa').text = '9.0'
    
    root.append(new_student)
    print("Added new student record: Pooja Iyer.")

    # 3. Generate and save the modified XML document
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)
    print(f"Modified XML successfully saved to {output_file}")

manage_student_xml('students.xml', 'modified_students.xml')
