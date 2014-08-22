from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

#es.indices.create(index='aceresources')


es.indices.put_mapping(
    index='aceresources',
    doc_type='articles',
    body={
        'articles': {
            'properties': {
                'id': {'type': 'integer'},
                'title': {'type': 'string'},
                'abstract': {'type': 'string'},
                'comments': {'type': 'string'},
                'URLS': {'type': 'string'},
                'citeulike': {'type': 'string'},
                'attachment': {'type': 'attachment',
                            "fields" : {
                            "title" : { "store" : "yes" },
                            "file" : { "term_vector":"with_positions_offsets", "store":"yes"  }
                            }
                },
                'authors': {'type': 'string'},
                'tags': {'type': 'string'},
                'created': {'type': 'date'}
            }
        }
    }
)

es.indices.put_mapping(
    index='aceresources',
    doc_type='links',
    body={
        'links': {
            'properties': {
                'id': {'type': 'integer'},
                'title': {'type': 'string'},
                'comments': {'type': 'string'},
                'delicious': {'type': 'string'},
                'URL': {'type': 'string'},
                'tags': {'type': 'string'},
                'created': {'type': 'date'}
            }
        }
    }
)


es.indices.put_mapping(
    index='aceresources',
    doc_type='books',
    body={
        'books': {
            'properties': {
                'id': {'type': 'integer'},
                'title': {'type': 'string'},
                'authors': {'type': 'string'},
                'date': {'type': 'string'},
                'comments': {'type': 'string'},
                'tags': {'type': 'string'},
                'cover': {'type': 'string'}
            }
        }
    }
)
