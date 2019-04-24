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
        attractions_for_destination= attractions[destination_index].append(attraction)
    except ValueError:
        return

add_attraction( 'Los Angeles, USA',['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])



attractions_with_interest=[]

def find_attractions(destination, interests):
    destination_index= get_destination_index(destination)
    attractions_in_city= attractions[destination_index]
    for i in attractions_in_city:
        possible_attraction= i
        attraction_tag= i[1]
        for j in interests:
            if j in attraction_tag:
                attractions_with_interest.append(possible_attraction[0])
                return attractions_with_interest

la_arts=find_attractions("Los Angeles, USA", ['art'])
print('theses are the the attractions with interest '+ str(la_arts))
