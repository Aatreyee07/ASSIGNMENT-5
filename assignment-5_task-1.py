dict = {"Alice":85 , "Mary": 46 , "Simran":79 , "Mark":83 , "Carl":72}
user_input = input("Enter the student's name: ")

if user_input in dict:
    print( f"{user_input}'s marks: {dict[user_input]}")
else:
    print("Student not found.")
