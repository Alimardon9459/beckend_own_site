from .views import * 
from django.urls import path , include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chat' , ChatViewSet)
router.register('comment' , CommentViewSet)
router.register('elon' , ElonViewSet)
router.register('elon_rasm' , Elon_rasmViewSet)
router.register('xodimlar' , XodimlarViewSet )
router.register('xodimga_xabar', Xodimga_xabarViewSet)
router.register('reyting_xodim', Reyting_xodimViewSet)
router.register('axolisi', AxolisiViewSet)
router.register('xudud', XududViewSet)
router.register('xudud_rasm', Xudud_rasmViewSet)


urlpatterns = [
   path('',include(router.urls)),
]