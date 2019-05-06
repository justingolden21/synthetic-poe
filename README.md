# Synthetic Poe  &mdash; RGB Studios 

### About

Synthetic Poe will generate Synthetic stories and poems by Edgar Allen Poe.

### How to Use

Run driver.py to begin. You can double click the file or type <code>python driver.py</code> or <code>py driver.py</code> to begin. You must have Python 3 on your computer. If you don't have it, you can download it [here](https://www.python.org/downloads/)

Enter the name of the file: either 'belfry', 'cask', 'raven', 'silence', or 'spirits'. Note that spirits is too small by itself to run alone and get any meaningful result. You can combine multiple input texts with commas: <code>belfry,cask,raven,silence,spirits</code>.

Then, enter the number of characters you'd like to look back. Fewer characters is more random, and eventually becomes gibberish, while more characters gets closer to the origonal piece. We've found 8 to 10 characters is usually a good place to start.

Lastly, enter how many characters you'd like to synthesize.

Synthesized text will appear both in command prompt and in your output folder. To clear your output folder, simply navigate to it, then press ctrl+A (command+A on Mac) to select everyting then hit the delete key.

To read the text outloud, you can use our text to speech website. Navigate to the speaker folder, then open "index.html" with your prefered browser (for example, Chrome, Firefox). Hit the "Upload Text" button and find and select the "data.txt" file adjacent to "index.html". Then, clikc the "Speak" button to speak the text. Click "Stop" at any time to stop, or simply close the tab.

### How it Works

Our synthesizer uses by using character-based Markov chains to generate semi-random text. 

We first create a dictionary that tracks the number of times each character occurs after each set of characters of size SIZE that occurs in the original text.

SIZE is the number of characters we look back, and NUM_CHARS is the number of characters we'll generate.

We start in a random location in the text, and take the next SIZE characters. Then, we loop through each index NUM_CHARS times, generating the next character using the following method:

We look back SIZE characters in our current output, and see which possible characters could follow that substring SIZE large. We then pick a random one of those possible characters with a weighted random, that is more likely to choose characters taht follow that substring more often.

Finally, we crop the beginning and end so that it starts after a terminating character and ends on a terminating character.

### Similar Programs

[Bloviate](https://successfulsoftware.net/2019/04/02/bloviate/) also uses character-based Markov chains to generate its output. Feel free to read more about how it works.

### Credit

Text from [Textfiles](http://www.textfiles.com/etext/AUTHORS/POE/)

<hr>

**Code by [Justin Golden](https://justingolden21.github.io)**
