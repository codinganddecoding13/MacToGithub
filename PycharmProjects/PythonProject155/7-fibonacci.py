"""this is the fibonacci equation which needs to be formatted"""
# sequence1 = input - 1
# sequence2 = input - 2
# sequence = format(sequence1) + format(sequence2)
def get_sequence():
    """Get and return a sequence length"""
    sequence = input('How many terms are in your fibonacci sequence?')
    return sequence

def show_sequence(sequence):
    """Show a sequence"""
    print('Your sequence is {}.'.format(sequence))

def get_and_show_sequence():
    """Get and show sequence"""
    sequence = get_sequence()
    show_sequence(sequence)

get_and_show_sequence()

