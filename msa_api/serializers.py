from rest_framework import serializers

from msa_api.models.advisor import Advisor
from msa_api.models.alumany import Alumanai
from msa_api.models.banner import Banner
from msa_api.models.executive import ExecutiveCommittee
from msa_api.models.gellary import Gallery
from msa_api.models.history import History
from msa_api.models.overview import Overview
from msa_api.models.speech import Speech
from msa_api.models.updateAndnotice import UpdateAndNotice
from msa_api.models.events import Event
from msa_api.models.mission import Mission
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model."""

    password = serializers.CharField(write_only=True)  # Password won't be returned in the response

    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'name', 'password', 'is_staff', 'is_superuser', 'is_active', 'date_time_of_creation'
        ]
        read_only_fields = ['id', 'date_time_of_creation', 'is_superuser']

    def create(self, validated_data):
        """Create and return a new user with hashed password."""
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update a user, set the password correctly, and return the user."""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password', 'is_staff']
        extra_kwargs = {
            'is_staff': {'required': False, 'read_only': True},
        }

    def create(self, validated_data):
        """Create a new user with hashed password."""
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        """Validate and authenticate user."""
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        data['user'] = user
        return data 
    
class ExecutiveCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveCommittee
        fields = '__all__'


class UpdateAndNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateAndNotice
        fields = ['id', 'title', 'file', 'date']



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'date']



class AlumanaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumanai
        fields = '__all__'



class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'



class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'



class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'
