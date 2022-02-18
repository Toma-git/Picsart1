#3th task
letter=input("Please enter the letter:")
if letter=="y":
    print('The letter is phonetic and consonant')
elif letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    print("The letter is phonetic")
elif letter.isalpha()==True:
    print('The letter is consonant')
else:
    print('Please enter the other letter:')   