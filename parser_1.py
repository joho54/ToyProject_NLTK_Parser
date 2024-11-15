################################################################
################ Just Change this sections #####################
################################################################
# (1) Type Your Sentence

sentences = ['Could you show me the way to City Hall ?',
'The outdoor concert will be canceled if it rains.',
'The shop manager wrote an email to the customer.',
'When she just finished cleaning her room, her mother called her.',
'Which option do you want to select ?']

# (2) Make your CFG file for parsing your sentence.

# ex. grammar.cfg (see the direction in the powerpoint)

################################################################

import nltk

grammar = nltk.data.load("file:.\\grammar.cfg")
parser = nltk.ChartParser(grammar)

for idx, sent in enumerate(sentences):
    tokens = nltk.tokenize.word_tokenize(sent)
    trees = parser.parse(tokens)
    
    result_path = f'./sent{idx+1}_조현호.txt'
    
    with open(result_path, "w") as f1:
        for tree in trees:
            print(tree)
            f1.write(str(tree)+"\n\n")
            tree.draw()
            
            
