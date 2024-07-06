from rest_framework import serializers
from ProjectHome.models import webUser
from random import randint
from django.contrib.auth.models import User


class RegistrationwebuserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = webUser,User
        fields = ['email','name','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def random_with_N_digits(self,n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def save(self):
        username = 'U'+ self.validated_data['email']+str(self.random_with_N_digits((len(self.validated_data['email'])%5)+1))
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        if self.validated_data['email'] > 150:
            raise serializers.ValidationError({'Email':'Your email name must be under 150 characters'})            

        if password1 != password2:
            raise serializers.ValidationError({'passsowrd':'Passsword must match.'})

        loguser = User.objects.create_user(username, self.validated_data['email'], password1)
        loguser.save()

        webus = webUser(
            user = loguser,
            Susername = username,
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            password = password1
        )
        webus.save()
        return webus

class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = webUser
        fields = ['email','name','password','password2']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['email','password']
