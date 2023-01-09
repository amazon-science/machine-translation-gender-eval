"""
Automatic accuracy metric for MT-GenEval paper.
We use the correct (gender-matched) references and incorrect (counterfactual/swapped) references to evaluate accuracy.
We first check the references for unique/gender-specific terms, then check for overlap with the incorrect gender
and the hypothesis. If there is overlap, we mark the segment as incorrect.
"""
import string


STRIP_PUNCT = str.maketrans(string.punctuation, ' '*len(string.punctuation))


def accuracy_metric(hypothesis, cor_ref, inc_ref):
    """
    Compute whether gender is correct in the translation given actual reference and counterfactual reference
    We assume input files contain one sentence per line
    :param hypothesis: AMT hypothesis file to be evaluated
    :param cor_ref: Correctly gendered reference file path
    :param inc_ref: Incorrect (counterfactual) reference file path
    :return decision (Corrct/Incorrect), one per each line in the input files
    """
    # read in the files. 
    # Note that each line of the input files will be lowercased and punctuation will be removed. 
    trg_list = read_file_to_list(hypothesis)
    cor_list = read_file_to_list(cor_ref)
    inc_list = read_file_to_list(inc_ref)

    assert len(trg_list) == len(cor_list), f'Output file and original reference file must have the same number of lines. Files are {hypothesis}, {cor_ref}'
    assert len(trg_list) == len(inc_list), f'Output file and counterfactual reference file must have the same number of lines. Files are {hypothesis},  {inc_ref}'

    metric_annot_mapped = []    
    for trg_line, cor_line, inc_line in zip(trg_list, cor_list, inc_list):
        [decision, trg_correct, trg_incorrect] = gender_decision(trg_line, cor_line, inc_line)
        metric_annot_mapped.append(decision) 
    accuracy = metric_annot_mapped.count('Correct')/len(metric_annot_mapped)
    return accuracy, metric_annot_mapped


def logicaloperation_AND(decision1, decision2):
    """
    Performs AND operation (per line) on the inputs: returns 'Correct' only if both inputs are 'Correct'. 
    :param decision1 and decision2: lists with each line either 'Correct' or 'Incorrect'
    :return: accuracy and list of decisions
    """
    combined_decision = ['Incorrect' if 'Incorrect' in [d1,d2] else 'Correct' for d1,d2 in zip(decision1, decision2)]
    accuracy = combined_decision.count('Correct')/len(combined_decision)
    return accuracy, combined_decision


def clean_line(line):
    """
    For an input line, lowercase it, strip extra spaces, and replace punctuation with spaces.

    :param line: Line to clean.
    :return: Cleaned version of the line
    """
    return line.lower().translate(STRIP_PUNCT).strip()


def get_words(line):
    """
    Helper function to get the set of words in a line.

    :param line: Line from which to get the words.
    :return: Set of words in the line.
    """
    return set(line.strip().split())


def get_trg_correct_incorrect(cor_words, inc_words, trg_words):
    """
    Compute overlap between references and translation
    """
    cor_unique = cor_words - inc_words
    inc_unique = inc_words - cor_words
    # now check the words in the target sentence for overlap with incorrect unique words
    trg_correct = trg_words & cor_unique 
    trg_incorrect = trg_words & inc_unique
    return trg_correct, trg_incorrect 


def gender_decision(trg_line, cor_line, inc_line):
    """
    Check if gender of a sentence is correct based on corresponding correct and incorrect references.
    Algorithm: We make decision based on whether hyp overlaps with original ref and counterfactual ref

    :param trg_line: Sentence from translation output for which to check gender.
    :param cor_line: Feminine reference.
    :param inc_line: Masculine reference.
    :return: a list of decision, overlap(hyp, original ref), overlap(hyp, counterfactual ref)
    """
    # start by getting unique words in each of the references
    cor_words, inc_words = get_words(cor_line), get_words(inc_line)
    trg_words = get_words(trg_line)
    trg_correct, trg_incorrect = get_trg_correct_incorrect(cor_words, inc_words, trg_words)

    if trg_incorrect:
        decision = 'Incorrect'
    else:
        decision = 'Correct'

    return [decision, trg_correct, trg_incorrect]


def read_file_to_list(filename):
    """
    Read a file to a list of lines; each line will be lowercased and punctuation will be removed.

    :param filename: File to read.
    :return: List of lines of the file.
    """
    out_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            cleaned_line = clean_line(line)
            out_list.append(cleaned_line)
    return out_list

