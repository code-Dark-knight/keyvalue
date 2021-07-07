import os
import argparse

#code

def msg(name=None):
    return '''[get [key]] [set [key] [value]] [del [key]]
        '''


def main():
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature.',usage=msg())
    my_parser.add_argument('get', action='store', nargs=2,type=str,help="It fetches the value")
    my_parser.add_argument('getall', action='store', nargs=2,type=str,help="It fetches all the value in the keyvalue store")
    my_parser.add_argument('set', action='store', nargs=3,type=str,help="It will set the key value")
    my_parser.add_argument('del', action='store', nargs=2,type=str,help="It remove the key")
    my_parser.add_argument('put', action='store', nargs=2,type=str,help="It updates the exisitng key or will insert a new key/value")
    my_parser.add_argument('subs', action='store', nargs=2,type=str,help="To set subscription on defined key")
    my_parser.add_argument('suball', action='store', nargs=2,type=str,help="Will show all the key which have subscription")
    my_parser.add_argument('-v', '--version', action='version',version='%(prog)s 1.0', help="version number.")
    args = my_parser.parse_args()
    parser.print_help()




if __name__ == "__main__":
    main()

