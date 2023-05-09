from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from distutils import errors
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
import openai
from django.conf import settings
openai.api_key=settings.API_KEY
import os
import pandas as pd
data=pd.DataFrame()
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
import spacy
lemmatizer=WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

class Inputfunction(APIView):
    def post(self , request):
        input= request.data.get('input')
        print(input)
        if not input:
            return Response({"message":"please provide input text"})
        
        # match the user input 
        ChatGpt_data=InputOutput.objects.create(input=input)
        serializers=InputOutputSerializer(data=ChatGpt_data)
        ChatGpt_data.save()
        
        input_text=ChatGpt_data.input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Auto Response Generator \n\nQ: {input_text} \n\nA:\n",
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1,
        )
        output= response.choices[0].text
        print('----------------->>>>>',output)
        update_content=InputOutput.objects.filter(input=input_text).update(output=output)
        
        return Response({'msg':'Data Added Succesfully','status':'status.HTTP_201_CREATED','outout':output})   
    


class Mobile_Technology_WavesView(APIView):
    def get(self, request):
        technology_rows = Mobile_Technology_Waves.objects.all()
        serializer = Mobile_Technology_WavesSerializer(technology_rows, many=True)
        df1 = pd.DataFrame(data=serializer.data)
        print(df1)
        return Response({"message": "Data saved to CSV file"})
       
class TechnologiesView(APIView):
    def get(self, request):
        technology_rows = Technologies.objects.all()
        serializer = TechnologieSerializer(technology_rows, many=True)
        df2 = pd.DataFrame(data=serializer.data)
        print(df2)
        return Response({"message": "Data saved to CSV file"})
       

class WebScrapDataView(APIView):
     def get(self, request, format=None):
        page = requests.get("https://buildfire.com/mobile-technology-waves/")
        soup = BeautifulSoup(page.content, "html.parser")
        p_tags = soup.select("h2 + p")
        array=[]
        count=0
        pattern = r'\d+'
        for p_tag in p_tags:
            h2_tag = p_tag.previous_sibling.previous_sibling
            if h2_tag is not None and h2_tag.name == "h2":
                print(h2_tag.text)
            print(p_tag.text)
            question = re.sub(pattern, '', h2_tag.text)
            answer=re.sub(pattern, '', p_tag.text)
            scrappy=Mobile_Technology_Waves.objects.create(question=question,answer=answer)
            serializers=Mobile_Technology_WavesSerializer(data=scrappy)
            scrappy.save()
            count+=1
            if count==23:
                break
        return Response({"message":"scrap data successfully","status":"200","Data":array})
    
class WebScrapingView(APIView):
    def get(self, request, format=None):
        page = requests.get("https://www.ishir.com/blog/55810/top-15-emerging-technology-trends-to-watch-in-2023-and-beyond.htm")
        soup = BeautifulSoup(page.content, "html.parser")
        h3_tags = soup.find_all('h3')
        array=[]
        pattern = r'^\d{1,2}\b'
        for h3 in h3_tags:
            h3_text = h3.text.strip()
            question=h3_text
            question= question.replace(".", "")
            question = re.sub(pattern, '', question)

            # find the first paragraph tag after the h3 tag and extract its text
            paragraph = h3.find_next('p')
            if paragraph is not None:
                paragraph_text = paragraph.text.strip()
                answer=paragraph_text
            scrappy=Technologies.objects.create(question=question,answer=answer) 
            dict_data={"question":question,"answer":answer}
            array.append(dict_data)
        print(array)
        return Response({"message":"scrap data successfully","status":"200","data":array})
    
class CricketScrapingView(APIView):
    def post(self, request, format=None):
        urls = ["https://www.prep4ias.com/top-300-cricket-general-knowledge-questions-and-answers/","https://www.edubabaji.com/top-50-cricket-gk-questions-answers-in-english/"]

        array=[] 
        for index, url in enumerate(urls):
            if index ==0:
                    print(url)

                    response = requests.get(url)
                    html_content = response.content
                    soup = BeautifulSoup(html_content, "html.parser")
                    pattern = r'^\d{1,2}\b'
                    h3_tags = soup.find_all("h3")
                    count = 0
                    for h3 in h3_tags:
                        if count == 60:
                            break
                        question=h3.text
                        question=re.sub(r'\.', '', question)
                        question=re.sub(r'\d+', '', question)
                        # print(question)
                        answer=h3.find_next("p").text
                        answer=re.sub(r'\.', '', answer)
                        answer= re.sub(r'\bAns\b', '', answer)
                        data_dict={"question":question,"answer":answer}
                        array.append(data_dict)
                        # print(array)
                        count += 1
            if index ==1:
                    print(url)
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

                    response = requests.get(url,headers=headers)

                    soup = BeautifulSoup(response.content, "html.parser")

                    video_wrapper = soup.find("div", {"class": "jetpack-video-wrapper"})

                    ol_tag = soup.find('ol')

                    for li_tag in ol_tag.find_all('li'):
                        li_text = li_tag.text.strip()
                        strong_tag = li_tag.find('strong')
                        if strong_tag:
                            strong_text = strong_tag.text.strip()
                        else:
                            strong_text = None
                        
                        question=li_text
                        question=question.split('?')[0] + '?'
                        # print(question)

                        answer=strong_text
                        answer=answer[1:]
                        # print(answer)
                        data_dict2={"question":question,"answer":answer}
                        array.append(data_dict2)
        # print(array)
        for x in array:
            question=(x['question'])
            answer=(x['answer'])
            cricketdata=Cricket_Question_and_Answer.objects.create(question=question,answer=answer)
            serializer=CricketSerializer(data=cricketdata)
            cricketdata.save()
            return Response({"message":"scrap data successfully","status":"200","data":len(array)})