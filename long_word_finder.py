valid_letters = []
removed_letters = []
max_len = 0

with open('names.txt', 'r') as f1:
    for full_name in f1:
        # split the string into a list  
        l = full_name.split()
        new = "" 
  
        # traverse in the list  
        for i in range(len(l)): 
            s = l[i]
            new = (s[0].lower())
            valid_letters.append(new)

valid_letters.sort()    

min_word_length = 2
j = 0

with open('wordlist.txt', 'r') as f2:
    for word in f2:
        valid_letters.extend(removed_letters)
        valid_letters.sort()
        removed_letters = []
        if '(' in word or ')' in word:
            continue
        #word = word.strip().lower()
        if len(word) < min_word_length:
            continue
        #print()
        #print(str(len(valid_letters)) + ' valid letters')
        for i in range(len(word) - 1):
            s = word[i]
            if s in valid_letters:
                valid_letters.remove(s)
                removed_letters.append(s)
                j += 1
                #print()
                #print(s + ', letter ' + str(j) + ' of ' + str(len(word) - 1) + ' in ' + word + ' removed from valid letters list')
                #print(valid_letters)
                #print(str(len(valid_letters)) + ' letters remaining')
                if j == len(word) - 1 and j > max_len - 1:
                    long_word = word
                    print(long_word + ' is ' + str(j) + ' letters long and is longer than ' + str(max_len) + ' letters')
                    max_len = len(word) - 1
            else:
                #print(s + ' is not a valid letter')
                break
        j = 0
        #print(valid_letters)
            
            