from Packages import *


class ARC_Challenge_Processor:
    def __init__(self, folder_name, file_name):
        self.folder_name = folder_name
        self.file_name = file_name

    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'
        
        # Open file and pass to objects
        with open(f'{folder_path}{self.file_name}', mode='r', encoding='UTF-8') as file:
            raw_objects = []
            for line in file:
                if line.strip():  # Avoid empty lines
                    raw_objects.append(json.loads(line))


        # Convert to dataframe
        main_df = pd.DataFrame(raw_objects)
        main_df = main_df[['question', 'answerKey']]

        # Convert endings to output col
        for idx in range(len(main_df)-1):
            input = main_df.iloc[idx]['question']
            main_df.at[idx, 'input'] = input['stem']
            temp_choices = input['choices']
            choice_options = ''
            for choice in temp_choices:
                choice_options += choice['label'] + ': ' + choice['text'] + '\n'
            
            main_df.at[idx, 'choices'] = choice_options
            
        main_df.drop(columns=['question'], inplace=True)
        main_df = main_df.rename(columns = {'answerKey':'target'})

        return main_df
    

class Big_Bench_Json_Processor:
    def __init__(self, folder_name, file_name):
        '''
        Constructor
        @param folder_name string: name of benchmark folder
        @param file_name string: the file name with .json extension
        '''
        self.folder_name = folder_name
        self.file_name = file_name

    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'
        with open(f'{folder_path}{self.file_name}', mode='r', encoding='UTF-8') as file:
            data = json.load(file) # standard json.load() function expects the entire file to be a single JSON object or array

        main_df = pd.DataFrame(data['examples'])
        main_df['input'] = main_df['input'].str.strip().str.replace('Question:', '')
        
        return main_df
    


class HellaSwag_Json_Processor:
    def __init__(self, folder_name, file_name):
        self.folder_name = folder_name
        self.file_name = file_name

    def convert_df(self):
        folder_path = f'../../CCSCMW2024/{self.folder_name}/data/'
        
        # Open file and pass to objects
        with open(f'{folder_path}{self.file_name}', mode='r', encoding='UTF-8') as file:
            raw_objects = []
            for line in file:
                if line.strip():  # Avoid empty lines
                    raw_objects.append(json.loads(line))
            '''
            The expression if line.strip(): checks if the stripped line is non-empty. If the line contains any characters other than whitespace, it evaluates to True. If the line is empty or contains only whitespace, it evaluates to False.
            '''

        # Convert to dataframe
        main_df = pd.DataFrame(raw_objects)
        main_df = main_df[['activity_label', 'ctx_a', 'ctx_b', 'endings']]
        main_df.rename(columns={'activity_label':'topic', 'ctx_a':'input'}, inplace=True)

        # Convert endings to output col
        for idx in range(len(main_df)-1):
            target = ""
            for ending in main_df.iloc[idx]['endings']:
                ctx_b = main_df.iloc[0]['ctx_b']
                target += f"{ctx_b} {ending}\n"
            main_df.at[idx, 'target'] = target

        main_df.drop(columns=['endings','ctx_b'], inplace=True)

        return main_df



