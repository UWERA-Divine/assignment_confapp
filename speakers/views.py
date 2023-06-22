from django.shortcuts import render
from django.http import HttpResponse

def speaker_list(request):
    data = Speakers.objects.all().values()
    template = loader.get_template('speaker_list.html')

    return HttpResponse (template.render({speakers: data}, request ))

def create_speaker(request):

    return render(request, 'create_speaker.html' )

def read_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    view_item = [speaker for speaker in data if speaker['id'] == speaker_id]

    return render(request, 'read_speaker.html',{'speaker': view_item}) 

def update_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    update_item = [speaker for speaker in data if speaker['id'] == speaker_id]

    return render(request, 'update_speaker.html',{'speaker': update_item })       

def delete_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    delete_item = [item for item in data if item['id'] ==speaker_id ]

    return render(request, 'delete_speaker.html',{'speaker': delete_item })