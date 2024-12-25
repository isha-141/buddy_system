from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Journey
from django.urls import reverse
from django.shortcuts import render
from openai import OpenAI
from django.db import connection

def journeys(request):
    template = loader.get_template('index.html')
    allrequests = Journey.objects.all().values()
    context = {
        'allrequests': allrequests,
    }
    return HttpResponse(template.render(context, request))

def addRequest(request):
    template = loader.get_template('addRequest.html')
    return HttpResponse(template.render({}, request))

def saverequest(request):
    x = request.POST['pid']
    y = request.POST['fullname']
    z = request.POST['startingpt']
    i = request.POST['destination']
    j = request.POST['starttime']
    request = Journey(PID=x, fullname=y, start=z, end=i, start_time=j)
    request.save()
    return HttpResponseRedirect(reverse('journeys'))

def findBuddy(request):
    """Django view to run a Python script and return its output."""
    match = None  # Initialize output as None

    if request.method == 'POST':
        # Get the input text from the form
        user_input = request.POST.get('user_input', '')
        schema = """
        Tables:
        - journeys_journey (id, pid, fullname, start, end, start_time)
        """
        # Call your Python script logic with the input
        match = text_to_sql(user_input, schema)

    # Render the template with the script output
    return render(request, 'findBuddy.html', {'match': match})

def text_to_sql(natural_language_query, table_schema):
    client = OpenAI(
        api_key=PASTE KEY HERE
    )

    messages = [
        {"role": "system", "content": "You are an AI assistant that generates SQL queries from natural language."},
        {"role": "user", "content": f"Convert the following query to SQL: '{natural_language_query}'\nSchema: {table_schema}"}
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use gpt-4o-mini
            messages=messages,
            temperature=0,
        )
        sql_query = response.choices[0].message.content.strip()
        cut_query = extract_sql_query(sql_query)
        return custom_query_view(cut_query)

    except Exception as e:
        return f"Error: {e}"
    
def extract_sql_query(response_text):
    # Look for the SQL code block
    start_marker = "```sql"
    end_marker = "```"

    # Find the start and end of the SQL query
    start_index = response_text.find(start_marker) + len(start_marker)
    end_index = response_text.find(end_marker, start_index)

    # Extract and return the SQL query
    if start_index != -1 and end_index != -1:
        return response_text[start_index:end_index].strip()
    return "No SQL query found."

def custom_query_view(query):

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    return results
