# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def update_data():
    export default async function handler(request, response) {
      const result = await fetch(
        'http://worldtimeapi.org/api/timezone/America/Chicago',
      );
      const data = await result.json();
    
      return response.json({ datetime: data.datetime });
    }