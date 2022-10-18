#get a greeting
greeting = input("Greeting: ")

new_g =greeting.lower().strip()

#check the answer is hello
if 'hello' in new_g:
    print("$0")

#then give $20 for answers that start with'h'
#strings are zero-based, so h is 0. word
elif 'h' == new_g[0]:
    print("$20")

else:
    print("$100")