#!/usr/bin/python3
"""gathers data from an api"""
import re
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            username = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                    'Employee {} is done with tasks({}/{}):'.format(
                        username,
                        len(todos_done),
                        len(todos)
                        )
                    )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
