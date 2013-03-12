from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from gallery.models import ImageItem
from django.core.urlresolvers import reverse


class ImageCreate(CreateView):
    model = ImageItem


class ImageDetail(DetailView):
    model = ImageItem


class ImageDelete(DeleteView):
    model = ImageItem
    success_url = '/images/'


class ImageList(ListView):
    model = ImageItem
