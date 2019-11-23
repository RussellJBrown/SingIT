



with open("/home/russell/SingIT/DeessingEnglish.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

number = 0
for i in content:
    iNew = int(i)
    number +=iNew

print(number/len(content))
