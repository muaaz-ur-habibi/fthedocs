<p align="center">
  <img src="https://github.com/user-attachments/assets/3483ce0e-f850-49c8-988b-3102f390a8cc">
</p>
<h1 align="center">F The Docs</h1>
<h3 align="center">Exactly what it sounds like</h3>
<p align="center">P.S: No offence is intended to documentation writers, nor to any documentations. I love the effort you guys put to writing good, easy-to-follow <i>(ahm)</i> manuals for software ❤️</p>
<p align="center">This was created as a fun side project. Please do not get mad at me if this doesnt meet your expectations</p>
<hr>
<h2>Huh?</h2>
<p>
  Do you ever get tired of just reading documentation?<br>
  Do you wish for a program with which you can just ask questions and get the answers from?<br>
  Well, this piece of majesticity is (probably) just for you!
</p>
<hr>
<h2>So what <i>IS</i> FTheDocs?</h2>
<p>
  Glad you asked. FTheDocs is a super advanced documentation querier software, that you can use to get information from the documentation faster and (maybe) more efficiently.<br>
  It first embeds all your docs, then, using your query, finds the closest most accurate piece of embedding to the embedding of the query<br>
  In short, it's a <a href="https://www.google.com/search?q=what+is+a+vector+database">vector database</a> querying software
</p>
<hr>
<h2>How does it work?</h2>
<ol>
  <li>You first stuff the entire documentation (which you should scrape and store into either a .txt or .json file) into FTheDocs</li>
  <li>FTheDocs then builds a 'collection' of those documents after parsing them, while also taking into consideration any settings you have given it (YOU CAN CUSTOMIZE IT)</li>
  <li>Then it presents you into 'asking mode', where you can ask the collection what you want to know from the docs</li>
</ol>
<hr>
<h2>Oooook, how do I get started?</h2>
<p>THATS EASY. Just git clone this repo :)</p>

```
git clone https://github.com/muaaz-ur-habibi/fthedocs.git
```
then just go into the directory, run the command

```
python fthedocs.py --help
```
to be presented with the help menu. Or just read the documentation below for more details
<hr>
<h3>Some Features:</h3>
<ol>
  <li>Pretty Console UI using Rich library</li>
  <li>Question-Answer style querying system</li>
  <li>Verbose output of whatever process is currently on-going (still working on this)</li>
  <li>Settings to allow the program to be fitted according to your documentation</li>
  <li>Free AND Open-source</li>
</ol>
<hr>
<h2>Documentation:</h2>
<h3>Basic Usage</h3>
<p>
  When cloning the repo, you also clone a test.txt & a test.json file. This is a scraped version of Beej's C Sockets Guide. This is also the test documents that I used for testing FTheDocs. You can use this to play around with it aswell<br>
  
  ```
  python fthedocs.py --file test.txt
  ```
  this is the most basic way to use FTheDocs. This command will load the test.txt file and present you in asking mode using default settings
</p>
<h3>Using JSON</h3>
<p>
  The argument `--file` is used for .txt files. To use .json files, use the argument `--json` to specify a .json file<br>
  When using JSON, the `--json-path` argument becomes compulsory
</p>
<h3>JSON Path</h3>
<p>
  This is the key values of the .json file FTheDocs needs to take in order to reach the target text, which it then converts into a list of texts<br>
  Think of it like this:<br>
  
  ```
  {
    'main': {
      'key_1': {
            'key_2': ["target_text_as_list"],
    }
  }
  ```
  In order to reach all the desired texts, in this case `["target_text_as_list"]`, FTheDocs needs to take the path 'main->key_1->key_2'<br><br>
  Naturally, there will be limitations. In this case:
  <ul>
    <li>The final key MUST have a list of the dictionaries to iterate over as its value</li>
    <li>Multiple paths in a single run can NOT be specified</li>
  </ul>
  To specify this, use the argument: `--json-path "PATH|TO|LIST|OF|TEXTS`<br><br>
  It would also be nice to know that, to specify the end of the path aka that 'here are the list of dictionaries' you should add a LIST parameter<br><br>
  Alternatively if you have many lists of lists, and only wish to use one of them, LIST also works like any list (in the sense you can use LIST[0] to specify an element at 1st index)<br><br>
  Too much to swallow? You bet. Go ahead and open the test.json file for me. I'll show you a real example.<br>
  <br>
  In here, you see there is a main dictionary, which has a "css" key, whose value is a LIST. Inside that LIST is another LIST, only one tho. That LIST is a list of dictionaries, with different HTML element properties. But what we are looking for is the "content" key of those dictionaries.<br><br>

  What will be the json path of this file?<br>
  <details>
    <summary>Think about it for a second...</summary>
      That would be "css|LIST[0]|LIST|content"<br><br>
      First fthedocs would go into 'css', there it will find a LIST, but we only need the 0th one, so we specified 'LIST[0]'. After that is another LIST, this one containing all the dictionaries, whose key that we need is 'content'
    
  </details>
</p>
<h3>Limits</h3>
<p>
  You can also specify a starting and ending point of the documents to be added. This is also a command-line argument.<br>
  The syntax goes as: `starting_point:ending_point`
</p>
<h3>Settings</h3>
<p>
  CUSTOMIZING (kinda)<br><br>
  There are quite a few things you can change. Some of them directly impact the results. Others not so much or not at all
  <ul>
    <li>Changing the collection name</li>
    <li>Changing the document I.D name</li>
    <li>Changing the parsing seperator</li>
    <li>Changing the amount of queried results</li>
    <li>Concatenating a set number of documents</li>
    <li>Changing the concatenating character</li>
    <li>Showing these settings when building the collection</li>
  </ul>
  Just from reading im pretty sure you can figure out which one has an impact on the result.<br>
</p>
<ol>
  <li><h3>Collection Name:</h3>This changes the created collection's name.</li>
  <li><h3>Document I.D Name:</h3>This changes the document I.D starting string</li>
  <li><h3>Parsing seperator:</h3>This changes the splitting criteria for each line. So if this is a '.', each line of the text/json file will be splitted further on each '.'. Can be useful for more seperation</li>
  <li><h3>Amount of Queried Results:</h3>Changes the amount of results that are returned back to the user, usually in ascending order of close match. NOTE: setting this to anything other than 1 will disable the 'Query around' functionality (explained later on)</li>
  <li><h3>Concatenating Docs:</h3>You can also concatenate an integer number of docs together, to create a bigger document. Think of it as the opposite of Parsing Seperator</li>
  <li><h3>Change Concatenation Character:</h3>Concatenate on a custom character. Eg: 'document 1', 'document 2'. Character is '. ' (spaces will matter). So the concatenated will be 'document 1. document 2'</li>
  <li><h3>Showing the Settings:</h3>Doesnt do much. Just display the settings when building the collection. Just in case you realise you messed up a setting or two</li>
</ol>
<hr>
Those were the basics of FTheDocs. Incase you dont understand anything OR encounter an issue/problem, you can always open up an issue, and ill make sure to find some time to respond :)
<hr>
<h3>Limitations:</h3>
<ul>
  <li>No file types supported other than .txt and .json</li>
  <li>Cannot save a previous collection</li>
  <li>Cannot scrape the documentation for you</li>
  <li>Cannot format the documentation for you (in json)</li>
  <li>It isnt an AI so you cant ask it anything</li>
  <li>Cannot give you emotional support (<i>I tried</i>)</li>
  <li>Made as a fun project to learn some <a href="https://www.google.com/search?q=What+Is+Retrieval+Augmented+Generation">RAG</a></li>
</ul>
