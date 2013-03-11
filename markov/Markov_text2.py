from sys import argv
from markov_class import *
import twitter

script, inputfile = argv

def main():
    order = int(raw_input("What Markov order would you like to use?"))

    filetext = process_file()

    markov = MarkovDict(filetext, order, 120)
    markov.read_text()
    output = markov.output_text()
    print output
    tweet_output(output)

# prompt to open file

def process_file():
    f = open(inputfile)
    # read through the file
    filetext = f.read()
    f.close()
    return filetext


def tweet_output(output):
    api = twitter.Api(consumer_key='t4Jb6e5ZGFu9D0PykTPQQ',
                      consumer_secret='PDs6QI9kdd7xOZbcpyiAoPChiCCNBDP7cn74K1zqcZg',
                      access_token_key='41198329-GWjvI5aDJTQS17Oi4fDN1hqNYrMStdwZ6ojG3uMwA',
                      access_token_secret='pnP7mKb9UzgaIaKLtMWxlZjNwVnnA3cE20FUG62j0')

    status = api.PostUpdate(output)


if __name__ == "__main__":
    main()
