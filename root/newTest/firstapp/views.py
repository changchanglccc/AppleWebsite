from django.shortcuts import render,HttpResponse
from django.template import Template,Context

from firstapp.models import People
# Create your views here.
def first_try(request):
    person = People(name = 'Bob', job = 'officer')
    html_string = '''
        <html lang="en">
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.4/semantic.css" media="screen" title="no title">
        </head>
        <body>
             <h1 class="ui center aligned icon header">
                  <i class="hand spock icon"></i>
                    Hello,{{ person.name }}
             </h1>
        </body>
        </html>
    '''

    t = Template(html_string)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)