import time
from concurrent.futures import ThreadPoolExecutor

import requests


def crack_the_safe(password):
    url: str = 'http://code.qqmber.wtf/guess/'
    response = requests.post(url, json={'password': password})
    return [response.status_code, password, f'Check: {password}. {response}']


if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=32) as executor:
        future = executor.map(crack_the_safe, [f'{i:0{3}}' for i in range(0, 1000)])
        for res in future:
            if res[0] == 200:
                print(f'{res[2]}\nDone! Password is {res[1]}.')
                break
            else:
                print(res[2])

    end = time.time()
    # print(results)
    print(f'Cracking took: {end - start}s')
