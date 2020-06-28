number = 0
print('Number counter. Fist number is 1')
while True:
    if int(input()) == number+1:
        print('correct')
        number += 1
    else:
        print('incorrect. Score was', number, '. Next number is 1')
        number = 0
