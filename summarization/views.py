from django.http import HttpResponse
from django.shortcuts import render
# Use a pipeline as a high-level helper
from transformers import pipeline

summarizer = pipeline("text2text-generation", model="kyukyuswe/t5-small-finetuned-xsum")
def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        summary = summarizer(input_text,max_length =250,min_length=30,do_sample=False)
        summary_ans = summary[0]['generated_text']
        return render(request,'index.html',{'summary':summary_ans})
    return render(request,'index.html')