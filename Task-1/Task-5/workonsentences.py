# Task 1 - 5

class WordProcessing:

    def __init__(self):
        self.final_list = []
        self.visited_word = set()

    # this method used for get input from user
    def first_part(self):
        name_list = []
        while True:
            string = input('Enter your words: ')
            if string == "":
                break
            name_list.append(string)

        self.find_ch(name_list) # send list of word to find_ch for category by character

    # category by character implementations
    def find_ch(self, lst):
      # create a dictionary for words category
        word_dict = {}
        for word in lst:  # create all keys for above dictionary
            key = ''.join(sorted(set(word)))

            if key in word_dict: # find by keys
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

        print([ls for ls in word_dict.values()]) #print result


    #part two , read file - create a list of words - word category by 3 character
    def second_part(self):
        url = "sentences_input.txt"
        with open(url, "r") as file:
            all_words = []
            lines = file.readlines()
            for line in lines: #read sentences
                line = line.rstrip('\n')
                lst = line.split()
                lst = lst[1:]
                all_words += lst #make a final list of all words

            all_words = self.process_words(all_words)

            for word in all_words:
                if word not in self.visited_word:
                    group = self.similar_words(word, all_words)
                    self.final_list.append(group)

            print(self.final_list)

    # a method for convert words character to lowercase and delete repetitive word from final list
    def process_words(self, lst):
        new_list = []
        for word in lst:
            new_word = word.lower()
            if new_word not in new_list: # check for delete repetitive words
                new_list.append(new_word)

        return new_list # return final list after delete repetitive words and convert to lowercase

    #method for classifications word on the final list (make sub list by 3 similar character)
    def similar_words(self, word, all_words):
        if word in self.visited_word:
            return []
        self.visited_word.add(word)
        group = [word]
        for w in all_words: #check every words with final list words and make sub list -> result have O(n^2) for Time
            if len(set(word) & set(w)) >= 3:
                group += self.similar_words(w, all_words)
        return group


object = WordProcessing()
selected_part = int(input("Please select a part of question (1 or 2): "))
if selected_part == 1:
    object.first_part()
else:
    object.second_part()
