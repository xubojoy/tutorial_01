# Author:xubojoy
from rest_framework import serializers
from sinppets.models import Snippet,LANGUANGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUANGE_CHOICES,default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

    def create(self, validated_data):
        '''
        如果数据合法，就创建并返回一个新的Snippet实例
        '''
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        如果数据合法，就更新并返回一个已经存在的Snippet实例 
        '''
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style',instance.style)
        instance.save()
        return instance

    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.id')
        print(owner.source)
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner',)



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id','username','snippets',)
