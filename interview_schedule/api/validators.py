from rest_framework import serializers


def beginIsBeforeEnd(data):
    if data.begin > data.end:
        raise serializers.ValidationError("begin must be before end.")
    return data


def mustBeAtFullHour(value):
    if value.minute != 0:
        raise serializers.ValidationError("You can only schedule dates to a full hour.")
    return value
