import sqlite3
import os

#----------------------------------------

con = sqlite3.connect("Animal_Taxonomy_DB.db")
cur = con.cursor()

#----------------------------------------


#cur.execute("DROP TABLE animal_details")
#cur.execute("CREATE TABLE animal_details(name, kingdom, phylum, class, naturalorder, family, genus, species)")

#----------------------------------------

while True :
    """cur.execute(
                        INSERT INTO animal_details VALUES

                        ("Human:", "Animalia:", "Chordata:", "Mamamalia:", "Primates:", "Hominidae:", "Home:", "Sapiens"),                        
                        ("Dog:", "Animalia:", "Chordata:", "Mamamalia:", "Carnivora:", "Canidae:", "Canis:", "Familaris"),
                        ("Rat:", "Animalia:", "Chordata:", "Mamamalia:", "Rodentia::", "Muridea:", "Rattus:", "Notvegicus"),
                        ("Rabbit:", "Animalia:", "Chordata:", "Mamamalia:", "Lagomorpha:", "Lpordae:", "Oryctolagus:", "Cuniculus"),
                        ("Leopord:", "Animalia:", "Chordata:", "Mamamalia:", "Carnivora:", "Felidae:", "Panthera:", "Paradus"),
                        ("Red Fox:", "Animalia:", "Chordata:", "Mamamalia:", "Carnivora:", "Canidae:", "Vulpes:", "Vulpes"),
                        ("Gorilla:", "Animalia:", "Chordata:", "Mamamalia:", "Primates:", "Hominidae:", "Gorilla:", "Gorlla"),
                        ("Capybara:", "Animalia:", "Chordata:", "Mamamalia:", "Rodentia:", "Caviidae:", "Hydrochoerus:", "Hydrochaeris"),
                        ("Wolf:", "Animalia:", "Chordata:", "Mamamalia:", "Carnivora:", "Canidae:", "Canis:", "Lupus"),
                        ("Lion:", "Animalia:", "Chordata:", "Mamamalia:", "Carnivora:", "Felidae:", "Panthera:", "Leo"),
                        ("Cockroach:", "Animalia:", "Arthropoda:", "Insecta:", "Orthoptera:", "Blattidae:", "Periplanta:", "Americana"),
                        ("Stag Beetle:", "Animalia:", "Arthropoda:", "Insecta:", "Coleoptera:", "Lucanide:", "Lucanus:", "Cervus"),
                        ("Boa Constrictor:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Boidea:", "Boa:", "Constrictor") ,
                        ("Spitting Cobra:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Elapidae:", "Naja:", "Pallida"),
                        ("Horned Viper:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Viperidae:", "Vipera:", "Ammodytes"),
                        ("Scarlet Snake:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Columbridae:", "Cemophora:", "Coccinae"),
                        ("Eastern Diamondback Rattlesnake:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Viperidae:", "Crotalus:", "Adamanteus"),
                        ("Timber Rattlesnake:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Viperidae:", "Crotalus:", "Horridus"),
                        ("Indian Python:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Pythonidae:", "Python:", "Molurus"),
                        ("Banded Water Snake:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Columbridae:", "Helicops:", "Angulatus"),
                        ("Mandalay Spitting Cobra:", "Animalia:", "Chordata:", "Reptila:", "Squamata:", "Elapidae:", "Naja:", "Mandalayensis")


                        
    )   
    con.commit()   """

#----------------------------------------

    tosearchby = input("By what classification do you want to search by ? \n\
Hit 'Enter' for name of the animal\n\
Enter 1 for name of the animal\n\
Enter 2 for name of the animal\n\
Enter 3 for name of the animal\n\
Enter 4 for name of the animal\n\
Enter 5 for name of the animal\n\
Enter 6 for name of the animal\n\
Enter 7 for name of the animal :")

#----------------------------------------

    if tosearchby == '':
        tosearch = input("Enter the name of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE name = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '1':
        tosearch = input("Enter the kingdom of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE kingdom = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '2':
        tosearch = input("Enter the phylum of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE phylum = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '3':
        tosearch = input("Enter the class of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE class = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '4':
        tosearch = input("Enter the order of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE naturalorder = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '5':
        tosearch = input("Enter the family of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE family = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '6':
        tosearch = input("Enter the genus of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE genus = '"+tosearch+"' "):
            print(row)

#----------------------------------------

    elif tosearchby == '7':
        tosearch = input("Enter the species of the organisim :")
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE species = '"+tosearch+"' "):
            print(row)
        
    decision = input("Do you want to search again? Hit 'Enter' to search again Enter any other to quit. : ")
    if decision =='':
        continue
    else:
        print("""
                                                <--CREDITS-->
                                                Ideaology --> Hari Dhejus V.S.
                                                Cheif Devoloper --> Hari Dhejus V.S.
                                                Co-Devoloper --> Anandha Krishnan
                                                Chief Biologist --> Pranav Krishna Prathap
                                                Co-Biologist-1-->Adharsh S.M.
                                                Co-Biologist2-->Akshay Ram R.F
                                                
                                                Contact us --> +91 948 668 3398

                                    Thank you for using this program © AnimalTaxonaomy ™HAPAA
            """)
        break

con.close()
