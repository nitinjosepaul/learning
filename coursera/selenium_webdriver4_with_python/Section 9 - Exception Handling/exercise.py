car = {
        'make' : 'maruti',
        'model' : 'swift',
        'year' : 2025
      }


try:
    data = car['color']
except KeyError as e:
    print(F"Attribute {e} is missing")
else:
    print(f"Color is {data}")
finally:
    print("Finished")