from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db


@main.route('/json')
def json():
    return '''{   
           "programmers": [   
           { "firstName": "Brett", "email": "brett@newInstance.com" },   
           { "firstName": "Jason",  "email": "jason@servlets.com" },   
           { "firstName": "Elliotte", "lastName":"Harold", "email": "elharo@macfaq.com" }  
          ],   
         "authors": [   
           { "firstName": "Isaac",  "genre": "science fiction" },   
           { "firstName": "Tad", "genre": "fantasy" },   
           { "firstName": "Frank",  "genre": "christian fiction" }   
          ],   
         "musicians": [   
           { "firstName": "Eric",  "instrument": "guitar" },   
           { "firstName": "Sergei", "instrument": "piano" }   
          ]}'''

