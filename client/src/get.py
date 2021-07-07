import os
import argparse
import requests

#code

url="http://localhost:8080/key/"

def get(params):
    url="http://localhost:8080/key/"+params.get[1]
    result=requests.get(url)
    print(result.json())

def main():
    usagemsg="usage: get [-h] requires key | ex get {key}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature.',usage=usagemsg)
    my_parser.add_argument('get', action='store', nargs=2,type=str)
    args = my_parser.parse_args()
    if args.get:
        get(args)




if __name__ == "__main__":
    main()

