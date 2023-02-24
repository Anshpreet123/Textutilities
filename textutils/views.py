# i have created this file ...
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    kill={'name':"god" , 'place':'heaven'}
    return render(request, 'index.html',  kill)

def about(request):
    return HttpResponse("<h1>Abotu</h1>")

def home(request):
    return HttpResponse('''<h1>home</h1><br><a href ="navigation"><button>navigation</button></a>
    <br><a href ="newline"><button>newline</button></a>
    <br><a href ="capfirst"><button>capfirst</button></a>
    <br><a href ="/"><button>back</button></a>''')

def navigation(request):
    return HttpResponse('''
    <div>
    <a href="https://internet.iitb.ac.in/logout.php">Internet.IItb</a><br>
    <a href="https://chat.openai.com/chat">Chat Gpt</a>
    <br><a href ="/"><button>back</button></a>
    </div>
    
    ''')

def newline(request):
    return HttpResponse("newline")

def analyse(request):
    djtext=request.POST.get('text', 'default')
    print(djtext)
    removepunc=request.POST.get('removepunc', 'OFF')
    print(removepunc)
    capital=request.POST.get('capital','OFF')
    print(capital)
    line=request.POST.get('line','OFF')
    print(line)
    charcount=request.POST.get('charcount','OFF')
    print(charcount)
    if removepunc=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed=''
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        dicto={'process':'Remove Punctuations' ,'analysed': analysed}
        djtext=analysed
        # return render(request, 'analyse.html',dicto)
    if capital=='on':
        analysed=djtext.upper()
        dicto={'process':'Capitalised' ,'analysed': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', dicto)
    if line=='on':
        analysed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analysed=analysed + char
        dicto={'process':'Line Remover' ,'analysed': analysed}
        djtext=analysed
        # return render(request, 'analyse.html', dicto)
    if charcount=="on":
        i=0
        for char in djtext:
            i=i+1
        dicto={'process':'Number of Characters' ,'analysed': i}
        djtext=analysed
        # return render(request, 'analyse.html', dicto)
    return render(request, 'analyse.html', dicto)
def capfirst(request):
    return HttpResponse("<h1>capfirst</h1>")


def nospace(request):
    return HttpResponse("<h1>nospace</h1>")


