from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ElonViewSet(ModelViewSet):
    queryset = Elon.objects.all()
    serializer_class = ElonSerializer

class Elon_rasmViewSet(ModelViewSet):
    queryset = Elon_rasm.objects.all()
    serializer_class = Elon_rasmSerializer

class XodimlarViewSet(ModelViewSet):
    queryset = Xodimlar.objects.all()
    serializer_class = XodimlarSerializer

class Xodimga_xabarViewSet(ModelViewSet):
    queryset = Xodimga_xabar.objects.all()
    serializer_class = Xodimga_xabarSerializer

class Reyting_xodimViewSet(ModelViewSet):
    queryset = Reyting_xodim.objects.all()
    serializer_class = Reyting_xodimSerializer

class AxolisiViewSet(ModelViewSet):
    queryset = Axolisi.objects.all()
    serializer_class = AxolisiSerializer

class XududViewSet(ModelViewSet):
    queryset = Xudud.objects.all()
    serializer_class = XududSerializer

class Xudud_rasmViewSet(ModelViewSet):
    queryset = Xudud_rasm.objects.all()
    serializer_class = Xudud_rasmSerializer

 