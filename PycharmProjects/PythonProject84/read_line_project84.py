with open('file.txt', 'w') as the_file:
    the_file.write('This is line one.\n'
                   'This is line two.\n'
                   'Finally, we are on the third and last line of the file. ')
with open('file.txt') as the_file:
    for line in the_file:
        print(line)