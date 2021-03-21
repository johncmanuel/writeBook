[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


# writeBook

Automatically copies and pastes a .docx file from a template document that contains all the industry standards for book manuscripts. This eliminates the hassle of setting up the document and working environment before writing a book.

This is only tested for the Windows OS.

## Command

```
book <name of your book>
```

## Preparations

Download templates here: https://kdp.amazon.com/en_US/help/topic/G201834230, create a 'Templates' folder, open the downloaded file and choose a language of your choice. Then, copy and paste all the .docx files into 'Templates'. I choose to do it this way rather than committing the template files themselves because I'm not sure if I'm legally allowed to republish Amazon KDP's content.

Alternatively, you can create your own .docx template with your own preferences and styles.

### Set up working environment

```
py -m venv <name of your venv>
cd <name of your venv>
git clone ...
pip install requirements.txt
```

Run venv

```
cd Scripts && activate.bat && cd ..
```

### Environment Variables

In your local machine, add working environment to 'Path'.

In the working directory, create an .env file and add the following variables:

```
# .env

BOOK_DIR=<path to where you want to place your writing documents>
TEMPLATES_DIR=<path to your templates folder>
PATH_TO_WORD=<path to your Microsoft Word application>
```

\*However, `PATH_TO_WORD` can be used for any other writing software.
