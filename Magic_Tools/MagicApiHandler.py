from mtgsdk import Card as MTGCard
from mtgsdk import Set as MTGSet
from mtgsdk import Type as MTGType
from mtgsdk import Supertype as MTGSupertype
from mtgsdk import Subtype as MTGSubtype
import Objects

Rarities = ['Common','Uncommon','Rare','Mythic']

def GetAllSets():
    mtgsets = MTGSet.all()
    sets = []

    for mtgset in mtgsets:
        sett = Objects.Set(mtgset.code,mtgset.name)
        sets.append(sett)

    return sets

def GetAllCardsInSet(setCode):
    mtgcards = []
    cards = []

    for rarity in Rarities:
        mtgcards.extend(MTGCard.where(set=setCode).where(rarity=rarity).all())

    for mtgcard in mtgcards:
        card = Objects.Card(0,mtgcard.cmc,mtgcard.colors,mtgcard.image_url,mtgcard.mana_cost
                    ,mtgcard.name,mtgcard.number,mtgcard.power,mtgcard.rarity,mtgcard.set
                    ,mtgcard.subtypes,mtgcard.text,mtgcard.toughness,mtgcard.types)
        cards.append(card)

    SortCards(cards)

    return cards

def GetAllTypes():
    mtgtypes = MTGType.all()
    types = []

    for mtgtype in mtgtypes:
        typee = Objects.Type(0,mtgtype)
        types.append(typee)

    return types

def GetAllSupertypes():
    mtgsupers = MTGSupertype.all()
    supers = []

    for mtgsuper in mtgsupers:
        supertype = Objects.Supertype(0,mtgsuper)
        supers.append(supertype)

    return supers

def GetAllSubtypes():
    mtgsubs = MTGSubtype.all()
    subs = []

    for mtgsub in mtgsubs:
        sub = Objects.Subtype(0,mtgsub)
        subs.append(sub)

    return subs

def SortCards(cards):
    high = len(cards)-1
    return quickSort(cards,0,high)

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#card = MTGCard.where(legality='Legal').where(format='Historic').all()

#card = MTGCard.find(479688)
card = MTGCard.where(name='Mythos of Brokkos').all()

print('')
