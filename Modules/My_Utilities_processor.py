from Packages import *

def read_directory_contents(path):
    """
    Read the contents of a directory
    @param path String: the path of the directory to be processed
    @return: a list
    """
    # Get list of contents in the folder
    contents = os.listdir(path)
    return contents


def write_string_to_file(text, file_name):
    """
    Writes a string to a file.

    @param text string: The string to write.
    @param file_name: The name of the file to write to.
    @return bool: True if file was written, False if an exception was thrown
    """
 
    status = True
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        '''The try block is used to catch any exceptions that might occur during the file writing process.
        os.makedirs(os.path.dirname(file_name), exist_ok=True) ensures that the directory for the file exists. If it doesn’t, it creates the directory. The exist_ok=True parameter prevents an error if the directory already exists.'''

        # Open the file in write mode  
        with open(file_name, 'w', encoding='utf-8') as file: 
            '''The file is opened in write mode ('w'). If the file does not exist, it will be created. If it does exist, its contents will be overwritten.'''
            file.write(text) # writes the string text to the file
        #print(f"String written to file: {filename}")
        
    except Exception as e:
        status = False
        print(f"Utilities.write_string_to_file(): Error writing to {file_name}: {e}")
        
    return status


def reduntdant_characters(data, col_names, characters):
    """
    Remove redundant characters from a column in a dataframe
    @param data DataFrame: the dataframe to be processed
    @param col_names List: the columns to be processed
    @param characters List: the characters to be removed
    @return: a DataFrame
    """

    for col in col_names:
        for character in characters:
            data[col] = data[col].str.replace(character,"")
    return data



def df_to_csv(folder_name, df, file_name, output_col):
    """
    Export the dataframe of AI generation to a csv file.

    @params: folder_name(name of the folder), df(dataframe)
    @return: True if the dataframe is exported successfully, False otherwise
    """
    base_path = r'/Users/ezishr/Library/CloudStorage/OneDrive-UniversityofCincinnati/Undergraduate Research/Check points'
    if (df[output_col].isnull().sum() == 0) or (df[output_col].isnull().sum() == 0):
        file_path = os.path.join(base_path, folder_name, f'{file_name}.csv')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        print(f"DataFrame exported successfully to {file_path}!")
    else:
        print("Export failed: DataFrame contains null values in 'gemini_output'.")
        return False
    



def gemini_generator(data, system_message):
    """
    GEMINI

    The function is to generate Gemini answers for the given data.

    @params: data(initial dataframe), system_message(message for Gemini system)
    @return: sample(dataframe with gemini_output column)
    """

    import time
    total_requests = 0
    successful_requests = 0


    model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_message,
    )

    sample = data.copy()
    sample['gemini_output'] = None

    for i in range(len(sample)):
        success = False
        retries = 3

        while not success and retries > 0:
            try:
                total_requests += 1

                # Make API request
                response = model.generate_content(sample['input'][i])
                # print(response.text)
                sample.loc[i, 'gemini_output'] = response.text.strip()
                success = True
                successful_requests += 1
                time.sleep(5)

            except Exception as e:
                # print(f"Error: {e}")
                retries -= 1
                time.sleep(5)
                total_requests += 1

    print(f"Total requests made: {total_requests}")
    print(f"Successful requests: {successful_requests}")

    return sample





def groq(data, system_message, model_name):
    """
    GROQ

    The function is to generate GROQ answers for the given data.

    @params: data(initial dataframe), system_message(message for Gemini system)
    @return: sample(dataframe with gemini_output column)
    """

    import time
    total_requests = 0
    successful_requests = 0
    client = Groq(api_key=os.environ['GROQ_API_KEY'],)

    sample = data.copy()
    sample[model_name] = None


    for i in range(len(sample)):
        success = False
        retries = 3

        while not success and retries > 0:
            try:
                total_requests += 1
                
                # Make a request to the GROQ API
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role":"user",
                            "content": sample.loc[i, 'input']
                        },
                        {
                            'role': 'system',
                            'content': system_message
                        }
                    ],
                    model = model_name
                )

                response = chat_completion.choices[0].message.content

                sample.loc[i, model_name] = response.strip()
                success = True
                successful_requests += 1
                # print(response)
                time.sleep(5)

            except Exception as e:
                # print(f"Error: {e}")
                retries -= 1
                time.sleep(5)
                total_requests += 1

    print(f"Total requests made: {total_requests}")
    print(f"Successful requests: {successful_requests}")

    return sample


def groq_line_generate(raw_dataset, output_dataset, start_idx, end_idx, system_message, model_name):
    """
    GROQ

    The function is to generate GROQ answers for the given data ROWS.

    """
    sample = raw_dataset.loc[start_idx:end_idx, ].copy()
    sample.reset_index(drop=True, inplace=True)
    groq_sample = groq(sample, system_message, model_name)
    output_dataset.loc[start_idx:end_idx, "llama_output"] = groq_sample[model_name].values
    return output_dataset