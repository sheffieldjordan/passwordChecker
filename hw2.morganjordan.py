#if the password is not in the list, still report the number of comparisons
# (a)  It has at least one uppercase and at least one lowercase letter
	# for i in string: if i.upper in string, return true
# (b)  It has at least one digit
	# 
# (c)  It has at least one character that is not a letter or a digit
# (d)  It has a length of at least six characters

# If exactly no conditions are met:  report that the password is "very weak"
# If exactly one condition is met:  report that the password is "weak"
# If exactly two conditions are met:  report that the password is "medium strength"
# If exactly three conditions are met:  report that the password "high medium strength"
# If all four conditions are met:  report that the password is "strong"

# You should also output which conditions are met and not met.

# The program should continue prompting the user for passwords until the user types "finish"

# (Extra credit:  When the user types in his or her password, we want don't to display it on the screen.  Find a way in Python to display asterisks instead of the password)
import string

def password_input():
	while True:
		password = ""	
		password = input("\n Enter test password: ")
		if password == "finish": # The program continues prompting the user for passwords until the user types "finish"
			exit()
		else: 
			validate_pw(password)
			

def validate_pw(password):
	"""Checks the password for the following conditions:
	(a)  It has at least one uppercase and at least one lowercase letter
	(b)  It has at least one digit
	(c)  It has at least one character that is not a letter or a digit
	(d)  It has a length of at least six characters
	If exactly no conditions are met:  report that the password is "very weak"
	If exactly one condition is met:  report that the password is "weak"
	If exactly two conditions are met:  report that the password is "medium strength"
	If exactly three conditions are met:  report that the password "high medium strength"
	If all four conditions are met:  report that the password is "strong"

	"""
	strength_calc = [0,0,0,0] #collects validation of all requirements; 0=False, 1=True; [length[0], upper and lower[1], digit[2], spec_char[3]]
	upper_and_lower = [0,0] #place holder for both the upper[0] and lower[1] checks
	if len(password) >= 6: #check length
		strength_calc[0] = 1
	
	for i in password: #check upper case
		if i.isupper():
			upper_and_lower[0] = 1
		elif i.islower(): #check lower case
			upper_and_lower[1] = 1
		elif i.isdigit(): #check for digits
			strength_calc[2] = 1
		elif i in string.printable[62:]: #checks for special characters; 63 and after
			strength_calc[3] = 1
		else:
			pass
	if sum(upper_and_lower) == 2: #if both lower and upper cases are present, then change the strength_calc validation place holder index [1] to 0. 
		strength_calc[1] = 1
	
	# give the user feedback
	if sum(strength_calc) == 0:
		pw_strength = "very weak"
	if sum(strength_calc) == 1:
		pw_strength = "weak"
	if sum(strength_calc) == 2:
		pw_strength = "medium strength"
	if sum(strength_calc) == 3:
		pw_strength = "high medium strength"
	if sum(strength_calc) == 4:
		pw_strength = "strong"

	# output which conditions are met and not met.
	if strength_calc[0] == 0:
		print("Password is not at least six characters long.")
	if strength_calc[1] == 0:
		print("Password does not contain both uppercase and lowercase lettters.")
	if strength_calc[2] == 0:
		print("Password does not contain a number.")
	if strength_calc[3] == 0:
		print("Password does not have any special characters.")

	print("Password strength is ***{}***.".format(pw_strength))
	check_pw(password)

def check_pw(password):
	"""checks the password against a list of commonly used
	passwords. Gives the user feedback if their password is
	in the list"""
	total_checks = 0
	with open('common.txt', 'r') as file_handle:
		pw_list = file_handle.read()
	pw_list = pw_list.strip().split()
		
	start = 0
	end = len(pw_list)-1
	check = "Password is not in list of common passwords."
	in_list = False

	while start <= end and not in_list:
		middle = (start+end) // 2
		if pw_list[middle] == password.lower(): #change all capital letters in the users password to lower case lettters
			check = "Password is in list of common passwords."
			in_list = True
		else: 
			if password.lower() < pw_list[middle]:
				end = middle - 1
			else: 
				start = middle + 1
		total_checks += 1 #total number of times the algorithm makes a comparison between the user's password and an entry on the list of common passwords"
	print(check)
	print("Total checks against common-password list: ", total_checks)
	password_input()


def main():
	print(password_input())

if __name__ == "__main__":
	main()

