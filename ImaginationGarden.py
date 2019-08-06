"""In this code I will create conditionals that describe whether or not and/or 
or how my dream garden is themed."""



white_fl_trees = ["Franklinia", "Gordlinia", "Evergreen Magnolia", "Stewartia", "Enkianthus"]
white_fl_tree = "Stewartia"
fav_eastern_shrubs = ["Calycanthus", "Fothergilla"]
fav_eastern_shrub = "Calycanthus"
winter_fragrance = ["Viburnum 'Dawn'", "Winter Daphne", "Sacococca", "Wintersweet", "Saucer Magnolia"]
winter_fragrant = "Viburnum 'Dawn'"
yard_size = .25
old_bathtub = True
mini_conifers = True
ferns = True
fig = True
shade = True


yard_state = "Garden"
if yard_size >= .25:
    if white_fl_tree in white_fl_trees:
        yard_state = "White-flower Structured " + yard_state
    if fav_eastern_shrub in fav_eastern_shrubs:
        yard_state = "Eastern " + yard_state
    if  winter_fragrant in winter_fragrance:
        yard_state = "Winter Fragrance " + yard_state
    if  old_bathtub:
        yard_state = "Carnivorous Bog " + yard_state
    if mini_conifers:
        yard_state = "Gymnosperm " + yard_state
    if ferns:
        yard_state = "Prehistoric " + yard_state
    if  fig:
        yard_state = "Mediterranean " + yard_state
    if shade:
        yard_state = "Shade " + yard_state
    if not(white_fl_tree in white_fl_trees or fav_eastern_shrub in fav_eastern_shrubs \
           or winter_fragrant in winter_fragrance or old_bathtub or mini_conifers \
           or ferns or fig or shade):
        yard_state = "New garden"

print(yard_state)