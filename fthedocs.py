from rich.console import Console
import pyfiglet
from undoc.chroma import new_collection, parse_documents_file, query_the_docs, query_around
from sys import argv


cons = Console()
cons.clear()

pyfiglet.print_figlet("F__kTheDocs", font="diet_cola", width=400)
cons.rule("[italic]F**KTHEDOCS")
print("\n")

# a dictionary containing all the necessary variables that will be used for querying and query creation
variables = {
    'collection_name': 'default_name',
    'document_id_starter': 'doco',
    'parsing_seperator': '.',
    'file_type': 'text',
    'concatenate_after': 0,
    'amount_to_query': 1,
    'limit_to_add': None
}

# display help
if '--help' in argv or '-h' in argv:
    cons.print("[bold]HOW TO USE (if you dont understand anything here you can visit the README of the Github repo):")
    cons.print("[pink1]      |____Use --file to state the file to use. Be sure to use the absolute file path")
    cons.print("[pink1]      |____Use --settings to tweak the settings configuration")
    cons.print("[pink1]      |____Use --help to show this help command")
    cons.print("[pink1]      |____Use --json to specify that the input file is JSON")
    cons.print("[pink1]      |____Use --json-path to specify the where the script will locate the data (required if --json is specified)")
    cons.print("[pink1]      |____Use --conc to specify the number of elements in list to concatenate after parsing. Better explained in the docs")

    exit(0)

# some simple command line parsing
if "--file" in argv:
    try:
        file_path = argv[argv.index('--file')+1]
    except IndexError:
        cons.print("[bold red]Error. No file path specified. HOW AM I SUPPOSED TO HELP YOU?")
        cons.print("[bold red]To specify a file path, just type '--file the_actual_file_path'")

        exit(1)

else:
    cons.print("[bold red]Error. No file path specified. HOW AM I SUPPOSED TO HELP YOU?")
    cons.print("[red]To specify a file path, just type '--file the_actual_file_path'")

    exit(1)

if '--settings' in argv:
    cons.print("[yellow]Entering into settings")
    cons.clear()

    pyfiglet.print_figlet("F__kTheDocs", font="diet_cola", width=400)
    
    cons.print("[bold yellow]Settings")
    
    cons.print("|-1. (1) Change collection name\n|-2. (2) Change document id name\n|-3. (3) Change parsing seperator\n|-4. (4) Change amount of queried results\n|-5. Press (e) to exit")
    


    exit_ = False
    # going into a loop in setting the variables
    while not exit_:
        try:
            option = cons.input("[cyan]> ")

            if option == '1':
                cons.print(f"[cyan]Enter the new collection name. [underline]Current Value: {variables['collection_name']}")
                new_collection_name = cons.input("[cyan]> ")
                cons.print("[bold green]UPDATED")
                variables['collection_name'] == new_collection_name
            
            elif option == '2':
                cons.print(f"[cyan]Enter the new document id starter. [underline]Current Value: {variables['document_id_starter']}")
                new_document_id_starter = cons.input("[cyan]> ")
                cons.print("[bold green]UPDATED")
                variables["document_id_starter"] = new_document_id_starter

            elif option == '3':
                cons.print(f"[cyan]Enter the new parsing seperator. [underline]Current Value: {variables['parsing_seperator']}")
                new_parsing_seperator = cons.input("[cyan]> ")
                cons.print("[bold green]UPDATED")
                variables['parsing_seperator'] = new_parsing_seperator
            
            elif option == '4':
                cons.print(f"[cyan]Enter the new amount to be queried. [underline]Current Value: {variables['amount_to_query']}")
                new_amount_to_be_queried = cons.input("[cyan]> ")
                cons.print("[bold green]UPDATED")
                variables['amount_to_query'] = int(new_amount_to_be_queried)

            elif option == 'e':
                exit_ = True
        except KeyboardInterrupt:
            cons.print("[red]Exiting")
            exit(1)
    
    cons.clear()
    pyfiglet.print_figlet("F__kTheDocs", font="diet_cola", width=400)
    cons.rule("[italic]F**KTHEDOCS", style="rule.bar")

if '--json' in argv:
    variables["file_type"] = 'json'

if '--json-path' in argv:
    try:
        variables['json_path'] = argv[argv.index('--json-path')+1]
    
    except IndexError:
        cons.print("[bold red]Error. So you included the json-path tag, but didnt give a value after?")
        exit(1)

if '--json' in argv and '--json-path' not in argv:
    print("[bold red]Error. JSON path not specified. How will I know where to look for the data?")
    exit(1)

if '--conc' in argv:
    try:
        variables['concatenate_after'] = int(argv[argv.index('--conc')+1])
    except IndexError:
        cons.print("[bold red]Error. You might want to specify a value for concatenation, dont you think?")
        exit(1)

if '--limit' in argv:
    try:
        variables['limit_to_add'] = argv[argv.index('--limit')+1]
    except IndexError:
        cons.print("[bold red]Error. Come on now, specify the limit")
        exit(1)

print("\n")
cons.print("[bold blue3 on white]Bored of reading billions of lines of documentation,\njust to spot that one solution to your problem?\nWORRY NOT! Just stuff all those letters in here and ask what you want\n\n", justify="center")

try:
    with cons.status("[bold underline yellow]Building collection of docs", spinner='dqpb') as status:
        documents = parse_documents_file(file_path=file_path,
                                         seperator=variables['parsing_seperator'],
                                         file_type=variables['file_type'],
                                         concatenate=variables['concatenate_after'],
                                         limit=variables['limit_to_add'])

        docs_collection = new_collection(docs=documents,
                                        name=variables['collection_name'],
                                        doc_id=variables['document_id_starter'])
        
        

    cons.print(f"[green]Items added: {docs_collection.count()}")
    cons.print("[green]Collection created successfully")

except Exception as e:
    cons.print(f"[bold red]Error occured in creating a collection. Error: {e}")

# let user read whatever the hell happened till now, though there isnt much to read
cons.print("[green]Switching over to asking mode. Press [white on red]{Enter}[/white on red] to continue..")
input()


cons.clear()
pyfiglet.print_figlet("F__kTheDocs", font="diet_cola", width=400)
cons.rule("[italic]F**KTHEDOCS", style="rule.bar")
print("\n")
cons.print("[green]Entered asking mode.\n    [underline bold]Options[/underline bold]:\n      (a)round: returns specified number of elements around the selected one. Eg: a 2\n      (c)lear: clear the screen\n      (Ctrl+C): exit")


# this is used for the query around thing
last_id = ""
while True:
    try:
        to_query = cons.input("[cyan]>>> ")

        # check if user wants to clear the screen
        if to_query == "c":
            cons.clear()

        elif to_query.split(" ")[0] == 'a' and variables["amount_to_query"] != 1:
            cons.print("[bold red]Error. The query around method can only work when you have set the amount of results to query to 1")

        elif len(to_query.split(" ")) == 2 and to_query.split(" ")[0] == 'a' and variables["amount_to_query"] == 1:
            cons.print(f"[bold pink1]Queried around I.D: {last_id}")
            try:
                cons.print(query_around(amount=int(to_query.split(" ")[1]),
                                        curr_id=last_id,
                                        collection=docs_collection)
                                        )
            except IndexError:
                cons.print("[bold red]Error. Please specify a value to query around. Eg: a 2 for querying +2 and -2 of current I.D")
        
        elif len(to_query.split(" ")) == 3 and to_query.split(" ")[0] == 'a' and variables["amount_to_query"] == 1:
            cons.print(f"[bold pink1]Querying around I.D {to_query.split(' ')[2]}")
            try:
                cons.print(query_around(
                    amount=variables['amount_to_query'],
                    curr_id=to_query.split(" ")[2],
                    collection=docs_collection
                ))
            except IndexError:
                cons.print("[bold red]Error. A syntax error. Did you follow the syntax for querying around a specific I.D?")
        
        elif to_query == 'help':
            cons.print("[bold]HOW TO USE (if you dont understand anything here you can visit the README of the Github repo):")
            cons.print("[pink1]      |____Use --file to state the file to use. Be sure to use the absolute file path")
            cons.print("[pink1]      |____Use --settings to tweak the settings configuration")
            cons.print("[pink1]      |____Use --help to show this help command")
            cons.print("[pink1]      |____Use --json to specify that the input file is JSON")
            cons.print("[pink1]      |____Use --json-path to specify the where the script will locate the data (required if --json is specified)")
            cons.print("[pink1]      |____Use --conc to specify the number of elements in list to concatenate after parsing. Better explained in the docs")

        else:
            response:dict = query_the_docs(query_string=to_query,
                                    collection=docs_collection,
                                    amount_to_query=variables['amount_to_query']
                                    )

            last_id = response['ids'][0][0]
            print(last_id)
            cons.print(response)

    except KeyboardInterrupt:
        cons.print("[underline]Interrupt detected. Exiting")
        quit(0)

    except Exception as e:
        cons.print(f"[bold red]Error occured. Error: {e}")