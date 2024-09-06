<p align="center">
  <img src="https://github.com/user-attachments/assets/3483ce0e-f850-49c8-988b-3102f390a8cc">
</p>
<h1 align="center">F The Docs</h1>
<h3 align="center">Exactly what it sounds like</h3>
<hr>
<h2>Huh?</h2>
<p>
  Do you ever get tired of just reading documentation?<br>
  Do you wish for a program with which you can just ask questions and get the answers from?<br>
  Well, this piece of garbage is (probably) just for you!
</p>
<hr>
<h2>So what <i>IS</i> FTheDocs?</h2>
<p>
  Glad you asked. FTheDocs is a super advanced documentation querier software, that you can use to get information from the documentation faster and (maybe) more efficiently.<br>
  In short, it's a vector database querying engine.
</p>
<hr>
<h2>How does it work?</h2>
<ol>
  <li>You first stuff the entire documentation (which you should scrape and store into either a .txt or .json file) into FTheDocs</li>
  <li>FTheDocs then builds a 'collection' of those documents that you added, while also taking into consideration any settings you have given it (YOU CAN CUSTOMIZE IT)</li>
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
to be presented with the help menu. Or just read the documentation of a documentation-bad-mouther below
<hr>
<h2>Documentation: 0_0</h2>
<h3>Basic Usage</h3>
<p>
  When cloning the repo, you also clone a test.txt file. This is a scraped version of Beej's C Sockets Guide. This is also the test document that I used for testing FTheDocs. You can use this to play around with it aswell<br>
  
  ```
  python fthedocs.py --file test.txt
  ```
  this is the most basic way to use FTheDocs. This command will load the test.txt file and present you in asking mode using default settings
</p>
<h3>Using JSON</h3>
<p>
  The `--file` is used for .txt files. To use .json files, use the argument `--json`
</p>
