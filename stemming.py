from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

inpute_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize','possibly', 'provision', 'hospital', 'kept', 'code', 'scratchy']

# create various stemmer object

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('English')

#create a list of stemmer name for display 

stemmer_name = ['POTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' *(lan(stemmer_name)+1)
print('\n', formatted_text.format('INPUT WORD', *stemmer_name), '\n', '='*68)

#stem each word and display the output
for word in inpute_words:
	output = [word, porter.stem(word), lancaster.stem(word), snowball.stem(word)]
	