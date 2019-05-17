#My art piece maker
class Art():

  def __init__(self, artist, title, medium, year):
    self.artist=artist
    self.title=title
    self.medium=medium
    self.year=year

  def __repr__(self):
    return "This piece is by {artist} in {year}. It is called {title} made with {medium}.".format(artist=self.artist, year=self.year, title=self.title, medium=self.medium)

    #the marketplace maker
class Marketplace():

    def __init__(self):
        self.listings=[]

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for i in self.listings:
            print(i)


girl_with_mandolin= Art("Picasso, Pablo", 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910)

veneer= Marketplace()
print(veneer.show_listings())
