# dictionaries is ordered collection of data type
# they are store multiple items in a single variable
# dictionaries items are a ky value pairs that sepreted by commas and enclosed within curly brackets {}


dic={
    "rahul":"human being",
    'ashu':'object'
}

print(dic["rahul"])


dic={
    344:'ashu',
    23:'rahul',
    12:'babu'
}

print(dic[23])

# accessing single values

info={'name':'rahul','age':20,'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))


# accessing multiple values

info={'name':'rahul','age':20,'eligible':True}
print(info)
print(info.values())
print(info.keys())

