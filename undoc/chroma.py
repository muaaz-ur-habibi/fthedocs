import chromadb
import json

# NOTE: DO NOT USE ANY OTHER VERSION OF CHROMADB SINCE THEY ARE MOST LIKELY TO FAIL DUE TO A BUG IN COLLECTION ADDING

def parse_documents_file(file_path:str,
                         seperator:str='.',
                         file_type:str='text',
                         json_path:str=None,
                         concatenate:int=0,
                         concatenator:str=" ",
                         limit:str=None):
    '''Parsing function of the input data file. For now only supports text and json files'''
    parsed_docs = []
    concatenated_docs = []

    # read the file
    with open(file_path, 'r', errors='ignore') as file:
        file = file.read()

        # check if user gave a json file
        if file_type.lower() == 'json':
            file = json.loads(file)

        # check if the json was parsed properly. if yes then it will return a dict
        if type(file) == dict:
            # dont know why this is even here since to get to the info in json we need the path
            if json_path != None:
                # split the path up
                json_path = json_path.split("|")
                # do some checks on the inputted path
                if "LIST" not in json_path:
                    print("LIST parameter not found. Please specify it to set a target list")

                for path in json_path:
                    # iterate over the paths

                    # check if the path is a list, else just go deeper in ;)
                    if path[0:4] != "LIST":
                        file = file[path]
                    else:
                        # if it was a list check if they also gave the index
                        if len(path) > 4:
                            list_amount = int(path.replace("]", "").split("[")[1])
                            file = file[list_amount]
                        else:
                            # else just iterate over the list and append the data to the parsed docs list
                            final_path = json_path.index("LIST")+1
                            for final_dictionary in file:
                                # here, final_dictionary is the final dictionary, the end, after which we specify the key at which the text is stored
                                final_dictionary:str = final_dictionary[json_path[final_path]]

                                if seperator != "NONE":
                                    for i in final_dictionary.split(seperator):
                                        parsed_docs.append(i)
                                else:
                                    parsed_docs.append(final_dictionary)
                            break
                limit = limit.split(":")
                parsed_docs = parsed_docs[int(limit[0]):int(limit[1])]
            else:
                print("JSON file could not be parsed properly. Please check everything and retry")
        
        # if the file type is something else.(most likely a text)
        elif file_type == 'text':
            # do some basic parsing
            file = file.split("\n")
            
            # slice the list to the limit specified by the user, if the user specified a limit that is
            if limit != None:
                try:
                    limit = limit.split(":")
                    file = file[int(limit[0]): int(limit[1])]
                except IndexError:
                    print("Error. To specify a limit, this is the format: start_of_limit:end_of_limit. Start is 0")
                    exit(1)
            
            # seperate each line based on seperator provided
            for i in file:
                if i.strip() != '':
                    if seperator != 'NONE':
                        i:str = i.split(sep=seperator)

                        for doc in i:
                            if doc != '':
                                parsed_docs.append(doc.strip())
                    else:
                        parsed_docs.append(i.strip())
            
        else:
            print("Invalid file provided. Please provide either a .txt or a .json")

    # think of this as 'batching': concatenate x number of docs together
    if concatenate != 0:
        for i in range(0, len(parsed_docs), concatenate):
            concatenated_doc = concatenator.join(parsed_docs[i:i+concatenate])
            concatenated_docs.append(concatenated_doc)

        return concatenated_docs
    else:
        return parsed_docs


def new_collection(name="damn-the-docs",
                   docs:list=[],
                   doc_id:str="doco"):
    '''Create and return new collection of the documents after parsing'''
    # create the client and collection with custom name
    cl = chromadb.Client()
    coll = cl.create_collection(name)

    # create the ids
    ids = []

    # iterate for the ids
    for idx, _ in enumerate(docs):
        _id = f"{doc_id}_{idx+1}"
        ids.append(_id)

    # add the docs to the collection
    coll.add(
        ids=ids,
        documents=docs
    )

    return coll

def query_the_docs(query_string:str,
                   amount_to_query:int,
                   collection:chromadb.Collection
                   ):
    '''Function to query the documents'''

    # do basic querying
    queried = collection.query(
            query_texts=query_string,
            n_results=amount_to_query
        )

    return format_chromadb_output(queried)

def query_around(amount:int,
                 curr_id:str,
                 collection:chromadb.Collection):
    '''Query the documents around the selected document'''
    
    # pretty straightforward:
    # get the last id, do some parsing and math and obtain the range
    curr_id = curr_id.split("_")
    curr_id_int = int(curr_id[-1])
    curr_id_str = "".join(i for i in curr_id[:-1])
    range_to_query = range(curr_id_int-amount, curr_id_int+1+amount)

    new_range = [f"{curr_id_str}_{i}" for i in range_to_query]

    # return the queried range
    queried = collection.get(
        ids=list(new_range)
    )

    #return format_chromadb_output(queried)
    return queried

def format_chromadb_output(output:dict):
    output = {
        'ids': output['ids'],
        'documents': output["documents"],
        'distances': output["distances"] if 'distances' in output.keys() else []
    }

    return output