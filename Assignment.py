import requests
from flask import Flask, jsonify

def get_citations(api_url,page):  
  response = requests.get(f"{api_url}?page={page}") #url+page numbers
  data = response.json()
  response = data['data']['data'][0]['response']  #responses
  source = data['data']['data'][0]['source']      #source
  citations = []    #empty list citations
  for entry in source:
      entry.pop('context', None)  #removing context from source
      if entry.get('link'):       #filtering of available links and id's
          citations.append(entry) #then appended them into citations list
  return citations

app = Flask(__name__)

@app.route('/', methods=['GET'])
def citations_data():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    pages_to_fetch = 14     #NO of pages 
    all_citations = []
    for page in range(pages_to_fetch):     #pages in range 0-14
        citations = get_citations(api_url, page)   #running the functions upto 13 pages
        all_citations.extend(citations)     #all citations
    return jsonify(all_citations)             

if __name__ == '__main__':
    app.run(debug=True)