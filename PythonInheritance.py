class Cell:
    def __init__(self):
        self.cell_attribute = "I am life"

    def metabolism(self):
        print("respiration")

    def replication(self):
        print("replication") 

    def growth(self):
        print("growth")     

    def membrane(self):
        print("membrane allow electrical and other gradients") 

class Archaea(Cell):
    def __init__(self):
        Cell.__init__(self)
        self.arch_attribute = "I was around before oxygen"
        
    def arch_traits(self):
        print("extremophiles", "obligate anaerobes","methanogens","non-pathogenic","ether-containing membranes")

class Bacteria(Cell):
    def __init__(self):
        self.bacteria_attribute = "I flourished after oxygen"

    def bact_traits(self):
        print("sometimes pathogenic", "ester-containing membranes","sometimes anaerobic")
    

class Eukarya(Cell):
    def __init__(self):
        self.euk_attribute = "I introduce complexity"

    def euk_traits(self):
        print("membrane-bound-organelles","large","nucleus/nuclear membrane","dna wound into chromosomes","cytoskeleton")
                   

class Algae(Cell, Eukarya):
    def alg_traits(self):
        print("autotrophic","light harvesting pigments","asexual and sexual reproduction","obvious alternation of generations")

class Moss(Cell, Algae):
    def moss_traits(self):
        print("upright growth", "land-adapted")

class Fern(Cell, Moss):
    def fern_traits(self):
        print("ligning-upright growth", "roots","cell walls", "vascular system","sporophyte dominant","diploid")    

class Conifer(Cell, Fern):
    def conifer_traits(self):
        print("wood", "seeds")

class Flowering(Cell, Conifer):
    def flowering_traits(self):
        print("ovaries","flowers","insect coevolution")

class Fungi(Cell):
    def fungi_traits(self):
        print("nutrition through absorption", "diploid","cell walls")

class Animal(Cell):
    def animal_traits(self):
        print("Boring unless an insect, amphibian, bat, owl, or pet cat.")    


cell = Cell()
arch = Archaea()
bac = Bacteria()
euk = Eukarya()
algae = Algae()
moss = Moss()
fern = Fern()
conifer = Conifer()
flower = Flowering()
fungi = Fungi()
animal = Animal()

#methods and attributes can be printed
cell.metabolism()

arch.arch_traits()
arch.replication()
print(arch.cell_attribute)

bac.bact_traits()
bac.growth()

euk.euk_traits()
euk.growth()

algae.alg_traits()
algae.membrane()

moss.moss_traits()
moss.alg_traits()

fern.fern_traits()
fern.moss_traits()

conifer.conifer_traits()
conifer.fern_traits()

flower.flowering_traits()
flower.conifer_traits()

animal.animal_traits()

