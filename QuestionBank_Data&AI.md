Question Bank for Interviews


 General Guidelines
1.	The objective of this document is to prepare a question bank that can be utilized as a handy reference for everyone for their interview preparation.
2.	Kindly maintain the consistency in the document so that it remains easy to navigate.
3.	Insert a new page, copy the template page, and edit the same by changing the required details.
4.	Kindly update the “Table of Contents,” “Last Updated", "Last Updating Author” whenever you add any of your content.
5.	Feel free to provide any feedback and help us improve it.
 Tables of Contents
1.Preeti Bhatt – 20.07.2026 Template Page

Client Industry (Optional)	Financial Services
Role 	Python Developer
Topics or Tags	Python, Pandas, Programming
	
	
	
 

1
1.	What is PEP 8 and why is it important?
2.	What is Scope in Python?
3.	What are lists and tuples? What is the key difference between the two?
4.	What are modules and packages in Python?
5.	What is self in Python? 
6.	What are decorators in Python? 
7.	What is lambda in Python? Why is it used? 
8.	What are generators in Python? 
9.	Can you create a series from the dictionary object in pandas?
10.	 How will you delete indices, rows, and columns from a data frame? 
11.	 Can you get items of series A that are not available in another series B? 
12.	How are NumPy arrays advantageous over python lists? 
13.	Write python function which takes a variable number of arguments. 
14.	WAP (Write a program) which takes a sequence of numbers and checks if all numbers are unique.










Microsoft Interview:

Client Name (Optional)	Microsoft
Client Industry (Optional)	Software product 
Role 	Delivery Data Scientist
Topics or Tags	Python, Machine Learning, Deep Learning
	
	

•	Eigen value and eigen vector in PCA (Principal Components Analysis).
•	Difference between exogenous and auto regression in time series forecasting.
•	Describe prophet model, univariate and multivariate
•	Difference between normalization and standardization, will it be used before train test split or after?
•	How to reduce the impact of one feature than others
•	Difference between xgboost and fbprophet.
•	Describe the scenario where you do not make stationery data in time series forecasting problem
•	Bert is trained on which dataset? What model will be used if Bert does not exist? Describe self- attention mechanism.
•	Difference between univariate and multivariate time series forecasting problems.
•	What features will you use to forecast sales volume?
•	Elaborate oops concept.
•	They gave me a problem to write a code to get the subset of elements of dataset which satisfied a condition to have sum equal to given constant value.

•	Problem to code on Notepad: Find the middle node of a given LinkedList. Used two pointer approach Slow Pointer = node.next, and Fast pointer = node.next.next; at each iteration check if any of the pointer equals to null. When fast pointer is null slow pointer will be at the middle node just print node.data to get the result. 

•	 Problem to code on Notepad: Print all the permutations of give string. There are two approaches for this either we can use permute library or we can code using loops in O(n^2).

•	Problem to code on Notepad: Third last node of LinkedList, above mentioned two pointer approach will be used here as well.
•	Difference between call by value and call by reference. In call by value, we pass the copy of variable in the function whereas in call by reference we pass the actual variable into the function. How we do that? We pass the memory address of that variable to the function. These concepts are used with pointers in C/C++.
•	Difference between == and === in JavaScript. Both are used for comparison double equal to is a content comparator whereas triple equals compares both content and data types of LHS & RHS.
•	Since Java was mentioned in my resume so panel asked for one or two basic stuffs on OOPs.
•	Breadth-first search & Depth first search.
•	Basic ML questions related to projects mentioned on my resume.
•	Last question was how will you proceed with the AI/ML solution for a given business case. 


British Petroleum Interview:
Client Name (Optional)	BP
Client Industry (Optional)	Software product 
Role 	Delivery Data Scientist
Topics or Tags	Python, Pandas time series, Machine Learning
	
	


•	Difference between Data Frame and Table. -Both are actually same implementations wise and data frame can perform all kinds of operations that a table do. The only difference is with indexing, indexing in table allows us to do parallel processing of big data sets over cluster of nodes. Reducing our query time.

•	What is the limit of Data frame, when it will overflow. - There is no any fixed limit as such it depends on the underlying hardware of machine, data frame will overflow once the ram capacity is reached. 
•	Pandas date & time functions.
•	In a data frame there is date column replace it with following Friday's date. First convert date column to pd.datetime(), then use pd.timeseries.offset.week(Weekday = 4).
           Code => dataframe[‘date’] = dataframe[‘date’] + pd pd.timeseries.offset.week(Weekday = 4).
This code will replace all the dates with coming Friday's date that means if the current day is Friday, it will replace it to next Friday’s date. If we do not want that, modify the above code by introducing where clause.
df['date] = df['date'].where( df['date'] == (( df['date'] + Week(weekday=4) ) - Week()), df[date] + Week(weekday=4))


Microsoft Interview:

Client Name (Optional)	Microsoft
Client Industry (Optional)	Software product 
Role 	Delivery Data Scientist
Topics or Tags	Python, Machine Learning
	
	



•	What is type-1 and type-2 error, explain with a project related example
•	Explain R*2 
•	Gave different scores of R*2 and MAE (Mean Absolute Error) and asked when to use when using scores and in general
•	A client came with a turbine problem where the turbine fails for every 30 years but we only have data for the past 2 years. In this case what should we mention to the client. How to produce a solution
•	Explain differences between bagging and boosting techniques
•	Gave scores of ROC-AUC curve and Precision and asked when to use when
•	What is the floor of ROC-AUC curve
•	How to handle an imbalanced dataset
•	Explain about SMOTE technique and how it is different from oversampling
•	Which one to use first train-test-split or smote
•	How to decide how many clusters must be present
•	How to know for sure if the data in different clusters are not overlapping
•	Few other project-based questions and scenario-based ones.
 
Microsoft Interview:

Client Name (Optional)	Microsoft
Client Industry (Optional)	Software product 
Role 	Delivery Data Scientist
Topics or Tags	Python, Machine Learning
	
	



•	Explanation of the past project. What were the features used and how did you determine performance?
•	What is the difference between linear regression and logistic regression?
•	What is the internal working of logistic regression (LR)?
•	What is the loss function of LR?
•	Name some hyperparameters used in LR? Why do we use regularization?
•	When do we use accuracy as a metric? When should we not use accuracy?
•	How do you deal with imbalance data?
•	What is SMOTE and how is it different from stratified sampling?
•	Watch this video to understand how SMOTE works [https://www.youtube.com/watch?v=U3X98xZ4_no]
•	What is better 0.51 AUC (Area Under the Curve) or 0.43 F1 score? Which one should you present to a client?
•	Watch this video to understand how AUC is interpreted [https://www.youtube.com/watch?v=mUMd_cKU0VM]
•	What does the ROC AUC value signify?
•	Do we only use the threshold of 0.5 or can we use other thresholds in LR? If yes, how do we find them?
•	Can I use a sales forecasting model built using pencils data to be used in erasers data?
•	How would you compare the performance of two forecasting models?
•	What are the different metrics used in regression analysis? Which metric should be used where?
•	How do you build a testing pipeline for a data science model? [https://www.kdnuggets.com/2020/08/unit-test-data-pipeline-thank-yourself-later.html]

 
Microsoft Interview:

Client Name (Optional)	Microsoft
Client Industry (Optional)	Software product 
Role 	Delivery Data Scientist
Topics or Tags	Python, Machine Learning
	
	


•	What is logistic regression? How can we use it for more than two class classification?
•	What is bias and variance? 
•	How do you remove lines using OpenCV ?
•	How do you measure accuracy of a model?
•	How do you deal with imbalanced data?
•	How do you deal with imbalance data?


Author	Vismaya
Date	21st Oct 2021
Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	Data Scientist
Topics or Tags	Python, Machine Learning, Deep Learning


•	Iterators and generators
•	Python constructors
•	Map function
•	How do you flatten an image(matrix) in a deep learning architecture
•	Difference between semantic segmentation and segmentation
•	Different types of pooling operations – the visual effect of applying a max pooling operation and average pooling operation on an image
•	Math behind convolution operation – size of a particular image (128*128) after convolution operation with a 3*3 kernel
•	Size of a 3*3 image after applying 1*1 kernel 
•	Loss function and optimization function of region proposal network
•	Image down sampling – why do we do down sampling
•	Python coding: Solve the following using a for loop, by defining a function and put in inside a class
o	#Input : a =[1,2,3]
o	#Output : ["hello1","hello2","hello3"]
•	Tradeoff between yolo and faster rcnn in terms of speed and accuracy
•	About different deep learning architectures (Tensorflow, Keras, Caffe)
•	 What are feature maps and how are they obtained

Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	Data Scientist
Topics or Tags	Python, Statistical analysis, correlation matrices ,Pandas
	
	


1.	Count unique values in a data frame column.  
2.	Convert a column data type to string
3.	Obtain correlation coefficient between 2 columns in a data frame
4.	Merge two data frame based on common column (when column name is same)
5.	Merge two data frames base on common column name (column name is different in left and right data frame) 
6.	Define is correlation 
7.	What are the types of correlation coefficient??
8.	What is the difference in Pearson correlation coefficient and spearmen correlation coefficient???
9.	How do we deal with categorical variables for statistical analysis???
10.	How do you obtain correlation between 2 categorical variables? 
11.	How do you find Correlation between one categorical variable and other numerical variables? 
12.	 Difference between dictionary and list
13.	How do you append a dictionary with another dictionary? 
14.	Difference between tuples and list
15.	Does tuple can have different data types of element
16.	How do you read data from database directly and convert it into data frame for analysis?
17.	How do you import file.py function into another python file?
18.	What is generator in python 
19.	Print index and values of a list without range function.

 Mixed Bag:

1) Given the list below, answer the following question:
mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
What is the result of max(mylist)?

2.a) Quick Cheat Sheets
2.b) why-do-we-take-n-1-when-calculating-sample-variance-why-is-it-useful

3) Considering the list below, answer the following question.
list1 = [10, 211, 99.99, 50.75, 11.5]
Which element is sorted(list1, reverse = True)[1] ?

4) Given the list below, answer the following question:
mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
Who is mylist[:7]?

5) Given the list below, answer the following question:
mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
Who is mylist[:-6] ?
6) Given the tuple below answer the following question.
mytuple = (100, 250, 300, 450, 500, "Python", "Java", "C++")
What is the result of (mytuple + (410, 430, 450, 205 * 2, 900 // 2, 445)).count(450) ?

7) Given the tuple below answer the following question.
mytuple = (100, 250, 300, 450, 500, 650, 700, 850, 900)
What is the result of mytuple[1::3] ?

8) Given the range below answer the following question.
myrange = range(10, 16, 2)[::2]
What is the result of list(myrange) ?

9) Given the range below answer the following question.
myrange = range(5, 15, 4)[::-1]
What is the result of list(myrange) ?

10) Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
Which is the correct way of deleting Estonia from the dictionary?

11) Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
What is the result of max(ee_countries.keys()) ?

12) Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
What is the result of max(ee_countries.values()) ?

13) What is the cause of the TypeError below?
>>> test = {['Ukraine', 'Poland', 'Romania']: [43.7, 38.1, 19.5]}
Traceback (most recent call last):
 File "<pyshell#52>", line 1, in <module>
   test = {['Ukraine', 'Poland', 'Romania']: [43.7, 38.1, 19.5]}
TypeError: unhashable type: 'list'

14) Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
How can you add multiple key-value pairs to the dictionary, at the same time (using a single line of code) ?
Example: 'Latvia': '1.9M', 'Lithuania': '2.8M', 'Belarus': '9.4M'

15) Considering the dictionary below (showing the population of some of the Eastern European countries) answer the following question.
ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
What is the result of sorted(ee_countries.keys(), reverse = True)[1] ?


16) What is the result of the code below?
try:
  t1 = "100 kilometers"
  t2 = "2.5 hours"
  ("With a {2} km/h speed you will travel {0} km in {1} hrs").format(t1[:3], t2[-9:-6], t1[:3]//t2[-9:-6])
except ZeroDivisionError:
  print("Oups! You're trying to divide by 0! :(")
except IndexError:
  print("You got your indexes messed up!")
except TypeError:
  print("You got your data types messed up!")

17) What is the result of the code below?
def my_first_function():
  print("Hello Python!")

Schlum Interview:

Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	MLOps Engineer
Topics or Tags	Docker, AWS, Ops
	
	



•	What is the difference between Docker and Containers?
•	How do you restart containers on failure?
•	How do you run a container in Docker?
•	Can you run a program that takes 4 hours to run in AWS Lambda?
•	What is the difference between ADD and COPY commands wrt. Dockerfile ?
•	Experience with different AWS services such as CloudFormation or Glue?
•	What is the schema in S3?
•	Can the lambda written in AWS interact with other infrastructure?
•	What is the Dockerfile setup if you want to expose the model as an API?
•	Difference between UDF, pandas UDF and pyspark UDFs?
•	Difference between synchronous and asynchronous request? How do you program one in Python?
•	What is the use of a DAG (Directed Acyclic Graph) in Spark?
•	Given the no. Of terms, print the Fibonacci sequence: Hint try both iterative and recursive methods [https://www.programiz.com/python-programming/examples/fibonacci-sequence]
•	Given an input string, print the length of the longest common substring without any repeating characters. [https://leetcode.com/problems/longest-substring-without-repeating-characters/]
•	Given an input string, write a function that returns the Run Length Encoded string for the input string. For example, if the input string is “ssslbbbbppiitttc”, then the function should return “s3l1b4p2i2t3c1”

def encode(message):
    encoded_message = ""
    i = 0
   
    while (i <= len(message)-1):
        
        count = 1
        ch = message[i]
        j = i
        
        while (j < len(message)-1):
            
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
                
        encoded_message = encoded_message + ch + str(count)
        i = j+1
        
    return encoded_message
  
#Provide different values for message and test your program
encoded_message=encode("ssslbbbbppiitttc")
print(encoded_message)



Schlum Interview:
Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	MLOps Engineer
Topics or Tags	Docker, AWS, Python
	
	

•	Given an input string, write a function that returns the Run Length Encoded string for the input string. For example, if the input string is “ssslbbbbppiitttc”, then the function should return “s3l1b4p2i2t3c1”
•	Difference b/w Iterators and Generators
•	Knowledge on AWS Services
•	How can we transfer data from AWS to GCP/Azure?
•	How do you create the ETL Solution loading the data daily. currently on AWS to migrate to Azure/ GCP.
•	Working Exp on Docker?
•	CI/CD implementation
•	Tools used for versioning models
•	What is PaaS VS Faas

ABI Interview:

Author	Vinay S
Date	03th Jan 2022
Client Name (Optional)	ABI
Client Industry (Optional)	
Role 	Python Developer 
Topics or Tags	Python


•	{'Name': ['Santosh', "Sourab", "Hrishi", "Nitin", "Ajay"], 'Age': [11, 12, 11, 15, 13], 'Marks': [35, 30, 50, 40, 25] } Write the Python code Using Data Frames
•	2) Columns 1: Pass/Fail ==> Above 35 of marks Pass - Include this in the Above Code
•	3) Difference b/w Tuple, List & Dictionary
•	4) Example the Dictionary




Author	Harish
Date	06-Jan-2022
Client Name (Optional)	ABI
Client Industry (Optional)	 
Role 	Python Developer
Topics or Tags	Python, pandas, numpy
 
 
 
·	Difference between tuples, List, Dictionary? Explain by coding.
·	(1, 2, 3, 4, [5, 6, 7, 8]) update the tuple?
·	Dictionary Keys can be updated? Explain by coding?
·	What are pandas, numpy?
·	Explain OOP’s Concept?
·	What are different types of methods?
·	Explain by coding Abstract Class
·	Explain by coding Lambda Func()?

Client Name (Optional)	ABI
Client Industry (Optional)	 
Role 	Python Developer
Topics or Tags	Python, pandas, numpy
	
	

1) what does mutable and immutable mean with respect to list, tuple, and dictionary
2) t = (1, 2, 3, 4, [5, 6, 7, 8]) can we modify it ? if yes then how?
3) can we use a list as a key in the dictionary? Explain
4) write lambda function to calculate cube of the number
5) find the cube of all the numbers in the range 1 to 10 without using for loop, and make use of lambda function or list comprehension.

Author 	Medha Ray
Date 	3rd Feb 2022
Client Name (Optional) 	ABI 
Client Industry (Optional) 	
Role  	Python Developer 
Topics or Tags 	Python, OOPs, Pandas, Numpy 
 
1.	Example of Dictionary?
2.	Following examples are dictionary or not? {[1, 2, 3]: "One/Two/Three"}, {(1, 2, 3): "One/Two/Three"}
3.	Print the even numbers of all the numbers in the range 1 to 10 without using for loop and make use of lambda function and list comprehension. 
4.	What are different types of methods? Explain by coding.
5.	Create a data frame and then add the new column:
6.	{'Name': ['Medha', "Sourab", "Hrishi", "Nitin", "Ajay"],
 'Age': [11, 12, 11, 15, 13],
 'Marks': [35, 30, 50, 40, 25]}
 New Column 1: Pass/Fail ==> Above 35 of marks Pass


Schlum interview:
Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	Data Engineer
Topics or Tags	Cloud, SQL, Programming, Docker
	
	



1.	Given a list, ls = [9,8,3,4,1,0,2,7,7,6], write a function to get nth highest element without using any inbuilt functions or sorting.
2.	Write a python class with method to sort a list and related questions on classes, static methods, init etc.
3.	Difference between RANK and DENSE RANK?
4.	Difference between parquet and csv file format? How are files written in a parquet file?
5.	Knowledge of Cloud services
6.	What is Cursor command in SQL?
7.	Difference between Spark vs MapReduce architecture?
8.	Explanation of ETL pipeline
9.	Containerization v/s virtualization
10.	What is port redirection in docker?
11.	Experience with data engineering?
12.	How to create a table with Databricks storage?
13.	Difference between SQL and NoSQL DB? 
14.	A scenario where data keeps on changing, with adding and updating new features , would you consider SQL or NoSQL?
15.	 Difference between iterators and generators
16.	Difference between OLAP and OLTP?

Levi Interview:

Client Name (Optional)	Levi
Client Industry (Optional)	
Role 	MLOps Engineer
Topics or Tags	Docker, Jenkins,Airflow
	
	

1.	Create a dataframe.
2.	Create a list and sort it
3.	Sort it without using any function(bubble sort)
4.	Pandas Transform questions
5.	Sql join questions(left join)
6.	Why random forest is more interpretable than xgboost
7.	Hyper Parameter tuning
8.	Gradient descent
9.	Where are the predictions stored after calling Model API. (sql database)
10.	Deployment Related questions.
 
Mlops
1.	Airflow experience
2.	Explain flow of MLops
3.	Knowledge on Jenkins, GitHub
4.	Which database to use for storing images (Blob)
5.	What data can be stored in ML metadata store (Model Hyperparameters, Columns used in model)
6.	Knowledge of docker and Kubernetes
7.	Knowledge of Redis
8.	Knowledge of spark
9.	What is the entry point in docker file (Base image)
10.	What tools will you use if you are building MLops platform for developer and manager?

Schlum Interview:

Client Name (Optional)	Schlum
Client Industry (Optional)	
Role 	Data Scientist
Topics or Tags	Cloud, SQL, Programming, Docker, ML
	
	


1.	Write a Docker file.
2.	What is randomness in Random Forest.
3.	How bagging and boosting works.
4.	How do you evaluate a classification and Regression in Bagging and Boosting.
5.	How weak learners combine to from strong Learners.
6.	How will u divide I/P data to weak learners in Ensemble Learning.
7.	What is stemming and lemmetization.
8.	Create a Dataframe from series.
9.	30 pages returned , 20 are relevant , failing to return 40 other relevant pages . Create Confusion matrix.
10.	SQL queries- Creating table , inserting to table , search usinh where and %like , case sensitive and insensitive search .


Levi Interview:

Client Name (Optional)	Levi
Client Industry (Optional)	
Role 	 Data Engineer
Topics or Tags	Spark, python, sql ,AWS
	
	

Questions-
1.	what is a parquet file? why we use?
2.	what all data files/sources/db you have used?
3.	experience with deployment?
4.	actions v/s transformations with examples
5.	data engg pipeline
6.	lazy evaluation?
7.	scala v/s python performance with big data
8.	 experience with data engg tools - airflow etc?
9.	 narrow v/s wide transformations
10.	 shuffle operation in spark? where is it used?
11.	 other questions based on my work experience in data engineering/big data.
12.	 Read claim.parquet file and get count of rows(in both spark as well as python)
13.	 Perform a join operation with another table
14.	explain left join with example
15.	 write a group by query and filter if sum(amount)>10000 after grouping

=====================================================================

1.	Difference between pivot table and groupby and which is better.
2.	[[1,2,3],[4,5,6],[7,8,9]] find the sum of both diagonal. Write the python code for it.
3.	Why there are three different methods pop,remove,del for list.
4.	Basic knowledge of list,tuple,dictionary etc.
5.	Pandas .loc and .iloc method.
6.	Negative indexing in list
7.	Basics of visualization.
8.	Libraries used in your previous project.
9.	How to use map and why it works faster
10.	Group by 2 states top 2
11.	Delete every 3 row in the dataframe
12.	Add a column in the dataset
13.	Find duplicates in 2 list
14.	Can we add 2 tuples
15.	Read multiple csv files from a location
16.	Merge 2 arrays 
Trainset=np.array([1,2,3])
Testset=np.array([0,1,2],[1,2,3])
Result set=([1,2,3],[0,1,2],[1,2,3])
17.	Which is faster to iterate list or dictionary
18.	5 tracks 25 cars . how many iterations/race will be taken to identify the best 2 performing cars 
19.	From a table employee get a super manager’s name . how will u excecute it ? create a separate table or do execution on this table only ?
Emp name    manager name 
Manager name  supermanager name 

