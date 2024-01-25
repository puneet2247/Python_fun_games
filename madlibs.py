# it is a program depicting string concatenation(putting sting together)
# suppose we want to create a string that says "subscribe to _______"
'''
youtuber = "my youtube channel"

# a few ways to do it
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}") # f-strings is the fastest and cleansest way of string interpolation 
'''
#madlib is a fun game for kids in which they enter different words which are than added to a surprise paragraph and they then read it.
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = (f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}.")
# Here using back slash to keep the para continuous

print(madlib)