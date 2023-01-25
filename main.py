
space=""
print(f"{space:^18}\033[34mKiprono's Palindrome...ndrome\033[0m")
print()
word=input("Enter a word: ").lower()
ndrome=word[::-1]
if ndrome==word:
  print(f"\033[33mWoohoo! {word} is a palindrome!! ")
else:
  print("\033[31mOopsie not a palindrome! \033[0m")