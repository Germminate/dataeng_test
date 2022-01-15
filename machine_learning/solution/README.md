# 5. Machine Learning
This section comprise the machine learning algorithm and data required for the algorhtim to make its predictions.

<br>

## Dataset
### Data Attributes
The dataset contains the following attributes (in order):

![](../../misc/model_desc.png)

The above attributes are also listed in [data attributes file](data/car.attributes-names)

For more information on the data description, please refer to [data description file](data/car.names)

Note: Acceptability refers to Class Value.

<br>

## Modeling

### Objective
The objective of the model is to predict the buying price of the car given the input variables (features of the car).

### Inputs Requirement
The variables that the user is allowed to input include all the attributes listed in the Data Attribute segment. However, there is a chance that several of these features 

### Model Selection
While deep learning methods can be used to complete this request, it is unnecessary and an overkill when a simple regression or classfication model can be used to achieve the same results.

As the buying price is a categorical variable, classification is adopted to predict the price of the vehicle to the nearest hundred.

### Approach

The below steps is my typical approach for data modelling:
  1. The data is first assessed to see if it tallies with the [data description file](data/car.names). Update data description file if it doesn't tally.
  2. Null values are imputed if they fall under key attributes.
  3. Data is balanced if required.
  4. Run a baseline training and prediction with just the key attributes.
  5. Optimise model (Dimensionality reduction, etc.).
  6. Evaluate model.
  7. Assess if any non-key attributes are useful and add them in to improve predictions (this requires industry knowledge, and for this case, it's based on my understanding of what affects a car price)

### Actual Steps
As the data is clean (no null values or columns), all available attributes are key attributes, steps 2, 3, and 7 are omitted.
Due to time constraint, 4 is omitted.

## Instructions for user

__Ideal case:__
To run the model, run `docker build -t model_docker ../docker/. && docker run --rm -it model_docker ./predict.py -c config/config.json`.

__Currently:__
There are issues with the support for the installation of packages required for the repository aarch64 builds. Installing the packages after accessing a vanilla python 3.9 docker container works, but installing it as a part of the requirements.txt results in the build context failure. There are also issues installing it with a modified image (see ^[Dockerfile](../docker/Dockerfile)). 

As there isn't enough time to figure out the root cause of this issue and the alternative method of installing it via docker context is also dirty, I have decided to install everything (chrone and packages) after accessing a vanilla python 3.9 docker.

^ In production cases, the [docker directory](../docker) will not be committed. In this case, it is committed for explanatory purposes.

The steps are as follows:
1. `docker pull python:3.9` 
2. `docker run --rm -it -v /path/to/repository:/path/in/docker python:3.9 sh`
3. `cd /path/to/mapped/repository/solution/dir`
4. `pip install -r requirements.txt`
5. `./predict.py -c config/config.json`


You should see the below for step 5:
```
# ./predict.py -c config/config.json
The predicted price based on the given parameters is LOW.
```

## Folder Structure
```
.
|____solution
| |____requirements.txt
| |____config
| | |____config.json
| |____predict.py
| |______init__.py
| |____components
| | |____dataset
| | | |______init__.py
| | | |____parser.py
| | |______init__.py
| | |____utils
| | | |____encoding.py
| | | |______init__.py
| | | |____dimensionality_reduction.py
| | | |____confusion_matrix.py
| | |____model
| | | |______init__.py
| | | |____random_forest.py
| |____data
| | |____car.data
| | |____car.attributes-names
| | |____car.names
|____README.md

```

All scripts and data are stored at `solution`. 

Ideally, there is a remote storage volume to store datasets and they are called from these remote volumes.

<br>

## Conclusion
Given more time, I would like to achieve the ideal case of containerize for the module for alpine docker.

Also, I would like to improve the model by using dimensionality reduction methods.