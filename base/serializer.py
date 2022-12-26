from rest_framework import serializers
from .models import *
from asyncore import read

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class AxolisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axolisi
        fields = '__all__'

class Elon_rasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon_rasm
        fields = '__all__'

class ElonSerializer(serializers.ModelSerializer):
    elon_rasm = Elon_rasmSerializer(many=True, read_only=True)
    class Meta:
        model = Elon
        fields = ['id','sarlavha','malumot','sana','elon_rasm']

class Xodimga_xabarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimga_xabar
        fields = '__all__'

class Reyting_xodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reyting_xodim
        fields = '__all__'

class XodimlarSerializer(serializers.ModelSerializer):
    xodim_xabar = Xodimga_xabarSerializer(many=True, read_only=True)
    baholar = Reyting_xodimSerializer(many=True, read_only=True)
    class Meta:
        model = Xodimlar
        fields = ['id','fish','mansabi','tel_raqami','manzili','rasmi','e_mail','ish_joyi_bir','ish_joyi_ikki','lavozim_doirasi','telegram_link','location','yili','baholar','xodim_xabar']

        
class Xudud_rasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xudud_rasm
        fields = '__all__'

class XududSerializer(serializers.ModelSerializer):
    xudud_rasm = Xudud_rasmSerializer(many=True, read_only=True)
    class Meta:
        model = Xudud
        fields = ['id','nomi','raysi','xonadon_soni','axoli_soni','xudud_rasm']

        