#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of
#strings.

def same_characters(lists):
    such_words = 0
    for i in lists:
        if len(i)>2 and i[0] == i[-1]:
            such_words += 1
    print(such_words)


same_characters(['abc', 'xyz', 'aba', '1221', 'dfd'])
