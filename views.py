from django.shortcuts import render, redirect
from .scrapper import scrape_pinterest_board, scrape_myntra
from .mapper import get_image_embedding, cosine_similarity

def index(request):
    return render(request, 'finder/index.html')

def analyze_webpage(url1):
    #Scrape both the websites
    pinlist=scrape_pinterest_board(url1) 
    myntralist=scrape_myntra('https://www.myntra.com/') #myntra page url
    #Find embeddings for each image
    pin_dict={}
    myntra_dict={}
    for img1,img2 in pinlist, myntralist:
        pin_dict[get_image_embedding(img1)]=img1
        myntra_dict[get_image_embedding(img2)]=img2
    #Find max. cosine similarities
    max_sim=-10
    max_vec=None
    for vec1 in pin_dict.keys():
        for vec2 in myntra_dict.keys():
            sim_score=cosine_similarity(vec1, vec2)
            if sim_score>max_sim:
                max_vec=vec2
    #Return path to that image
    return myntra_dict[max_vec]


       

def cli():
    print("Bring Your Board To Life!")
    url1=input("Enter the URL to your Board: ")
    analyze_webpage(url1)
    print("Found the best matches for you!")
