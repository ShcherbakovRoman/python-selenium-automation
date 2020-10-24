'''It is either a tricky question or the question has an error. The task is to find 1st NON-UNIQUE letter.
Which means => first letter that appears more than once in the string.
But the example shows that we need to find first unique letter. So I'm confused.
I wrote a function to find first UNIQUE letter until I noticed the mismatch in the task, though :)'''

def find_first_nonunique_char(string):
    new_string = string.lower()
    for char in new_string:
        x = new_string.count(char)
        if x == 1:
            return char
    return ''


print(find_first_nonunique_char("Amazon"))

'''If the task is to find first UNIQUE letter, could you give me a hint 
how to write a code so it would return in the same register as the input string.
For example: if input string "Hello", function will return "h", but I would like to see "H". Thank you'''