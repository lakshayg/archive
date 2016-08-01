import urllib2
from bs4 import BeautifulSoup
from textwrap import fill
import argparse

# global params
WIDTH = 63
DOC   = ""

def add_section(title, content):
    global DOC
    DOC += title + '\n'
    DOC += len(title) * '-' + '\n'
    DOC += fill(content, WIDTH) + '\n'

def fix_word(word):
# spell check and show alternatives, returns a correct word
    return word

def main():
    global DOC
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="Display information for this word", type=str)
    args = parser.parse_args()

    try:
        vocabulary_dot_com = urllib2.urlopen("http://vocabulary.com/dictionary/" + args.word)
    except:
        print "Please check your internet connection\n"
        return
    soup = BeautifulSoup(vocabulary_dot_com, "lxml")
    usage = soup.find_all('p', attrs = {'class': 'short'})
    if usage:
        add_section('Usage', usage[0].text)
    else:
        print "Did you spell the word correctly?"

    print DOC

if __name__ == '__main__':
    main()

