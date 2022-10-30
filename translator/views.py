from django.shortcuts import render

from translator.translate import translate

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        print(original_text)
        output = translate(original_text)
        return render(request,'translator.html',{'output_text':output,'original_text':original_text})
    else:
        return render(request,'translator.html')

    