"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/docs/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
app = Flask(__name__)

###
# Jinja filters
###

def stripbib_filter(s):
    """ Strip {} at end and beginning of string """
    if s[:1] == '{':
        return s[1:-1]
    else:
        return s
    
app.jinja_env.filters['stripbib'] = stripbib_filter

###
# ES
###

from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://localhost:9200/')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    # Show search form
    # Show tag cloud
    # Show stats (n books in Oldham, n books in Oxford, n references with attachments)
    # Show most recent entries
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        searchtxt = request.form['searchtxt']
        if request.method == 'POST':
            items = []
            query = {'query': {
                 'filtered': {
                     'query': {
                         'query_string': {'query': searchtxt}
                     },
                     "highlight" : {
                        "fields" : {
                            "attachment" : {}
                        }
                    }
                 },
             },
            }
            #items = es.search(query, index='aceresources')        
            items = es.search(searchtxt, index='aceresources')            
        return render_template('search_results.html',searchtxt=searchtxt,returneditems=items['hits']['hits'])
        
###
# Internal functions
###

def prepare_item_for_web(bibentry):
    """ Prepares a bibtex entry for the web. e.g. urls all on one line, title, author etc.. standardised """
    return None
          
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
