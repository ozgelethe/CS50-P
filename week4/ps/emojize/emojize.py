#import library
import emoji

#get input from user
msg = input("Input: ")
msg2 = emoji.emojize(msg)

print("Output: ", msg2)