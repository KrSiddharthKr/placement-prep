# *args
def detail(*personalDetails, company_name):
    print(personalDetails)
    print(type(personalDetails))
    details = personalDetails
    print(personalDetails[0])
    print(personalDetails[1])
    print(personalDetails[2])
    print(personalDetails[3])
    print(personalDetails[4])
    for i in details:
        print(i)
    print(company_name)

name = "Siddharth"
age = 22
gender = "Male"
stipend = "25000"
designation = "Intern"
detail(name, age, gender, stipend, designation, company_name="Drizz")