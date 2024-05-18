from django.shortcuts import render
import json, random
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'indexs.html')



main_morning=["idly","dosa","poori","upma","upma godhumai","ragi semiya","vendhaya kanji","pongal"]
chutney=["coconut chutney","tomato chutney","kothamali chutney","pulipu chutney","pudhina chutney"]
night_side=["mushroom guruma","coconut chutney","tomato chutney","kothamali chutney","pulipu chutney",
            "pudhina chutney"]
night_menu=["idlly","dosa","idiyappam","appam","rava upma",
            "godhumai upma","ragi idiyapam","adai",
            "chappathi","panner stuffed chapathi","panner stuffed chapathi"]
lunch=["sambar","rasam","sambar rice","kadalai kulambu","puli kulambu","guruma",
       "lemon rice","curd rice","vegetable rice","moor kulambu","ghee rice",
       "thakkali rice","urundai kolambu"]
sambar_side=["potato fry","pudalai","brinjal fry","carrot fry","beans fry","cabbage poriyal","valaikai fry",
            "kothavarangai poriyal","pasalai keerai fry","murungai keerai fry",]
rasam_side=["potato fry","brinjal fry","cabbage kuttu(yellow color)","valaikai fry","simple egg fry",
            "masala egg","mushroom fry"]
fry_side=["potato fry","brinjal fry","valaikai fry","mushroom fry"]
puli_side=["kothavarangai poriyal","cabbage poriyal","carrot and beans poriyal","keerai","appalam"]
lemonrice_side=["potato fry","brinjal fry","valaikai fry","mushroom fry","vadaga thovayal"]
def morning_function():
   main=random.choice(main_morning)
   if main=="idly" or main=="dosa":
      side=random.choice(chutney)
      op=main+" with "+side
   else:
      op=main
   return op

def afternoon_function():
    main=random.choice(lunch)
    if main=="sambar":
        side=random.choice(sambar_side)
        op=main+" with "+side
    elif main=="rasam":
        side=random.choice(rasam_side)
        op=main+" with "+side
    elif main=="sambar rice"or main=="guruma" or "moor kulambu":
        side=random.choice(fry_side)
        op=main+" with "+side
    elif main=="puli kulambu" or main=="kadalai kulambu":
        side=random.choice(puli_side)
        op=main+" with "+side
    elif main=="curd rice" or main=="lemon rice":
        side=random.choice(lemonrice_side)
        op=main+" with "+side
    elif main=="thakali rice" or main=="vegetable rice":
        side="raita"
        op=main+" with "+side
    elif main=="ghee rice":
        side="guruma"
        op=main+" with "+side
    elif main=="urundai kolambu":
        side="papad"
        op=main+" with "+side
    elif main=="rava upma" or main=="godhumai upma":
        side="coconut chutney"
        op=main+" with "+side
    return op

def night_function():
    main=random.choice(night_menu)
    if main=="idly" or main=="dosa":
      side=random.choice(night_side)
      op=main+" with "+side
    elif main=="panner stuffed chapathi" or main=="adai" or main=="panner stuffed chapathi" or main=="ragi idiyapam":
      op=main
    elif main=="appam" or main=="idiyappam":
      side="coconut milk"
      op=main+" with "+side
    elif main=="chappathi":
        side="kuruma"
        op=main+" with "+side
    
    return op


@csrf_exempt
def handle_button(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        button_type = data.get('button_type')
        if button_type == 'morning':
            result = morning_function()
        elif button_type == 'afternoon':
            result = afternoon_function()
        elif button_type == 'night':
            result = night_function()
        else:
            result = "Invalid button type."
        return JsonResponse({'result': result})
    return JsonResponse({'result': 'Invalid request method.'})

