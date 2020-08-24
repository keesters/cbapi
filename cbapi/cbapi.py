import http.client
import sys
import json
import requests
import pandas as pd
from threading import Thread
from queue import Queue

RAPIDAPI_KEY = ''

def set_api_key(api_key):
    global RAPIDAPI_KEY
    RAPIDAPI_KEY = api_key
    
def get_api_key():
    return '35658967cbmsh78da30f62c42138p19349fjsnf03dfd67e446'

def trigger_api(query: dict,orgs: bool):
    api_key = get_api_key()
    headers = {
        'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    if orgs:
        tp = 'organizations'
    else:
        tp = 'people'
    url = 'https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-'+tp
    response = requests.request("GET", url, headers=headers, params=query)
    if(200 == response.status_code):
        return json.loads(response.text)
    else:
        return None
        
def get_data(query: dict,tp: bool):
    # trigger api and get data
    api_data = trigger_api(query,tp)
    # determine number of pages, current page
    n_pages = api_data['data']['paging']['number_of_pages']
    current_page = api_data['data']['paging']['current_page']
    # transform important data into pandas DataFrame
    try:
        df = pd.DataFrame(list(pd.DataFrame(api_data['data']['items'])['properties']))
    except:
        print("Error: Invalid Arguments")
        return
    # if pages > 1, trigger pages and append to df
    # use multi-threading to speed up pagination
    if current_page == 1 and n_pages > 1: # only run when page = 1
        # start a new thread for each page to avoid appending within each thread
        threads = list()
        results = Queue()
        for t_count in range(n_pages-1):
            # change the page to be queried
            query_tmp = {**query, 'page': t_count+2 }
            # recursively call function and send results to Queue
            threads.append(Thread(target=lambda q, query, tp: q.put(get_data(query,tp)), args=(results,query_tmp,tp)))
            threads[t_count].start()

        for t_count in range(len(threads)):
            threads[t_count].join()
            # append results from Queue
            # this will not necessarily append in order,
            # but we will append the same number of results as threads
            df = df.append(results.get(),ignore_index=True)
    
    # return DataFrame
    return df
    
def companies(**kwargs): 
  # accepts: 'name', 'locations', 'domain', 'types', 'updated_since'
  return get_data(kwargs,True)
      
def people(**kwargs): 
  # accepts: 'name', 'locations', 'socials','types', 'updated_since'
  return get_data(kwargs,False)
