#Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. Let’s get started!

#list of possible destinations
destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt",]

#list test
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index= destinations.index(destination)
  return destination_index


def get_traveler_location(traveler):
  traveler_destination= test_traveler[1]
  traveler_destination_index= get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index= get_traveler_location(test_traveler)

attractions = [[] for index in destinations]

print(attractions)

def add_attraction(destination, attraction):
    try:
        destination_index= get_destination_index(destination)
    except ValueError:
        return
