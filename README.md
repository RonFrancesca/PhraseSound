# PhraseSound

PhraseSound is an interactive web application which make users able to listen to a particular sound related to words or phrases. The system is based on a Flask web application, which allows the user to type down the words or sentence he will to listen the sound of, while the sound is generated  by a Pure Data audio engine. The  communication between the two systems is based on Open Sound Control messages. The mapping between the phrase and the sounds depends on the distance between two consecutive words of the phrase in an embedding space (word2vec [1] has beenused  for  this  project). Two same consecutive  words  will generate the same sound, the distance being zero. Two different consecutive words will generate different  sounds, which will change according to how distant their are in the word embedding space. 

[1]:
> T. Mikolov, K. Chen, G. Corrado, and J. Dean.Efficient estimation of word representations in vectorspace, 2013

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

In order to run the code you need a copy of two files: 
- *mappying.npy*: file containing the words mapping
- *glove.6B.50d_word2vec.txt*: txt file with words and words dimensions. 

Due to size file limits, these files can be asked to the authors. 
The glove.6B.50d_word2vec.txt can also be downloaded from this link: https://www.kaggle.com/watts2/glove6b50dtxt

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

### Pure Data instruction

Please, refer to this link for more information about Pure Data and how to install it: https://puredata.info/ 


## Clone or Download the repository 

Command to clone the repository:
```
$ git clone https://github.com/RonFrancesca/PhraseSound.git
```

The repository constist of multiple folders: 
- **abstraction**: folder with Pure Data Patch used by the Pure Data audio engine to generate sound. Please, do not move the folder (if you do it you will also need to change the path in the upf.sonificator.pd patch, inside the pd osc patch)
- **externals**: folder with Pure Data Patch used by the Pure Data audio engine to generate sound. Please, do not move the folder (if you do it you will also need to change the path in the upf.sonificator.pd patch, inside the pd osc patch)
- **PhraseSound_Client**: it contains the *main.py* script and three other folders:
  - **osc**: *osc_client.py* script which handle the comunication between client and server
  - **web**: *web.py* scripty which implement the Flask application, and two other folders, **static** which contains the *style.css* file and **templates** which contains the *index_basic.html* file. Please, do not move those two folders. 
  - **words2midi**: *w2midi.py* script, which it is in charge of calculating the distance between words, and two jupyter notebooks that the user can use as example in order to understand how the mapping between words and MIDI values work. Refer to the Jupyter Notebook instructions for how to install and use Jupyter notebook. 
  Inside this folder need to be added also the two files which need to be requested to the authors in order to make the system work. 
- **PhraseSound_Server**: *upf.sonificador.pd* which si the Pure Data audio engine to generate sound. Please, do not move the file ((if you do it you will also need to change the paths for the abtraction and externals folders, inside the pd osc patch inside the upf.sonificador.pd patch)

## Running the code

Open the PhraseSound_Server/upf.sonificador.pd patch. 

Typing on the terminal the following commands: 
```
$ cd PhraseSound_Client/web
$ export FLASK_APP=web
$ flask run
```

The web application is now up and running at the 127.0.0.1:5000 or 0.0.0.0:5000. 

Type your sentence and enjoy exploring the sound!

### Jupyter Notebook instructions
Install Jupyter Notebook according to the its instructions https://jupyter.org/install

Start up jupyter notebook

```
$ jupyter notebook
```

Follow the instructions appearing in the console regarding navigating your browser to the notebook


## Authors 
- Francesca Ronchini
- Marco Bertola 
- Miguel Perez Fernandez


