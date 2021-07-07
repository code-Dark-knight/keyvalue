import os
import argparse
import requests

#code

url="http://localhost:8080/subscribe/list"
def suball():
    result=requests.get(url)
    print(result.json())


def main():
    usagemsg="usage: getall [-h] requires key | ex getall"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature.',usage=usagemsg)
    my_parser.add_argument('suball', nargs="*",type=str)
    args = my_parser.parse_args()
    suball()




if __name__ == "__main__":
    main()

