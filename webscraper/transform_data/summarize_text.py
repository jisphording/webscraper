# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SUMMARIZE TEXT
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# Extract the "most important" sentences from a text to use as blog entry headline.
# Used to fill empty blog entry headlines, which can then manually be refined.
#

# Import standard modules
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
# install punkt sentence tokenizer
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import codecs

def summarize_text( text ):
    
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    # METHODS
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

    # STRIP HTML TAGS
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    # 
    def strip_html_tags( text ):
        clean = re.compile( '<.*?>' )
        return re.sub( clean, '', text )

    # CREATE FREQUENCY TABLE
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    #
    def create_frequency_table( text_string ) -> dict:
        stopWords = set( stopwords.words( "german" ) )
        words = nltk.word_tokenize( text_string )
        ps = nltk.stem.PorterStemmer()

        # Create dictionary for the word frequency table
        frequency_table = dict()
        for word in words:
            word = ps.stem( word )
            if word in stopWords:
                continue
            if word in frequency_table:
                frequency_table[ word ] += 1
            else:
                frequency_table[ word ] = 1

        return frequency_table

    # SPLIT SENTENCES
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    #
    def split_sentences( text ) -> dict:
        sentences = sent_tokenize( text, language='german' )

        for i, s in enumerate( sentences ):
            print(i+1, '-->', s)


    # SCORE SENTENCES
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    #
    def score_sentences( sentence, frequency_table ) -> dict:
        sentence_value = dict()

        for sentence in sentences:
            word_count_in_sentence = ( len( word_tokenize( sentence )))
            for word_value in frequency_table:
                if word_value in sentence.lower():
                    if sentence[:-1] in sentence_value:
                        sentence_value[ sentence[:-1] ] += frequency_table[ word_value ]
                    else:
                        sentence_value[ sentence[:-1] ] = frequency_table[ word_value ]

            sentence_value[ sentence[:-1] ] = sentence_value[ sentence[:-1] ] / word_count_in_sentence

        return sentence_value

    # FIND AVERAGE SCORE
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    #
    def find_average_score( sentence_value ) -> float:
        sum = 0

        for entry in sentence_value:
            sum += sentence_value[ entry ]

        # Average value of a sentence from original text
        average = float( sum / len( sentence_value ))

        return average

    # GENERATE SUMMARY
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    #
    def generate_summary( score ):
        # sort the sentences in descending order
        sorted_values = sorted( score.items(), key=lambda kv: kv[1], reverse=True )

        summary = sorted_values[ 0 ]

        return summary

    # ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
    # MAIN PROGRAM
    # ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

    text = strip_html_tags( text )
    frequency_table = create_frequency_table( text )
    sentences = nltk.sent_tokenize( text, language='german' )
    score =  score_sentences( sentences, frequency_table )
    summary = generate_summary( score )

    return summary[0]
