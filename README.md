# key-value Service

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

* put {key} {value} : It's an update command.

* subs {key} : It will set the key in subscription list any changes done to that {key}.


# Prerequisite
- Docker (https://docs.docker.com/get-docker/) must be installed and running. 
 
- Python

- Pip
