from flask import Flask
from flask import render_template
from pybtex.database.input import bibtex

app = Flask(__name__)

@app.route('/')
def index():
    # Show search form
    # Show tag cloud
    # Show stats (n books in Oldham, n books in Oxford, n references with attachments)
    # Show most recent entries
    return render_template('index.html')
    return 'Index Page'

@app.route('/bibfile/<bibfile>')
def show_bibfile(bibfile):    
    # Get All elements in a bibtex file
    # Present nicely - like the bibtexbrpwser.php does
    bib_data = parser.parse_file(bibfile+'.bib')
    return render_template('base.html',bib_data=bib_data)
    return 'Index Page'
   
@app.route('/bibentry/<bibentry>')
def show_bibentry(bibentry):
    # show the entry for a bibtex entry
    return 'User %s' % bibentry

@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        request.args.get('key', '')
        bib_data = parser.parse_file(bibfile+'.bib')
        # do some clever auto-detection of the kind of item it is..
        # text: search authors, abstract, tags, 
        # year: year
        # doi or isbn or some kind of url.. 
        # and options:
          #has attachments (or in our library) - true or false
        # search attachments
        # https://github.com/willowtreeapps/flask-solr
        # https://github.com/toastdriven/pysolr

def search_bibtex

if __name__ == "__main__":
    parser = bibtex.Parser()
    app.run(debug=True)