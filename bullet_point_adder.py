# bullet_point_adder.py - Adds bullet points to the start of each line of text on the clipborad
import pyperclip
# returns all text on the clipboard as one big string
text = pyperclip.paste()

# separate each line with a new line 
lines = text.split('\n')

# We store the list in lines and then loop through the items in lines. For each line, we add a star and a space to the start of the line. Now each string in lines begins with a star.
for i in range(len(lines)):
      lines[i] = '- ' + lines[i]
text = '\n'.join(lines)
# separate lines and add starts
pyperclip.copy(text)
