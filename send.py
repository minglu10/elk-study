from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
es = Elasticsearch("http://localhost:9200", basic_auth=('elastic', 'changeme'))
#doc = {
#    'author': 'kimchy',
#    'text': 'Elasticsearch: cool. bonsai cool.',
#    'timestamp': datetime.now(),
#}
#resp = es.index(index="test-index", id=1, document=doc)
#print(resp['result'])
#f = open("psc-snapshot-2022-12-31_1of23.txt", "r")
#actions = [] 
#for line in f:
#    doc = json.loads(line)
#    actions.append({"_index":"test-index", "_source":doc })
#    if len(actions) > 1000:
#        print("sending")
#        bulk(es, actions)
#        actions = []
#
body = {
            "query": {
                "bool": {                    
                    "filter": [
                        {
                            "terms": {
                                "company_number": [
                                    "09145694",
                                    "08581893"
                                ]
                            }
                        }
                    ]
                }
            },
          
       }
resp = es.search(index="test-index", body=body)
hits = resp['hits']['hits']
print(hits)
    #resp = es.index(index="test-index", document=doc)