from rest_framework import serializers


def beginIsBeforeEnd(begin, end):
    if begin > end:
        raise serializers.ValidationError("begin must be before end.")
    return True


def mustBeAtFullHour(value):
    if value.minute != 0:
        raise serializers.ValidationError("You can only schedule dates to a full hour.")
    return value
