from Packages import *

class FarelBench_CSV_Processor_my:
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
        folder_path = f'../../{self.folder_name}/data/'

        with open(f'{folder_path}{self.file_name}', 'r', encoding='utf-8') as csv_file:
            reader_csv = csv.reader(csv_file)
            # sample ouput of the above reader:
            # [
            #        '1', 
            #        'child', 
            #        '1', 
            #        'Given the family relationships:\n* Ralph is Anthony\'s parent.\n* Albert is Ralph\'s parent.\nWhat is Anthony\'s relationship to Ralph?\nSelect the correct answer:\n1. Anthony is Ralph\'s child.\n2. Anthony is Ralph\'s parent.\nEnclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>.'
            #    ]
            #    [
            #        '2', 
            #        'parent', 
            #        '2', 
            #        'Another question\nwith multiple lines\nin one cell.'
            #    ]

            questions = []
            
            for line in reader_csv:
                question = dict()

                question["topic"] = line[1]   # Label the question so we know which level it is (child, grandparent, etc.)
                
                question["input"] = line[3]

                match = re.search(r"<ANSWER>(\d+)</ANSWER>", line[3])
                question["target"] = match.group(1) if match else None

                questions.append(question)
            
            main_df = pd.DataFrame(questions)
        
        return main_df
    




class TruthfulQA_CSV_Processor_my:
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
        folder_path = f'../../{self.folder_name}/data/'

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
    

class MMLU_CSV_Processor_my:
    def __init__(self, folder_name, file_name):
        '''
        Constructor
        '''
        self.folder_name = folder_name
        self.file_name = file_name
        # print("TruthfulQA_CSV_Processor.__init__:", "self.question_path:", self.question_path, "self.input_files:", self.input_files)
    
    def convert_df(self):
        folder_path = f'../../{self.folder_name}/data/'

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