char = input("Enter a char: ")
a_count = 0
ac_count = 0
acb_count = 0
while char != ".":
    if char == "a":
        a_count += 1
    elif char == "c":
        ac_count = a_count
        a_count = 0
    elif char == "b":
        acb_count += ac_count
    char = input("Enter a char: ")
print(acb_count)
2.
for i in range(15):
    text = input('enter a text: ')
    if text[0] == text[-1]:
        print(text)