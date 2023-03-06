# dictionary = A collection of unique key:value pair. It is unordered and mutable (changeable).
#               This is fast because it uses hashing technique to access the values.

rajdhani = {'Bharat': 'Nayi Dilli',
            'Jharkhand': 'Ramgarh',
            'Bihar': 'Patna',
            'Odisha': 'Bhubaneswar',
            'Paschim Bangal': 'Kolkata',
            'Chhattisgarh': 'Raipur',
            'Uttar Pradesh': 'Lucknow'}

print("Jharkhand ki Rajhdhani: " + rajdhani['Jharkhand'])
rajdhani.update({'Jharkhand': 'Ranchi'})

print(rajdhani.get('Maharashtra'))
rajdhani.update({'Maharashtra': 'Mumbai'})
print("Maharashtra ki Rajdhani: " + rajdhani['Maharashtra'])

rajdhani.update({'Pakistan': 'Lahor'})
print(rajdhani.keys())
print(rajdhani.values())
print(rajdhani.items())

rajdhani.pop('Pakistan')
for key, value in rajdhani.items():
    print(key + " ki Rajdhani: " + value)
