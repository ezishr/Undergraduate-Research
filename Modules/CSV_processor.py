from Packages import *


class FarelBench_CSV_Processor:
    '''
    CSV Processor for questions in the Farel (Family Relations) Benchmark
    '''
    def __init__(self, folder_name, file_name):
        '''
        Constructor
        '''
        self.folder_name = folder_name
        self.file_name = file_name

    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'

        with open(f'{folder_path}{self.file_name}', 'r', encoding='utf-8') as csv_file:
            questions = []
            
            for line in csv_file:
                line = line.split(",")
                question = dict()
                target = ""
                # 0 1     2 3                                                                                                                                                                                                                                                                                                                                               
                # 1,child,1,"Given the family relationships:\n* Ralph is Anthony's parent.\n* Albert is Ralph's parent.\nWhat is Anthony's relationship to Ralph?\nSelect the correct answer:\n1. Anthony is Ralph's child.\n2. Anthony is Ralph's parent.\nEnclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>."
                question["topic"] = line[1]   # Label the question so we know which level it is (child, grandparent, etc.)
                tmp = line[3]
                tmp = tmp.split(r"\n")
                first_part = []
                second_part = []
                found_what_is = False

                for string in tmp:
                    if string.startswith("What is"):
                        found_what_is = True
                    if not found_what_is:
                        first_part.append(string)
                    else:
                        second_part.append(string)
                question["input"] = ' '.join(first_part)
                question["target"] = ' '.join(second_part)
                
                questions.append(question)
            
            main_df = pd.DataFrame(questions)
        
        return main_df
    




class TruthfulQA_CSV_Processor:
    '''
    CSV Processor for questions in the TruthfulQA Benchmark
    '''
    def __init__(self, folder_name, file_name):
        '''
        Constructor
        '''
        self.folder_name = folder_name
        self.file_name = file_name
        # print("TruthfulQA_CSV_Processor.__init__:", "self.question_path:", self.question_path, "self.input_files:", self.input_files)
    
    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'

        questions = []
        with open(f'{folder_path}{self.file_name}', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for line in csv_reader:
                #*************************************
                #ToDo map the questions/answers into our dictionary format
                question = dict()
                target = ""
                question["input"] = line["Question"]
                # There is a funky character in the Category column label. Instead of editing the question file, that character is used here.
                question["topic"] = line["﻿Category"]   # Label the question so we know which topic it came from
                question["source"] = line["Source"]    # Out bouilerplate processing doesn't use this, but we might be interested in the future
                target =         line["Examples: True"]
                target += " \n" + line["Examples: Informative"]
                target += " \n" + line["Examples: False"]
                target += " \n" + line["Examples: Uninformative"]
                question["target"] = target
                #*************************************
                questions.append(question)

        main_df = pd.DataFrame(questions)
        return main_df
    


class MMLU_CSV_Processor:
    def __init__(self, folder_name, file_name):
        '''
        Constructor
        '''
        self.folder_name = folder_name
        self.file_name = file_name
        # print("TruthfulQA_CSV_Processor.__init__:", "self.question_path:", self.question_path, "self.input_files:", self.input_files)
    
    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'

        questions = []
        fieldnames = ['input', 'optionA', 'optionB', 'optionC', 'optionD', 'correctAns']

        with open(f'{folder_path}{self.file_name}', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames = fieldnames)

            for i, line in enumerate(csv_reader):
                question = dict()

                prompt = line['input'] + ' \n' + line['optionA'] + ' \n' + line['optionB'] + ' \n' + line['optionC'] + ' \n' + line['optionD']

                target = line['correctAns']

                question['input'] = prompt
                question['target'] = target

                questions.append(question)

        main_df = pd.DataFrame(questions)
    
        return main_df