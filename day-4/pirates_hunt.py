line1 = ["⬜" , "⬜" , "⬜"]
line2 = ["⬜" , "⬜" , "⬜"]
line3 = ["⬜" , "⬜" , "⬜"]
map = [line1, line2, line3]

print("Hiding your tressure : X marks the spot. ")
position = input("Where do you want to hide your treasure? (e.g. 1,2): ")

#actual logic code
letter = position[0].lower()
abc = ["a" , "b" , "c"]
letter_index = abc.index(letter)
number = int(position[1]) - 1
map[number][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")