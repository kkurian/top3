# top3

Simple text analysis to reveal the top 3 adjectives in a set of LinkedIn
recommendations.

For example purposes, the Recommendations.csv are drawn from [my LinkedIn profile](https://www.linkedin.com/in/kkurian/).

## Quick Start

    $ python3 -m venv </path/to/new/virtual/environment>
    $ source </path/to/new/virtual/environment>/bin/activate
    $ pip3 install -k requirements.txt
    $ ./top3.py
  
The output is the following:

    ['technical', 'creative', 'excellent']

Note: If you see requests to download nltk data, follow the instuctions and
then run top3.py again.
