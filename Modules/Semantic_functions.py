from Packages import *

def find_ambiguous_words(sentence):
    """
    Find ambiguous words in a sentence
    @param sentence string: the sentence to find ambiguous words in
    @return list: a list of ambiguous words in the sentence
    """
    words = word_tokenize(sentence)
    ambiguous_words = [word for word in words if len(wn.synsets(word)) > 1]
    return ambiguous_words


def auto_wsd(df):
    """
    Count the number of times each sense of an ambiguous word appears in a dataset
    @param df DataFrame: the dataset to find ambiguous words in
    @return dict: a dictionary of ambiguous words and their senses
    """
    disambiguated_senses = {}
    for idx in range(len(df)):
        sentence = df.loc[idx, 'input']
        ambiguous_words = find_ambiguous_words(sentence)

        for word in ambiguous_words:
            sense = lesk(sentence, word)
            sense_name = sense.name() if sense else None

            if word not in disambiguated_senses:
                disambiguated_senses[word] = {}
            
            if sense_name not in disambiguated_senses[word]:
                disambiguated_senses[word][sense_name] = 1
            else:
                disambiguated_senses[word][sense_name] += 1

    return disambiguated_senses





def build_text_from_questions(df, write_to = None, remove_stopwords = True):
    '''
    # Build one long text string from all the questions.
    # This logic will vary based on the architecture of the benchmark questions.
    # @param questions list: list of dictionaries, one dictionary per question.
    # @param write_to string: File path to write the text string. Default is None. 
    # @param remove_stopwords bool: True to remove stopwords from the text string. Defaults to True
    # @return String: The text string
    '''
    text = ""
    for idx in range(len(df)):
        text += " " + str(df.loc[idx, "input"])
    text_without_stopwords = preprocessing.remove_stopwords(text)
    # if write_to != None:
    #     write_string_to_file(text, write_to)
    #     write_string_to_file(text_without_stopwords, write_to.replace(".txt", "_stopwords_removed.txt"))

    # if remove_stopwords:
    #     #print(text_without_stopwords[0:1000])
    #     return text_without_stopwords
    # else:
    #     return text

    return text_without_stopwords