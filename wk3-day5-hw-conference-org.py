import requests
from datetime import datetime, timedelta
from operator import itemgetter

data = requests.get("https://ct-mock-tech-assessment.herokuapp.com/").json()



United_States_list = []
United_States_attendee_list = []
Ireland_list = []
Ireland_attendee_list = []
Spain_list = []
Spain_attendee_list = []
Mexico_list = []
Mexico_attendee_list = []
Canada_list = []
Canada_attendee_list = []
Singapore_list = []
Singapore_attendee_list = []
Japan_list = []
Japan_attendee_list = []
United_Kingdom_list = []
United_Kingdom_attendee_list = []
France_list = []
France_attendee_list = []

for num in range(233):
   
    
    if data['partners'][num]['country'] == 'Ireland':
        Ireland_list.append([data['partners'][num]['availableDates']])
        if '2017-05-28' in data['partners'][num]['availableDates'] and '2017-05-29' in data['partners'][num]['availableDates']:
            Ireland_attendee_list.append(data['partners'][num]['email'])
   
    if data['partners'][num]['country'] == 'Spain':
        Spain_list.append([data['partners'][num]['availableDates']])
        if '2017-04-16' in data['partners'][num]['availableDates'] and '2017-04-17' in data['partners'][num]['availableDates']:
            Spain_attendee_list.append(data['partners'][num]['email'])

    if data['partners'][num]['country'] == 'United States':
        United_States_list.append([data['partners'][num]['availableDates']])
        if '2017-05-28' in data['partners'][num]['availableDates'] and '2017-05-29' in data['partners'][num]['availableDates']:
            United_States_attendee_list.append(data['partners'][num]['email'])
   

    if data['partners'][num]['country'] == 'Mexico':
        Mexico_list.append([data['partners'][num]['availableDates']])
        if '2017-04-19' in data['partners'][num]['availableDates'] and '2017-04-20' in data['partners'][num]['availableDates']:
            Mexico_attendee_list.append(data['partners'][num]['email'])
     
    if data['partners'][num]['country'] == 'Canada':
        Canada_list.append([data['partners'][num]['availableDates']])
        if '2017-06-23' in data['partners'][num]['availableDates'] and '2017-06-24' in data['partners'][num]['availableDates']:
            Canada_attendee_list.append(data['partners'][num]['email'])
   
    if data['partners'][num]['country'] == 'Singapore':
        Singapore_list.append([data['partners'][num]['availableDates']])
        if '2017-06-03' in data['partners'][num]['availableDates'] and '2017-06-04' in data['partners'][num]['availableDates']:
            Singapore_attendee_list.append(data['partners'][num]['email'])
    
   
    if data['partners'][num]['country'] == 'Japan':
        # Japan_list.append(data['partners'][num]['email'])
        Japan_list.append([data['partners'][num]['availableDates']])
        if '2017-06-09' in data['partners'][num]['availableDates'] and '2017-06-10' in data['partners'][num]['availableDates']:
            Japan_attendee_list.append(data['partners'][num]['email'])

    if data['partners'][num]['country'] == 'United Kingdom':
        # United_Kingdom_list.append([data['partners'][num]['email']])
        United_Kingdom_list.append([data['partners'][num]['availableDates']])
        if '2017-06-01' in data['partners'][num]['availableDates'] and '2017-06-02' in data['partners'][num]['availableDates']:
            United_Kingdom_attendee_list.append(data['partners'][num]['email'])
   
    if data['partners'][num]['country'] == 'France':
        # France_list.append([data['partners'][num]['email']])
        France_list.append([data['partners'][num]['availableDates']])
        if '2017-06-08' in data['partners'][num]['availableDates'] and '2017-06-09' in data['partners'][num]['availableDates']:
            France_attendee_list.append(data['partners'][num]['email'])

print(f"France Attendee List: {France_attendee_list}, Number of Attendees: {len(France_attendee_list)}")


list_of_countries = []
for num in range(233):
    if data['partners'][num]['country'] not in list_of_countries:
        list_of_countries.append(data['partners'][num]['country'])

France_new_list = []
for each in France_list:
    for date in each:
        France_new_list.append(date)
# print(France_new_list)
United_Kingdom_new_list = []
for each in United_Kingdom_list:
    for date in each:
        United_Kingdom_new_list.append(date)
print(f"United Kingdom new list: {United_Kingdom_new_list}")

Japan_new_list = []
for each in Japan_list:
    for date in each:
        Japan_new_list.append(date)
print(f"Japan new list: {Japan_new_list}")

Singapore_new_list = []
for each in Singapore_list:
    for date in each:
        Singapore_new_list.append(date)
print(f"Singapore new list: {Singapore_new_list}")

Canada_new_list = []
for each in Canada_list:
    for date in each:
        Canada_new_list.append(date)
print(f"Canada new list: {Canada_new_list}")

Mexico_new_list = []
for each in Mexico_list:
    for date in each:
        Mexico_new_list.append(date)
print(f"Mexico new list: {Mexico_new_list}")

United_States_new_list = []
for each in United_States_list:
    for date in each:
        United_States_new_list.append(date)
print(f"United_States new list: {United_States_new_list}")

Spain_new_list = []
for each in Spain_list:
    for date in each:
        Spain_new_list.append(date)
print(f"Spain new list: {Spain_new_list}")

Ireland_new_list = []
for each in Ireland_list:
    for date in each:
        Ireland_new_list.append(date)
print(f"Ireland new list: {Ireland_new_list}")



# France Begin
# Datetime Date Comparison Begins
France_valid_start = []
current_index = 0
for each in France_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            France_valid_start.append(each[idx-1])
   
France_date_counter = {

}

for each in France_valid_start:
    if each not in France_date_counter:
        France_date_counter[each] = 1
    else:
        France_date_counter[each] += 1

print(f"France date counter: {France_date_counter}")

print(f"France Valid Start: {France_valid_start}")

France_valid_start_dates = set(France_valid_start)
print(f"France Valid Start Dates: {France_valid_start_dates}")
# Datetime Date Comparison Ends




France_Dictionary = {
    'attendee count': len(France_attendee_list),
    'attendee emails': France_attendee_list,
    'country': 'France',
    'start date': "2017-06-08"
}

print(f"France Dictionary: {France_Dictionary}")
# # ///////////////////////France End/////////////////////////////

# # # United Kingdom Begin
# # # Datetime Date Comparison Begins
# # print(f"United Kingdom New List: {United_Kingdom_new_list}")
# # print(f"France New List: {France_new_list}")
# # print(f"United Kingdom List: {United_Kingdom_list}")
# # print(f"France List: {France_list}")
United_Kingdom_valid_start = []
current_index = 0

for each in United_Kingdom_new_list:

    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            United_Kingdom_valid_start.append(each[idx-1])

United_Kingdom_date_counter = {

}

for each in United_Kingdom_valid_start:
    if each not in United_Kingdom_date_counter:
        United_Kingdom_date_counter[each] = 1
    else:
        United_Kingdom_date_counter[each] += 1

print(f"United_Kingdom date counter: {United_Kingdom_date_counter}")

print(f"United_Kingdom Valid Start: {United_Kingdom_valid_start}")

United_Kingdom_valid_start_dates = set(United_Kingdom_valid_start)
print(United_Kingdom_valid_start_dates)
# Datetime Date Comparison Ends


United_Kingdom_Dictionary = {
    'attendee count': len(United_Kingdom_attendee_list),
    'attendee emails': United_Kingdom_attendee_list,
    'country': 'United Kingdom',
    'start date': "2017-06-01"
}

print(f"United_Kingdom Dictionary: {United_Kingdom_Dictionary}")
# ////////////////////////////United_Kingdom End ///////////////////////////////

# ////////////////// Japan Begin ///////////////////////
# Datetime Date Comparison Begins
Japan_valid_start = []
current_index = 0
for each in Japan_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Japan_valid_start.append(each[idx-1])
   
Japan_date_counter = {

}

for each in Japan_valid_start:
    if each not in Japan_date_counter:
        Japan_date_counter[each] = 1
    else:
        Japan_date_counter[each] += 1

print(f"Japan date counter: {Japan_date_counter}")

print(f"Japan Valid Start: {Japan_valid_start}")

Japan_valid_start_dates = set(Japan_valid_start)
print(Japan_valid_start_dates)
# Datetime Date Comparison Ends


Japan_Dictionary = {
    'attendee count': len(Japan_attendee_list),
    'attendee emails': Japan_attendee_list,
    'country': 'Japan',
    'start date': "2017-06-09"
}

print(f"Japan Dictionary: {Japan_Dictionary}")
# /////////////////Japan End////////////////////
#  Singapore Begin
# Datetime Date Comparison Begins
Singapore_valid_start = []
current_index = 0
for each in Singapore_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Singapore_valid_start.append(each[idx-1])
   
Singapore_date_counter = {

}

for each in Singapore_valid_start:
    if each not in Singapore_date_counter:
        Singapore_date_counter[each] = 1
    else:
        Singapore_date_counter[each] += 1

print(f"Singapore date counter: {Singapore_date_counter}")

print(f"Singapore Valid Start: {Singapore_valid_start}")

Singapore_valid_start_dates = set(Singapore_valid_start)
print(Singapore_valid_start_dates)
# Datetime Date Comparison Ends




Singapore_Dictionary = {
    'attendee count': len(Singapore_attendee_list),
    'attendee emails': Singapore_attendee_list,
    'country': 'Singapore',
    'start date': "2017-06-03"
}

print(f"Singapore Dictionary: {Singapore_Dictionary}")
# Singapore End

#  Canada Begin
# Datetime Date Comparison Begins
Canada_valid_start = []
current_index = 0
for each in Canada_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Canada_valid_start.append(each[idx-1])
   
Canada_date_counter = {

}

for each in Canada_valid_start:
    if each not in Canada_date_counter:
        Canada_date_counter[each] = 1
    else:
        Canada_date_counter[each] += 1

print(f"Canada date counter: {Canada_date_counter}")

print(f"Canada Valid Start: {Canada_valid_start}")

Canada_valid_start_dates = set(Canada_valid_start)
print(Canada_valid_start_dates)
# Datetime Date Comparison Ends




Canada_Dictionary = {
    'attendee count': len(Canada_attendee_list),
    'attendee emails': Canada_attendee_list,
    'country': 'Canada',
    'start date': "2017-06-23"
}

print(f"Canada Dictionary: {Canada_Dictionary}")
# ///////////////////////////////Canada End//////////////////////////////////////

# ///////////////////////////////Mexico Begin/////////////////////////////////////
# Datetime Date Comparison Begins
Mexico_valid_start = []
current_index = 0
for each in Mexico_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Mexico_valid_start.append(each[idx-1])
   
Mexico_date_counter = {

}

for each in Mexico_valid_start:
    if each not in Mexico_date_counter:
        Mexico_date_counter[each] = 1
    else:
        Mexico_date_counter[each] += 1

print(f"Mexico date counter: {Mexico_date_counter}")

print(f"Mexico Valid Start: {Mexico_valid_start}")

Mexico_valid_start_dates = set(Mexico_valid_start)
print(Mexico_valid_start_dates)
# Datetime Date Comparison Ends


Mexico_Dictionary = {
    'attendee count': len(Mexico_attendee_list),
    'attendee emails': Mexico_attendee_list,
    'country': 'Mexico',
    'start date': "2017-04-19"
}

print(f"Mexico Dictionary: {Mexico_Dictionary}")
# ////////////////////////////Mexico End////////////////////////////////////
#  ///////////////////////////////United States Begin///////////////////////////
# Datetime Date Comparison Begins
United_States_valid_start = []
current_index = 0
for each in United_States_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            United_States_valid_start.append(each[idx-1])
   
United_States_date_counter = {

}

for each in United_States_valid_start:
    if each not in United_States_date_counter:
        United_States_date_counter[each] = 1
    else:
        United_States_date_counter[each] += 1

print(f"United_States date counter: {United_States_date_counter}")

print(f"United_States Valid Start: {United_States_valid_start}")

United_States_valid_start_dates = set(United_States_valid_start)
print(United_States_valid_start_dates)
# Datetime Date Comparison Ends




United_States_Dictionary = {
    'attendee count': len(United_States_attendee_list),
    'attendee emails': United_States_attendee_list,
    'country': 'United_States',
    'start date': "2017-05-28"
}

print(f"United_States Dictionary: {United_States_Dictionary}")
# ////////////////////////////////United_States End//////////////////////////////////////

# ///////////////////////////// Spain Begin////////////////////////////////////////////
# Datetime Date Comparison Begins
Spain_valid_start = []
current_index = 0
for each in Spain_new_list:
    
    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Spain_valid_start.append(each[idx-1])
   
Spain_date_counter = {

}

for each in Spain_valid_start:
    if each not in Spain_date_counter:
        Spain_date_counter[each] = 1
    else:
        Spain_date_counter[each] += 1

print(f"Spain date counter: {Spain_date_counter}")

print(f"Spain Valid Start: {Spain_valid_start}")

Spain_valid_start_dates = set(Spain_valid_start)
print(Spain_valid_start_dates)
# Datetime Date Comparison Ends


Spain_Dictionary = {
    'attendee count': len(Spain_attendee_list),
    'attendee emails': Spain_attendee_list,
    'country': 'Spain',
    'start date': "2017-04-16"
}

print(f"Spain Dictionary: {Spain_Dictionary}")
# # //////////////////////////////# Spain End////////////////////////////////////////

# # /////////////////////////////Ireland Begin////////////////////////////////////////
# # Datetime Date Comparison Begins
Ireland_valid_start = []
current_index = 0
for each in Ireland_new_list:

    for idx in range(1, len(each)):
        current_date = datetime.strptime(each[idx], "%Y-%m-%d")
        previous_date = datetime.strptime(each[idx-1], "%Y-%m-%d")
        # checking for 1 day time difference
        if (current_date-previous_date).days == 1:
            Ireland_valid_start.append(each[idx-1])

Ireland_date_counter = {

}

for each in Ireland_valid_start:
    if each not in Ireland_date_counter:
        Ireland_date_counter[each] = 1
    else:
        Ireland_date_counter[each] += 1

print(f"Ireland date counter: {Ireland_date_counter}")

print(f"Ireland Valid Start: {Ireland_valid_start}")

Ireland_valid_start_dates = set(Ireland_valid_start)
print(Ireland_valid_start_dates)
# Datetime Date Comparison Ends


Ireland_Dictionary = {
    'attendee count': len(Ireland_attendee_list),
    'attendee emails': Ireland_attendee_list,
    'country': 'Ireland',
    'start date': "2017-05-28"
}

print(f"Ireland Dictionary: {Ireland_Dictionary}")
# # ////////////////////////////////////Ireland End///////////////////////////////////////////


data1 = {
    "France Dictionary": France_Dictionary,
    "United Kingdom Dictionary": United_Kingdom_Dictionary,
    "Japan Dictionary": Japan_Dictionary,
    "Singapore Dictionary": Singapore_Dictionary,
    "Canada Dictionary": Canada_Dictionary,
    "Mexico Dictionary": Mexico_Dictionary,
    "United States Dictionary": United_States_Dictionary,
    "Spain Dictionary": Spain_Dictionary,
    "Ireland Dictionary": Ireland_Dictionary,
}
print(data1)


