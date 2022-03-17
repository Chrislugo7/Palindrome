# def number():
#     import random
#     chocolate = random.randint(1,7)
#     print(chocolate)
# number()


# def num():
#     randomlist = []
#     for i in range(1,8):
#         randomlist.append(i)
#     print(randomlist)
# num()


# def palindrome(word):
#     for i in range(0, len(word)):
#         for x in range(len(word),0,-1):
#         if [i] = [x]:
#         print("We have a palindrome!!!!")
#         print(word[i])

# palindrome("racecar")
# palindrome("textbook")


# def palindrome(str):
#     for i in range(0, (len(str)/2)):
#         print(str[i])
#         print(str[len(str)-i-1])
#         if str[i] != str[len(str)-i-1]:
#             return False

#     return "is palindrome"
    
# print(palindrome('racecar'))



    # for i in range(0, len(word)):
    #     # print(word[i])
    #     for j in range(len(word) -1,-1,-1):
        #     if word[i] == word[j]:
        #         print("Huston we have a palindrome!!!")
        # else:
        #     print("Try again!")
# palindrome('racecar')
# palindrome('stanley yelnats')


# We can only drive 11 hours in a day.
# def drive_clock():
#     from datetime import datetime
#     start = datetime.now()
#     end = datetime.now()
#     print()
# drive_clock()
def drive_clock():
    from datetime import datetime
    start = datetime(2022,2,23,15,13,11)
    print(start)
    # end = datetime.now()
    # if end - start >= 0:
    #     print(end-start)
    # else:
    #     print("you are in violation")
    # print(f"starttime {start} end {end}")
drive_clock()


