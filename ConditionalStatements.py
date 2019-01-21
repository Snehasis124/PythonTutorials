#5TH PROGRAM #CONDITIONAL STATEMENTS

#Question : To detect in which grade the student mark falls

student_mark = float(input("Enter your mark "))
mark_set_for_a_grade = 70
mark_set_for_b_grade = 60
mark_set_for_c_grade = 50
mark_set_for_d_grade = 40
mark_set_for_e_grade = 80
mark_set_for_0_grade = 90

if(student_mark >= mark_set_for_0_grade):
    print("Student has received O grade" , student_mark)
elif (student_mark >= mark_set_for_e_grade):
    print("Student has received E grade", student_mark)
elif (student_mark >= mark_set_for_a_grade):
    print("Student has received A grade", student_mark)
elif (student_mark >= mark_set_for_b_grade):
    print("Student has received B grade", student_mark)
elif (student_mark >= mark_set_for_c_grade):
    print("Student has received C grade", student_mark)
elif (student_mark >= mark_set_for_d_grade):
    print("Student has received D grade", student_mark)
else:
    print("Student FAILED , teacher to be blamed")
