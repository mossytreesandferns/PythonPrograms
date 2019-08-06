"""Write a dichotomous key that allows users to determine which of the
Cascadia swallowtail butterflies that they have seen.  Print description
or "species account" of butterfly that user has seen from BUTTERFLIES OF THE
PACIFIC NORTHWEST by William Neill"""

"""TYPE 1 FOR YES AND 2 FOR NO"""


#Pale Swallowtail is the only white Swallowtail


question_one = ('Is the butterfly white?')


#Two-tailed Swallowtail is the only Swallowtail with two points
#on the hindwings


question_two = ('Does the hindwing have two tails?: ')


#Western Tiger Swallowtail is the only swallowtail left on which
#a black dot does not sit on a red mark in the hind wing


question_three = ('Is a black dot superimposed on a red spot?: ')

#The range of the Oregon Swallowtail is limited to the Columbia
#and Snake river basins east into Idaho


question_four = ('Are you seeing the yellow swallowtail in the'
                          'Columbia or Snake river basins?: ')


#Of the remaining two swallowtails, that each have a red mark with a black
#eyespot superimposed, the Anise Swallowtail has a long tail on the hindwing
# and the tail of the Indra Swallowtail is blunted so the hindwing appears
#rounded.


question_five = ('Is the tail on the hindwing of this swallowtail '
                          'rounded/blunted with most of the top-wing black?: ')

if int(input(question_one)) == 1:

    print("""Congratulations, you have seen a Pale Swallowtail
           (Papilio eurymedon). WINGSPAN: 2 7/8 - 3 1/4 inches. 
           DESCRIPTION: The top is creamy white with black vertical stripes 
           and broad black wing borders. The hindwing has a tail, a red 
           spot at the anal angle, and submarginal blue crescents.
           RANGE in PNW: Throughout, except in treeless prairies.
           HABITAT: Forests and mountains. HOST PLANTS: Species
           of Ceanothus, Red Alder (Alnus rubra).""")


# else:
#         print(question_two)

elif int(input(question_two)) == 1:

    print("""Congratulations, you have seen a Two-tailed Swallowtail.
            (Papilio multicaudata) WINGSPAN: 3 3/8 - 3 7/8 inches. 
            DESCRIPTION: The top is yellow with vertical
            stripes and black wing borders.  Each hindwing has two tails, a red
            spot at the anal angle, and submarginal blue crescents. RANGE IN 
            PNW: East of Cascade Crest and in Siskiyou Mountains. HABITATS: 
            Canyons and riversides. HOST PLANTS: Chokecherry(Prunus virginiana).""")
# else:
#     print(question_three)

elif int(input(question_three)) == 2:

    print("""Congratulations, you have seen a Western Tiger Swallowtail.
            (Papilio rutulus) WINGSPAN: 3 1/8 - 3 1/2 inches. DESCRIPTION: 
            The top is yellow with black vertical stripes and black wing borders. 
            The hindwing has a tail,a red spot at the anal angle, 
            and submarginal blue crescents(more prominent in females. 
            RANGE in PNW: Throughout. HABITAT: Forest openings and streamsides.
            HOST PLANTS: Deciduous trees, including Bigleaf Maple(Acer macrophyllum)
            and species of aspen and cottonwood(both Populus) and willow(Salix).""")
# else:
#     print(question_four)

elif int(input(question_four)) == 1:

    print("""Congratulations, you have seen an Oregon Swallowtail(Papilio oregonius).
             a.k.a Baird's Swallowtail, Old World Swallowtail
             WINGSPAN: 2 1/8 - 2 3/8 inches. DESCRIPTION: The top is yellow with black
             outer margins, a black basal area of teh forewing, and black patches
             along the costal margin. The hindwing has a tail, a red spot at the anal 
             angle that contains and eccentric black pupil and submarginal blue 
             crescents.  RANGE IN PNW: Columbia and Snake River basins (east of the
             Dalles) into Idaho. HABITAT: Arid canyons. HOST PLANTS: Tarragon 
             (Artemesia dracunculus).""")
# else:
#     print(question_five)

elif int(input(question_five)) == 1:

    print("""Congratulations, you have seen an Indra Swallowtail (Papilio indra).
            WINGSPAN: 2 1/4 - 2 1/2 inches. DESCRIPTION: The top is black with 
            pale yellow bands and spots. The hindwing has a short tail, a red 
            spot with a central black pupil at the anal angle and submarginal
            blue crescents. RANGE IN PNW: Steens, Siskiyou, and Wallowa 
            mountains and eastern slope of Cascade mountains. HABITAT: Canyons
            and mountain ridges. HOST PLANTS: Species of desert parsley
            (Lomatium), including L. grayi.""")
else:
    print("""Congratulations, you have seen an Anise Swallowtail (Papilio selicaon).
            WINGSPAN: 2 1/2 - 2 3/4 inches. DESCRIPTION: The top is yellow with 
            black outer margins, a black basal area on the forewing, and black patches
            along the costal margin. The hindwing has a tail, a red spot with a centered
            black pupil at the anal angle, and submarginal blue crescents. 
            RANGE IN PNW: Throughout. HABITAT: Many including mountaintops and 
            urban areas. HOST PLANTS: Parsley family, especially Lomatium grayi;
            fennel(Foeniculum) and others.""")




