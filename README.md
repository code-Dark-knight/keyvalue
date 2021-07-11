# key-value Store

The approach is to use python flask framework to create a CRUD api which can store data in key value form in memory and similarly design a client in python which can fetch the values from the given api.

# language

* python
* shell

# Usage

* set {key} {value} : It will set key-value in {"key": {key} , "value": {value}}. set command only sets unique keys.

* get {key} : It will fetches the value of the given key.

* del {key} : It will delete the {key} | {value} pair. Any {key} that has been subscribed and delete will also be removed from the subscription list if not updated.

* getall : It will return all the {key} {value} pair at any point of time in KV-Store memory.

* suball : It will return a list of all the key which has been subscribed. These key will response to any changes done via put.

* put {key} {value} : It's an update command. Use this if you need to change the value in a existing key.

* subs {key} : It will set the key in subscription list any changes done to that {key}.


# Prerequisite
- Docker must be installed and running. 
 
- Python

- Pip

### Directory Structure

.
|--Dockerfile
|--README.md
|--build.sh
|--client
|    |--bin
|    |    |--kv-client
|    |
|    |--src
|        |--client.py
|        |--del.py
|        |--get.py
|        |--set.py
|
|--utility
      |--code
      |    |--app.py
      |--config.ini
      |--requirements.txt


#HOW to RUN

1.

$ cd into project

$ bash build.sh

SELECT option 1 if you are running the project for the first time. The output will be similar to this:

```
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice :
```

2.
RUN the script again.

$ bash build.sh

Then choose option 2 to run the client.

#How to perform operations in the client

- Setting a Key

[set key value] ---> ex.: set name ashish


- updating an existing key
 [put key updatevalue] ---> put name ashish-sharma


- Getting a Key

[get key] ---> ex.: get name


- Deleting a Key

[del key] ---> del name


- Get all the Key

[get-all key] ---> ex.: getall


- Subscribe get for any changes

[subs key] ---> subs name

- To check subscription on key at any given time you can `suball` to get all the keys that you have subscribed.


# CI/CD  pipeline using AWS Codebuild, Codepipeline and Codedeploy

buildspec.yaml is the files that builds the Dockerfile and pushed in into ECR(Elastic Container Registry) for secure image storage and it can be pulled for various use-cases. 
