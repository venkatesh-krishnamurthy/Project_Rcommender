from django.shortcuts import render
from django.http import HttpResponse
import openai
import os
from dotenv import load_dotenv


load_dotenv()

# Create your views here.

openai.api_key=os.getenv('OPENAI_KEY',None)


# function for api call
def index(request):
    suggestions=None
    if openai.api_key is not None and request.method=='POST':
      skills=request.POST.get('skills')
      ideas=request.POST.get('ideas')
      
      sentence=f"Based on following skills: {skills} and project ideas: {ideas}, suggest 4-5 creative project ideas or suitable roles. Provide a brief description and rationale for each."
      try:
         response=openai.completions.create(
            model='gpt-3.5-turbo',
            prompt=sentence,
            max_tokens=500,
            temperature=0.7


         )
         suggestions=response.choices[0].text.strip().split('\n')
      except Exception as e:
         suggestions=[f'Error generating suggestions:{str(e)}']
    return render(request, 'home.html',{'suggestions':suggestions})