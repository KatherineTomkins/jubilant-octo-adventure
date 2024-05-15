### In this exercise, you will develop a function named decode(message_file). 
### This function should read an encoded message from a .txt file and return its decoded version as a string.
### Note that you can write your code using any language and IDE you want 
### (Python is preferred if possible, but not mandatory).

def read_text_file(message_file):
    # reads in file
    with open(message_file, 'r') as file:
        message = file.read()
        return message

def create_dictionary(message):
    # creates dictionary from input
    dictionary = dict((int(a.strip()), b.strip())
                      for a, b in (item.split(" ")
                                   for item in message.split("\n")))
    return dictionary

def create_pyramid(number_dictionary):
    # generates triangular numbers from input up to max value
    triangular_numbers = []
    my_keys = number_dictionary.keys()
    highest = max(my_keys)
    for number in range(1, highest):
        triangular_numbers.append(int(number*(number+1)/2))
    decoded_numbers = [x for x in triangular_numbers if x <= highest]
    return decoded_numbers

def get_message(dictionary, decode_numbers):
    # gets associated words from dictionary
    words = [dictionary.get(item) for item in decode_numbers]
    return ' '.join(words)    
            
def decode(message_file):
    message = read_text_file(message_file)
    dictionary = create_dictionary(message)
    decoded_numbers = create_pyramid(dictionary)   
    decoded_words = get_message(dictionary, decoded_numbers)
    print(decoded_words)

if __name__ == "__main__":
    decode("test1.txt")
    decode("test2.txt")
    
