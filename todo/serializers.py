from rest_framework import serializers
from todo.models import Todo
 
 
class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description',
                  'status', 'updated')


    #Todo Serializer.
 
    #Used to serialize the Todo model to JSON. The fields to be 
    #serialized are:
    #- id
    #- title
    #- description
    #- status
    #- updated