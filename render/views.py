from django.shortcuts import render
import json, random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Menu options
main_morning = ["idly", "dosa", "poori", "upma", "upma godhumai", "ragi semiya", "vendhaya kanji", "pongal"]
chutney = ["coconut chutney", "tomato chutney", "kothamali chutney", "pulipu chutney", "pudhina chutney"]
night_side = ["mushroom guruma", "coconut chutney", "tomato chutney", "kothamali chutney", "pulipu chutney", "pudhina chutney"]
night_menu = ["idly", "dosa", "idiyappam", "appam", "rava upma", "godhumai upma", "ragi idiyapam", "adai", "chappathi", "panner stuffed chapathi"]
lunch = ["sambar", "rasam", "sambar rice", "kadalai kulambu", "puli kulambu", "guruma", "lemon rice", "curd rice", "vegetable rice", "moor kulambu", "ghee rice", "thakkali rice", "urundai kolambu"]

sambar_side = ["potato fry", "pudalai", "brinjal fry", "carrot fry", "beans fry", "cabbage poriyal", "valaikai fry", "kothavarangai poriyal", "pasalai keerai fry", "murungai keerai fry"]
rasam_side = ["potato fry", "brinjal fry", "cabbage kuttu(yellow color)", "valaikai fry", "simple egg fry", "masala egg", "mushroom fry"]
fry_side = ["potato fry", "brinjal fry", "valaikai fry", "mushroom fry"]
puli_side = ["kothavarangai poriyal", "cabbage poriyal", "carrot and beans poriyal", "keerai", "appalam"]
lemonrice_side = ["potato fry", "brinjal fry", "valaikai fry", "mushroom fry", "vadaga thovayal"]
veg_side = ["raitha"]
ghee_side = ["guruma"]
urundai_side = ["papad"]
upma_side = ["coconut chutney"]

def index(request):
    return render(request, 'indexs.html')

def morning_function():
    main = random.choice(main_morning)
    if main in ["idly", "dosa"]:
        side = random.choice(chutney)
        op = f"{main} with {side}"
    else:
        op = main
    return op

def afternoon_function():
    main = random.choice(lunch)
    if main == "sambar":
        side = random.choice(sambar_side)
        op = f"{main} with {side}"
    elif main == "rasam":
        side = random.choice(rasam_side)
        op = f"{main} with {side}"
    elif main in ["sambar rice", "guruma", "moor kulambu"]:
        side = random.choice(fry_side)
        op = f"{main} with {side}"
    elif main in ["puli kulambu", "kadalai kulambu"]:
        side = random.choice(puli_side)
        op = f"{main} with {side}"
    elif main in ["curd rice", "lemon rice"]:
        side = random.choice(lemonrice_side)
        op = f"{main} with {side}"
    elif main in ["thakkali rice", "vegetable rice"]:
        side = random.choice(veg_side)
        op = f"{main} with {side}"
    elif main == "ghee rice":
        side = random.choice(ghee_side)
        op = f"{main} with {side}"
    elif main == "urundai kolambu":
        side = random.choice(urundai_side)
        op = f"{main} with {side}"
    else:
        op = main
    return op

def night_function():
    main = random.choice(night_menu)
    if main in ["idly", "dosa"]:
        side = random.choice(night_side)
        op = f"{main} with {side}"
    elif main in ["panner stuffed chapathi", "adai", "ragi idiyapam"]:
        op = main
    elif main in ["appam", "idiyappam"]:
        side = "coconut milk"
        op = f"{main} with {side}"
    elif main == "chappathi":
        side = "kuruma"
        op = f"{main} with {side}"
    elif main in ["rava upma", "godhumai upma"]:
        side = random.choice(upma_side)
        op = f"{main} with {side}"
    else:
        op = main
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
