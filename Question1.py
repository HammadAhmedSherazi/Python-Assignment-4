person_info={"first_name":"Hammad", "last_name":"Ahmed", "age":21, "city":"Karachi"}
print("First Name:", person_info["first_name"], "\tLast Name:", 	person_info["last_name"])
print("\nAge:", person_info["age"], "\t\tCity:", person_info["city"])
person_info["Qualification"]="Intermediate"
print("\n\tQualification:",person_info["Qualification"])
print("\n\t",person_info)
person_info["Qualification"]="BS(ComputerScience)"
print("\n\tUpdated Qualification:",person_info["Qualification"])
print("\n\tAfter Updating",person_info)
del person_info["Qualification"]
print("\n After Deletion",person_info)