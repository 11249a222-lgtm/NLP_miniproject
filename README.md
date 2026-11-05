# College Enquiry Chatbot (Python + NLTK)

A beginner-friendly NLP mini project. Students can ask questions about admissions,
courses, fees, hostel, transport, library, examinations and placements.

## Project files

- `main.py` - starts the application.
- `gui.py` - Tkinter chat window.
- `chatbot.py` - NLTK text preprocessing and FAQ matching.
- `knowledge_base.py` - questions and answers; edit this file with your college's real details.
- `requirements.txt` - Python dependency list.

## Requirements

- Python 3.9 or later
- Tkinter (usually included with standard Python on Windows)
- Internet access on first run if NLTK stopwords need to be downloaded

## Installation

Open a terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Customize for your college

Open `knowledge_base.py`. Change the sample answers to verified details from
your college, such as the official course list, fee structure, office hours,
address, department names and contact information. Add more FAQ entries by
following the existing dictionary format.

## How it works

1. The student enters a question in the Tkinter interface.
2. NLTK tokenizes the text, removes stopwords and stems words.
3. The chatbot compares the question with stored FAQ examples.
4. The closest FAQ answer is shown if the match score passes a threshold.
5. Otherwise, the bot asks the student to rephrase or contact the college office.

## Limitations

This is a rule-based FAQ chatbot with basic word-overlap matching. It does not
understand every sentence or generate new facts. Use official college information
and test common questions before presenting it.
