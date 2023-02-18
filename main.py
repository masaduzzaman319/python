import phonenumbers

from number import numbers

from phonenumbers import geocoder
from phonenumbers import carrier

country = phonenumbers.parse(numbers, "CH")
operater = phonenumbers.parse(numbers, "RO")

print (geocoder.description_for_number(country, "en"))
print (carrier.name_for_number(operater, "en"))