import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number (with country code): ")
try:
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")
    print("Phone Number:", phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
    print("Timezone:", time[0] if time else "Not found")
    print("Carrier:", car)
    print("Region:", reg)
except phonenumbers.phonenumberutil.NumberParseException as e:
    print("Invalid phone number:", e)
