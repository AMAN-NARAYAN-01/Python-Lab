text = input("Enter a string:")

char_freq = {}
for ch in text:
    if ch !=" ":
        char_freq[ch] = char_freq.get(ch,0)+1
        
        print("\nCharacter Freqeuncy")
        for k,v in char_freq.items():
         print(k, ":", v)
          
          word_freq = {}
          words = text.split()
            
            for word in words] = 
            word_freq[word] =
            word_freq.get(word, 0) + 1 
            
            print("\nWord Frequency")
            for k,v in word_freq.items():
            print(k, ":",v)
            
