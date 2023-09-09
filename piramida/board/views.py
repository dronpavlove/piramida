from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.shortcuts import render
from django.conf import settings
from pathlib import Path
# from fpdf import FPDF, HTMLMixin
from datetime import datetime

def board_page(request):
    return render(request, 'board/board.html')
