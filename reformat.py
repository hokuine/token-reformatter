output = open('tokens.txt','w')
for combo in open("tokens.txt").read().splitlines() : 
    split = combo.split(':')
    token = split[2] 
    print(f"{token}")
    output.write(f"{token}\n") 
    
