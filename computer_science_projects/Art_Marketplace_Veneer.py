#My art piece maker
class Art():

  def __init__(self, artist, title, medium, year,owner):
    self.artist= artist
    self.title= title
    self.medium= medium
    self.year= year
    self.owner= owner

  def __repr__(self):
    return "This piece is by {artist} in {year}. It is called {title} made with {medium}. The owner is {owner}, {location}.".format(artist=self.artist, year=self.year, title=self.title, medium=self.medium, owner=self.owner.name, location=self.owner.location)

    #the marketplace maker
class Marketplace():

    def __init__(self):
        self.listings=[]

    #this function adds a listing to the marketplace
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    #this function removes a listing
    def remove_listing(self, listing):
        self.listings.remove(listing)

    #this function shows the listing
    def show_listings(self):
        for i in self.listings:
            print(i)

# this class creates client information for the marketplace
class Client():
    def __init__(self, name, location, is_museum):
        self.name=name
        self.location=location
        if self.location=='Private Collector':
            self.is_museum=False
        else:
            self.is_musem=True

    def sell_artwork(self, artwork, price):
        if (artwork.owner==self):
            veneer.add_listing(listing(artwork, price, self.name))

    def buy_artwork(self, artwork):
        if (artwork.owner != self):
            art_listing= None
            for listing in veneer.listings:
                if artwork==listing.art:
                    art_listing=listing
                    break

        if (art_listing != None):
            art_listing.art.owner=self
            veneer.remove_listing(art_listing)


        else:
            
            return 'You already own this piece'

# this class creates listing for the marketplace
class listing():
    def __init__(self, art, price, seller):
        self.art=art
        self.price=price
        self.seller=seller
    
    def __repr__ (self):
        return 'This piece is {art} for {price}, sold by {seller}.'.format(art=self.art, price=self.price, seller=self.seller)
edytta= Client('Edytta', 'Private Collector', False)

moma= Client('The MOMA', 'New York', True)
        


girl_with_mandolin= Art("Picasso, Pablo", 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)


veneer= Marketplace()
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
print(girl_with_mandolin)
print(veneer.show_listings())
moma.buy_artwork(girl_with_mandolin)
print(veneer.show_listings())
print(girl_with_mandolin)


