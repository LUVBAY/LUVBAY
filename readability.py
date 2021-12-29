s = input(("Text: "))

num_of_letters = 0
num_of_words = 0
num_of_sentences = 0

for i in range(len(s)):
    if (i == 0 and s[i] != ' ') or (i != len(s) - 1 and s[i] == ' ' and s[i + 1] != ' '):
        num_of_words += 1

    if s[i].isalpha():
        num_of_letters += 1

    if s[i] == '!' or s[i] == '?' or s[i] == '.':
        num_of_sentences += 1

L = num_of_letters / num_of_words * 100
S = num_of_sentences / num_of_words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")

elif index >= 16:
    print("Grade 16+")

else:
    print("Grade", index)
