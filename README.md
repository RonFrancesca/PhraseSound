# PhraseSound

PhraseSound is an interactive web application which make users able to listen to a particular sound related to words or phrases. The system is based on a Flask web application, which allows the user to type down the words or sentence he will to listen the sound of, while the sound is generated  by a Pure Data audio engine. The  communication between the two systems is based on Open Sound Control messages. The mapping between the phrase and the sounds depends on the distance between two consecutive words of the phrase in an embedding space (word2vec [1] has beenused  for  this  project). Two same consecutive  words  will generate the same sound, the distance being zero. Two different consecutive words will generate different  sounds, which will change according to how distant their are in the word embedding space. 

[1]:
> T. Mikolov, K. Chen, G. Corrado, and J. Dean.Efficient estimation of word representations in vectorspace, 2013

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Python and the following modules are necessary to run the notebook correctly: numpy, scipy, gensim, python-osc. 

You can install the modules required simply typing on the terminal the following command: 

```
$ pip install -r requirements.txt
```
(the file requiremennts.txt is in the repository)

Otherwise, you can manually install the single modules with the following commands.  

In **Ubuntu** the user can install all these modules it is as simple as typing on the terminal:
```
$ sudo apt-get install python-dev python-numpy python-scipy 
$ pip install gensim
$ pip install python-osc
```

In **OSX** the user can install these modules by typing on the terminal:

```
$ brew install python
$ pip install numpy scipy gensim python-osc
````

In **Windows** the user can refer to this link to install python on your local machine: https://docs.python.org/3/using/windows.html and install the other modules by typing on the terminal: 

```
$ pip install numpy scipy gensim python-osc
```

### Clone or Download the repository 

Clone or download the repository. 
It contains a jupyter notebook, please read Jupyter Notebook instruction to properly change directories paths and run the notebook correctly.

Command to clone the repository:
```
$ git clone https://github.com/RonFrancesca/PhraseSound.git
```

The dataset can be downlaoded at the following links:
- download the full pdf score dataset here: https://github.com/MTG/SymbTr-pdf 
- download the full xml files dataset here: https://github.com/MTG/SymbTr/releases/tag/v2.4.3


### Jupyter Notebook instructions
Install Jupyter Notebook according to the its instructions https://jupyter.org/install

Start up jupyter notebook

```
$ jupyter notebook
```

Follow instructions appearing in the console regarding navigating your browser to the notebook


## Authors 
- Francesca Ronchini
- Marco Bertola 
- Miguel Perez Fernandez


