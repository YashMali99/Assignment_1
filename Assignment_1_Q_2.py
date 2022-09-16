
# Q-2) Write a Python program that accepts a word from the user and reverse it 





word = input("Enter a word to reverse: ")

for i in range(len(word) - 1, -1, -1):
  print(word[i], end="")
print("\n")
