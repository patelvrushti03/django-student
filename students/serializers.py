from rest_framework import serializers
from students.models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "url",
            "id",
            "name",
            "roll_no",
            "email",
            "course",
            "image",
            "owner",
        ]

    owner = serializers.ReadOnlyField(source="owner.username")
