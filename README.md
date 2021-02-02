# top3
Simple text analysis to reveal the top 3 nouns and adjectives in a set of LinkedIn recommendations.

## Quick Start

    $ python3 -m venv </path/to/new/virtual/environment>
    $ source </path/to/new/virtual/environment>/bin/activate
    $ pip3 install -k requirements.txt
    $ ./top3.py
  
The output is the following:

    defaultdict(<class 'list'>,
        {   'JJ': [('creative', 4), ('technical', 3), ('excellent', 2)],
            'NN': [('project', 5), ('team', 4), ('engineer', 4)]})
            
Note: If you see requests to download nltk data, follow the instuctions and then run top3.py again.
