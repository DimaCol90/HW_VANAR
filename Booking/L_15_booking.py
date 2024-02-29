import lib

lib.readDestinations()
lib.readPrices()

while lib.running:
    
    lib.renderMenu()
    if lib.option ==1:
       lib.searchDestination() 
    if lib.option ==2:
       lib.renderDestinations()   
    if lib.option ==3:
       lib.renderOrder()      
    if lib.option==4:
       lib.deleteOrder()       
    if lib.option==0:
        lib.running=False   


#HW1 Add option 4 to cancel order        