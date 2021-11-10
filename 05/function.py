def print_score(name, score): 
    print(name, 'score is', score) 
    if score > 1000:
        print('World record!') 
    elif score > 100: 
        print('Perfect!') 
    elif score > 10: 
        print('Passable.') 
    elif score > 1: 
        print('At least something. ') 
    else: 
        print('Maybe next time. ')

print_score('Your', 256) 
print_score('Denis', 5)