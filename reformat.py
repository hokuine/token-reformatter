input = open("tokens.txt").read().splitlines() #files
output = open('tokens.txt','w')
for combo in input: 
    split = combo.split(':')
    token = split[2] 
    print(f"{token}")
    output.write(f"{token}\n") 
    
