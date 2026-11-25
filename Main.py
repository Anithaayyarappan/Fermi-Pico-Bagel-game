import random

original_number = str(random.randint(100,999))

while True:
    output = []
    guess_number = input('Enter the Guess Number:')
    
    if(len(original_number)!=len(guess_number)):
        print(f'Enter the {len(original_number)} digits')
        continue
    
    # if win
    if(int(original_number)-int(guess_number))==0:
        print('Fermi '*len(original_number))  #replication
        print('You Win!!!')
        break
    
    # if one digiit same or all are in correct positions with correct digit using nested for loop each time j restarts from start 
    for i in range(len(original_number)):
        for j in range(len(guess_number)):
            if(original_number[i]==guess_number[j]):
                if i==j: #positions
                    output.append('Fermi')
                else:
                    output.append('Pico')
                    
                    
    output_string = ''

    for item in output:
        output_string= output_string+" "+item
    
    if len(output)==0:
        print('Bagel')
    else:
        print(output_string)