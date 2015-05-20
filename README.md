# kvittr
Exam project - ITM30614 - Spring 2015

## How to use
Start with forking this repository, then create a virtual environment.

```
# creating a virtual environment called kvittr
# in the directory called virtualenvironments
$> virtualenv virtualenvironments/kvittr

# Activates the environment
$> source virtualenvironments/kvittr/bin/activate

# Notice that (kvittr) has appeard, this indicates that the virtual
# enviroment kvittr is activated.
(kvittr)$> ls
    djangoprojects      virtualenvironments
(kvittr)$> cd djangoprojects/
(kvittr)djangoprojects $> ls
    kvittr

# Clone the repository that you just forked
(kvittr)djangoprojects $> git clone git@github.com:(your username)/kvittr.git
    Cloning into 'kvittr'...

# Install Django in the virtual environment
(kvittr)kvittr $> pip install Django
    Successfully installed Django

```