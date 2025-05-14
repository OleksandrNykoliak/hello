from django.shortcuts import render

def landing(request):
    return render(request, 'about.html')


def new_address(request):
    return render(request, 'new_address.html')


def frame_houses(request):
    return render(request, 'frame_houses.html')


def tiny_house(request):
    return render(request, 'tiny_houses.html')

def contact(request):
    return render(request, 'contact.html')

def our_wood(request):
    return render(request, 'our_wood.html')

def natural_edge_banding(request):
    return render(request, 'natural_edge_banding.html')

def our_mission(request):
    return render(request, 'our_mission.html')

def sliced_veneer(request):
    return render(request, 'sliced_veneer.html')