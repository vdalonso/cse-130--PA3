Victor Alonso
A12981873

What language is your tokenizer written in?
    I decided to write in python since 1) its practice for my python class and 
    2) I'm genuinely curious about the language
What language are you tokenizing?
    I'm tokenizing lambda calculus, as simple as it gets. In my program I 
    included what the grammer I believe is most appropriate for lambda calculus.
How do you run your tokenizer?
    $ python tokenizer.py [FILENAME]
    pretty simple, the tokenizer takes in only one file that could have multiple
    lines of lambda calculus. I provided only 2 files since they test a lot of lines themselves.
What is the output format of your tokenizer?
    This guy prints out the list of tokens, although if implemented this could return
    to a larger pipeline or even output to its own output file.
What sorts of errors can your tokenizer handle?
    Maybe it's best to mention what it CAN'T handle. This program assumes the arguments
    to a function are one single character (i.e. nothing like \.arg1...), which makes sense
    because thats how it's supposed to be for lambda calc. Another thing, every space in the input file
    WILL BE TREATED AS A FUNCTION APPLICATION. It will not like spaces in the arguments.
Final Thoughts
    You know despite only spending a short amount of time with this part of the PA (Calculator.hs ate most of my time)
    I enjoyed thinking about the grammer of languages and how to represent them as tokens. Implementing the actual parser with
    the rules and stuff actually does sound really cool. However, it is now time to enjoy my 3 weeks of vacation. Thanks!