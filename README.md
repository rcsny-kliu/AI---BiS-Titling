# BiS Creative Titling #
Version 2.0.0

Running using Python 3.7

Author(s): Sebastien V. & Kevin Liu

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
		* *par1: <class 'str'>, {"in":include,"ex":exclude} Default="in"*, Inclusion or exclusion of part-of-speech tag
		* *par2: <class 'list'>, Default=["noun"]*, List of parts-of-speech tags of interest
		* *par3: <class 'int'>, {1:word only, 0:word & part-of-speech tag} Default=1*, Output style 
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
		* *fuzztype: <class 'str'>, {"ratio":ratio,"partial":partial ratio,"weighted":(ratio+partial ratio)/2}*, fuzzy matching algorithm
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

### Data Collection Functions ###
* **bisProcess.image_scrape(dataframe,save_path=False,image_only=True,no_dupes=True,n_jobs=1)**
	
	Ccrape images using AWS S3 urls, outfitted with parallel
	
	* Parameters:
		* *dataframe: <class 'pandas.core.frame.DataFrame'>*, list of creative URLs must contain column "creative_url
		* *save_path: <class 'str'> Default=os.getcwd()*, folder path to save scraped images
		* *image_only: <class 'str'> Default=True*, scrape only acceptable image formats (True) 
		* *no_dupes: <class 'str'> Default=True*, scrape only creatives not found in save_path (True)
		* *n_jobs: <class 'str'> Default=1*, number of cores to dedicate towards scraping
	* Returns:
		* *object: <class 'pandas.core.frame.DataFrame'>*, list of creative URLs and the result from scraping 

### AWS Functions ###
* **bisProcess.s3_login(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)**
	
	Creates AWS S3 client
	
	* Parameters:
		* *AWS_ACCESS_KEY_ID: <class 'str'>*
		* *AWS_SECRET_ACCESS_KEY: <class 'str'>*
	* Returns:
		* *object: <class 'botocore.client'>* S3 client
		
#### ####
* **bisProcess.rekognition_login(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)**
	
	Creates AWS Rekognition client
	
	* Parameters:
		* *AWS_ACCESS_KEY_ID: <class 'str'>*
		* *AWS_SECRET_ACCESS_KEY: <class 'str'>*
	* Returns:
		* *object: <class 'botocore.client'>* Rekognition client
		
#### ####
* **bisProcess.parr_upload(client,file_name,upload_name)**
	
	Upload file objects to production bucket (hardcoded), outfitted for parallel usage
	
	* Parameters:
		* *client: <class 'botocore.client'>* S3 client
		* *file_name: <class 'str'>* file path to be uploaded
		* *upload_name: <class 'str'>* name object is to be saved as in bucket
	* Returns:
		* *object: <class 'bool'>* 

#### ####
* **bisProcess.process_creative(client, creative_name, bucket, path="output")**
	
	Submit and retrieve AWS Rekognition Detect Text results, results saved as JSON
	
	* Parameters:
		* *client: <class 'botocore.client'>* Rekognition client
		* *creative_name: <class 'str'>* object name in bucket
		* *bucket: <class 'str'>* 
		* *path: <class 'str'> Default="output"*, file path to output json results
	* Returns:
		* *object: <class 'bool'>* 

### Pipelines & Algorithms ###
* **bisProcess.preProcPipe(dataframe_text,dataframe_accountsInfo)**
	
	A series of text operations performed on both untitled BiS instances and MM-accounts list
	
	* Parameters:
		* *dataframe_text: <class 'pandas.core.frame.DataFrame'>* Untitled BiS instances
		* *dataframe_accountsInfo: <class 'pandas.core.frame.DataFrame'>* MM-accounts list
	* Returns:
		* *dataframe_text: <class 'pandas.core.frame.DataFrame'>* Pre-processed untitled BiS instances
		* *dataframe_accountsInfo: <class 'pandas.core.frame.DataFrame'>* Pre-processed MM-accounts list

* **bisProcess.feature_creation(dataframe)**
	
	Create feature set of fuzzymatching metrics
	
	* Parameters:
		* *dataframe: <class 'pandas.core.frame.DataFrame'>* Dataframe must have been preprocessed through bisProcess.preProcPipe for correct text operations and 				column name conventions
	* Returns:
		* *object: <class 'pandas.core.frame.DataFrame'>*

* **bisProcess.mm_search(dataframe_text,dataframe_accountsInfo,index_loc)**
	
	BiS instances one-to-one comparison against an accounts list to identify best match, outfitted for parallel usage
	
	* Parameters:
		* *dataframe_text: <class 'pandas.core.frame.DataFrame'>* Untitled BiS instances
		* *dataframe_accountsInfo: <class 'pandas.core.frame.DataFrame'>* MM-accounts list
		* *index_loc: <class 'int'>* integer index location of BiS instance to run match against
	* Returns:
		* *object: <class 'list'> [dataframe_full,dataframe_max]* contains both the full list of every match and the miaximized match with respect to mean

* **bisProcess.production_ML(max_number_rows,date_observed)**

	Production pipeline to map BiS instances for a given datetime
	
	* Parameters:
		* *max_number_rows: <class 'str'> Default="200000"*, Maximum number of BiS instances to process
		* *date_observed: <class 'str'> Default=datetime.datetime.now() - datetime.timedelta(1)*
	* Returns:
		* *dataframe: <class 'pandas.core.frame.DataFrame'>* Finalized full results of BiS mapping
		* *ml_model: <class 'pandas.core.frame.DataFrame'>* ML model used for fitting
		* *upload: <class 'json'>* JSON object uploaded
		* *upload_response: <class 'str'>*
