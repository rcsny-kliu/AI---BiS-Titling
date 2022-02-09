# BiS Creative Titling #
Version 1.0.0

Running using Python 3.7

### Usage Notes: ###

* First time users must run bisProcess.py which invoke bisProcess.py will iniatiate multiple pip install methods for packages.

### Module Installation ###
* **bisProcess.modInstall()**
	
	Installs modules relevant to BiS Titling process which are not included in Python 3.7 standard library.
	
	* Parameters:
	
		* *None*
	
	* Returns:
	
		* *None*

### Text Functions ###
* **bisProcess.remove_stop(text)**
	
	Remove stop words in a string, dependancy upon *nltk* stopwords
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'str'>*

#### ####
* **bisProcess.remove_punc(text)**
	
	Remove punctuation characters in a string
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'str'>*
		
#### ####
* **bisProcess.split_punc(text)**
	
	Tokenize string object 
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'list'>*

#### ####
* **bisProcess.pos_only(text,par1,par2,par3)**
	
	Tokenize and parse string object based on parts-of-speech tagging, dependancy upon *nltk* 
	
	* Parameters:
		* *text: <class 'str'>*
		* *par1: <class 'str'>, {"in":include,"ex":exclude} Default "in"*, Inclusion or exclusion of part-of-speech tag
		* *par2: <class 'list'>, Default ["noun"]*, List of parts-of-speech tags of interest
		* *par3: <class 'int'>, {1:word only, 0:word & part-of-speech tag} Default 1*, Output style 
	* Returns:
		* *object: <class 'list'>*
		
#### ####
* **bisProcess.split_url(text)**
	
	Tokenize string object, delimeters based on punctuation characters. Common url encoding character(s) excluded, such as "http", "https", "#", "@", "=", "~", ":", "
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'list'>*

#### ####
* **bisProcess.fuzz_comp(text,url,fuzztype)**

	Levenshtein distance between two lists of text strings 
 	
	* Parameters:
		* *text: <class 'list'>*
		* *url: <class 'list'>*
		* *fuzztype: <class 'str'>, {"ratio":ratio,"partial":partial ratio,"weighted":(ratio+partial ratio)/2*, fuzzy matching algorithm
	* Returns:
		* *object: <class 'list'>* 
		
#### ####
* **bisProcess.scoreCount(scores,thresh)**
	
	Count the number of elements which pass fuzzy matching score threshold

	* Parameters:
		* *scores: <class 'list'>*
		* *thresh: <class 'float'>*
	* Returns:
		* *object: <class 'int'>* 

#### ####
* **bisProcess.scorePerc(scores,thresh)**
	
	Percentage of the number of elements which pass fuzzy matching score threshold

	* Parameters:
		* *scores: <class 'list'>*
		* *thresh: <class 'float'>*
	* Returns:
		* *object: <class 'float'>* 

#### ####
* **bisProcess.repAbb(text)**
	
	Replaces words with their respective abbreviations in a text string
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'str'>*
		
#### ####
* **bisProcess.stateAbb(text)**
	
	Replaces states with their respective two letter abbreviations in a text string
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'str'>*

#### ####
* **bisProcess.remove_spec(text)**
	
	Remove all special characters in a text string
	
	* Parameters:
		* *text: <class 'str'>*
	* Returns:
		* *object: <class 'str'>*
		
