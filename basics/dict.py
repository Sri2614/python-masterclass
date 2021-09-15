# Dictionary - Changeable,unordered collection of unique key value pairs. It is fast because they use hashing, which allows us to access a value quickly

capitals = {'USA': 'Washington DC',
'India':'Delhi', 
'China': 'Beijing',
'Russia': 'Moscow'}

# print(capitals['Germany'])

# print(capitals.get('India'))

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.pop('China')

for key,value in capitals.items():
    print("Keys are: ", key)
    print("Values are: ",value)

