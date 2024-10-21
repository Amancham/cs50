# Making faces 

# create replace function 
def convert(smile):
	# check if userinput has :) or :( and replace with smilie
	smile = smile.replace(":)", "🙂").replace(":(", "🙁")
	print(smile)
# create main function to run replace function
def main(): 
	user_input = input("")
	convert(user_input)
# set up to only run when run directly 

if __name__ == "__main__": 
	main()
