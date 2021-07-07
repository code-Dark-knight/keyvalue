import os
import requests
import argparse

#code

headers={"Content-Type": "application/json"}

def remove(params):
    url="http://localhost:8080/key/"+params.rem[1]
    result=requests.delete(url)
    print(result.json())

def main():
    usagemsg="usage: del [-h] requires key | ex del {key}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature.',usage=usagemsg)
    my_parser.add_argument('rem', action='store', nargs=2,type=str)
    args = my_parser.parse_args()
    if args.rem:
        remove(args)







if __name__ == "__main__":
    main()

