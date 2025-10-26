# Think of serializers as translators that:
# Convert your Django models into formats that can be sent over the internet (typically JSON)
# Convert incoming data from the internet back into Django model instances
# Validate data to ensure it meets your requirements before saving
# This is particularly important when building APIs, as they need to communicate with
# different types of clients (web browsers, mobile apps, other services) that expect data in standard
# formats like JSON or XML.


from rest_framework import  serializers
from django.utils.html import escape
from .models import Note


# Base serializer for Note a model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

# You're properly inheriting from NoteSerializer
# You're validating both title and content
# You're using strip() to remove whitespace
# You're using escape() for security to prevent XSS attacks
# You're raising proper ValidationError with clear messages

# Check out if the title and content are empty
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Title cannot be empty')
        return escape(value.strip())

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError('Content cannot be empty')
        return escape(value.strip())


class NoteCreateSerializer(NoteSerializer):
    pass

# The validator methods will be called automatically by Django REST Framework when:
# Creating a new note (POST requests)
# Updating an existing note (PUT/PATCH requests)
# These validations will run before the data is saved to the database,
# ensuring data integrity and security.

# Update the NoteSerializer to include the title and content fields
class NoteUpdateSerializer(NoteSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)











