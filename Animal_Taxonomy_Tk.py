from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x500")
root.title("Animal Taxonomy")
root.maxsize(width = "800", height = "500")
root.iconbitmap(r"icon/favicon1.ico")

def on_enter(e):
    e.widget['background'] = 'deepskyblue3'

def on_leave(e):
    e.widget['background'] = 'darkgrey'

def on_enter(e):
    search_btn['background'] = 'deepskyblue3'

def on_leave(e):
    search_btn['background'] = 'dodgerblue3'



def home_page():
    home_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(home_frame, text = "HOME",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(home_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search_name_btn = tk.Radiobutton(home_frame, text = "NAME", bg = "darkgrey", activebackground = "darkgrey",
                                       activeforeground = "dodgerblue3", value = "NAME")
    search_name_btn.place(x = "4", y = "100")

    search_kingdom_btn = tk.Radiobutton(home_frame, text = "KINGDOM", bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "KINGDOM")
    search_kingdom_btn.place(x = "71", y = "100")

    search_phylum_btn = tk.Radiobutton(home_frame, text = "Phylum", bg = "darkgrey", activebackground = "darkgrey",
                                         activeforeground = "dodgerblue3", value = "Phylum")
    search_phylum_btn.place(x = "159", y = "100")

    search_class_btn = tk.Radiobutton(home_frame, text = "CLASS", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "CLASS")
    search_class_btn.place(x = "233", y = "100")

    search_order_btn = tk.Radiobutton(home_frame, text = "ORDER", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "ORDER")
    search_order_btn.place(x = "300", y = "100")

    search_family_btn = tk.Radiobutton(home_frame, text = "FAMILY", bg = "darkgrey", activebackground = "darkgrey",
                                         activeforeground = "dodgerblue3", value = "FAMILY")
    search_family_btn.place(x = "370", y = "100")

    search_genus_btn = tk.Radiobutton(home_frame, text = "Genus", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "Genus")
    search_genus_btn.place(x = "444", y = "100")

    search_species_btn = tk.Radiobutton(home_frame, text = "SPECIES", bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "SPECIES")
    search_species_btn.place(x = "510", y = "100")

    search = tk.Entry(home_frame, width = "30", bg = "aliceblue", fg = "dodgerblue3")
    search.place(x = "1", y = "135")
    contents = tk.StringVar()
    contents.set("Search according to your option.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(home_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "132")

    home_frame.pack(padx = 20, pady = 20)
    home_frame.configure(width = "650", height = "500")

def kingdom_page():
    kingdom_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(kingdom_frame, text = "KINGDOM",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(kingdom_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search_animal_btn = tk.Radiobutton(kingdom_frame, text = "ANIMALS", bg = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "ANIMALS")
    search_animal_btn.place(x = "3", y = "98")

    search_plant_btn = tk.Radiobutton(kingdom_frame, text = "PLANT", bg = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "PLANT")
    search_plant_btn.place(x = "78", y = "98")

    search_fungi_btn = tk.Radiobutton(kingdom_frame, text = "FUNGI", bg = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "FUNGI")
    search_fungi_btn.place(x = "138", y = "98")

    search_protista_btn = tk.Radiobutton(kingdom_frame, text = "PROTISTA", bg = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "PROTISTA")
    search_protista_btn.place(x = "196", y = "98")

    search_monera_btn = tk.Radiobutton(kingdom_frame, text = "MONERA", bg = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "MONERA")
    search_monera_btn.place(x = "271", y = "98")

    search = tk.Entry(kingdom_frame, width = "30", bg = "aliceblue", fg = "dodgerblue3")
    search.place(x = "1", y = "135")
    contents = tk.StringVar()
    contents.set("Type The Kingdom.")
    search["textvariable"] = contents


    global search_btn
    search_btn = tk.Button(kingdom_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "132")


    kingdom_frame.pack(padx = 20, pady = 20)
    kingdom_frame.configure(width = "650", height = "500")

def phylum_page():
    phylum_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(phylum_frame, text = "PHYLUM",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(phylum_frame , text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")


    search_chordate_btn = tk.Radiobutton(phylum_frame, text = "CHORDATE", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "CHORDATE")
    search_chordate_btn.place(x = "4", y = "100")

    search_arthropod_btn = tk.Radiobutton(phylum_frame, text = "ARTHROPOD", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "ARTHROPOD")
    search_arthropod_btn.place(x = "93", y = "100")

    search_molusc_btn = tk.Radiobutton(phylum_frame, text = "MOLUSC", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "MOLUSC")
    search_molusc_btn.place(x = "193", y = "100")

    search_echinoderm_btn = tk.Radiobutton(phylum_frame, text = "ECHINODERM", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "ECHINODERM")
    search_echinoderm_btn.place(x = "270", y = "100")

    search_annalid_btn = tk.Radiobutton(phylum_frame, text = "ANNALID", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "ANNALID")
    search_annalid_btn.place(x = "369", y = "100")

    search_sponge_btn = tk.Radiobutton(phylum_frame, text = "SPONGE", bg = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "SPONGE")
    search_sponge_btn.place(x = "448", y = "100")

    search = tk.Entry(phylum_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "135")
    contents = tk.StringVar()
    contents.set("Type The Phylum.!")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(phylum_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "132")

    phylum_frame.pack(padx = 20, pady = 20)
    phylum_frame.configure(width = "650", height = "500")

def class_page():
    class_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(class_frame, text = "CLASS",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(class_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search_mammallia_btn = tk.Radiobutton(class_frame, text = "MAMMALIA", bg = "darkgrey",
                                            activeforeground = "dodgerblue3", value = "MAMMALLIA")
    search_mammallia_btn.place(x = "4", y = "100")

    search_maxillopoda_btn = tk.Radiobutton(class_frame, text = "MAXILLOPODA", bg = "darkgrey",
                                            activeforeground = "dodgerblue3", value = "MAXILLOPODA")
    search_maxillopoda_btn.place(x = "85", y = "100")

    search_souropsida_btn = tk.Radiobutton(class_frame, text = "SOUROPSIDA", bg = "darkgrey",
                                            activeforeground = "dodgerblue3", value = "SOUROPSIDA")
    search_souropsida_btn.place(x = "190", y = "100")

    search_diplopoda_btn = tk.Radiobutton(class_frame, text = "DIPLOPODA", bg = "darkgrey",
                                            activeforeground = "dodgerblue3", value = "DIPLOPODA")
    search_diplopoda_btn.place(x = "285", y = "100")


    search = tk.Entry(class_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "135")
    contents = tk.StringVar()
    contents.set("Type The Class.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(class_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "132")

    class_frame.pack(padx = 20, pady = 20)
    class_frame.configure(width = "650", height = "500")

def order_page():
    order_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(order_frame, text = "ORDER",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(order_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    def show(): 
        search.config( contents.set( clicked.get()) ) 

    clicked = StringVar() 
    
    clicked.set( "Monday" ) 
    options = [ 
    "Rodentia", 
    "Chiroptera", 
    "Afrosoricida", 
    "Eriaceomorph", 
    "Primates"
    ] 
    
    search_kingdom_menu = OptionMenu( order_frame , clicked , *options)# back = "dodgerblue3",) 
    search_kingdom_menu.place(x = "1", y= "100") 

    search = tk.Entry(order_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "135")
    contents = tk.StringVar()
    contents.set("Type The Order.")    
    contents = tk.StringVar()
    contents.set(clicked.get() )
    search["textvariable"] = contents
 
    global search_btn
    search_btn = tk.Button(order_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3", command = show )
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)

    search_btn.place(x = "191", y = "132")

    order_frame.pack(padx = 20, pady = 20)
    order_frame.configure(width = "650", height = "500")

def family_page():
    family_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(family_frame, text = "FAMILY",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    search = tk.Entry(family_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "100")
    contents = tk.StringVar()
    contents.set("Type The Family.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(family_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "98")

    family_frame.pack(padx = 20, pady = 20)
    family_frame.configure(width = "650", height = "500")

def genus_page():
    genus_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(genus_frame, text = "GENUS",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    search = tk.Entry(genus_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "100")
    contents = tk.StringVar()
    contents.set("Type The Genus.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(genus_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "98")

    genus_frame.pack(padx = 20, pady = 20)
    genus_frame.configure(width = "650", height = "500")

def species_page():
    species_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(species_frame, text = "SPEICES",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    search = tk.Entry(species_frame, width = "30", bg = "darkgrey", fg = "dodgerblue3")
    search.place(x = "1", y = "100")
    contents = tk.StringVar()
    contents.set("Type The Species.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(species_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "98")

    species_frame.pack(padx = 20, pady = 20)
    species_frame.configure(width = "650", height = "500")

def about_page():
    about_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(about_frame, text = "ABOUT",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    
    label = tk.Label(about_frame, text = "We are a group of students studying in XI std,\n\
<--CREDITS-->\n\
Ideaology --> Hari Dhejus V.S.\n\
Cheif Devoloper --> Hari Dhejus V.S.\n\
Co-Devoloper --> Anandha Krishnan\n\
Chief Biologist --> Pranav Krishna Prathap\n\
Co-Biologist-1-->Adharsh S.M.\n\
Co-Biologist2-->Akshay Ram R.F\n\
\n\
Contact us --> +91 948 668 3398\n\
\n\
        Thank you for using this program © AnimalTaxonaomy ™HAPAA", 
                        font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "0", y = "100")

    about_frame.pack(padx = 20, pady = 20)
    about_frame.configure(width = "650", height = "500")

#=-=-=-=-=-=-=-EXTRA-=-=-=-=-=-=-=#

def hide_indicator():
    home_indicate.config(bg = "darkgray")
    kingdom_indicate.config(bg = "darkgray")
    phylum_indicate.config(bg = "darkgray")
    class_indicate.config(bg = "darkgray")
    order_indicate.config(bg = "darkgray")
    family_indicate.config(bg = "darkgray")
    genus_indicate.config(bg = "darkgray")
    species_indicate.config(bg = "darkgray")
    about_indicate.config(bg = "darkgray")

def indicate(lb, page):
    hide_indicator()
    lb.config(bg = "dodgerblue3")
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

option_frame = tk.Frame(root, bg = "darkgray")

home_btn = tk.Button(option_frame, text = "Home", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3",
                     bd = 0, bg = "darkgray",  activebackground = "darkgray",
                    command = lambda: indicate(home_indicate, home_page))
home_btn.place(x = 15, y = 25)

home_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
home_indicate.place(x = 10, y = 25, width = 2, height = 60)

kingdom_btn = tk.Button(option_frame, text = "Kingdom", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3", 
                        bd = 0, bg = "darkgray", activebackground = "darkgray",
                        command = lambda: indicate(kingdom_indicate, kingdom_page))
kingdom_btn.place(x = 15, y = 75)

kingdom_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
kingdom_indicate.place(x = 10, y = 75, width = 2, height = 60)

phylum_btn = tk.Button(option_frame, text = "Phylum", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3",
                     bd = 0, bg = "darkgray",  activebackground = "darkgray",
                    command = lambda: indicate(phylum_indicate, phylum_page))
phylum_btn.place(x = 15, y = 125)

phylum_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
phylum_indicate.place(x = 10, y = 125, width = 2, height = 60)

class_btn = tk.Button(option_frame, text = "Class", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3", 
                        bd = 0, bg = "darkgray", activebackground = "darkgray",
                        command = lambda: indicate(class_indicate, class_page))
class_btn.place(x = 15, y = 175)

class_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
class_indicate.place(x = 10, y = 175, width = 2, height = 60)

order_btn = tk.Button(option_frame, text = "Order", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3",
                     bd = 0, bg = "darkgray",  activebackground = "darkgray",
                    command = lambda: indicate(order_indicate, order_page))
order_btn.place(x = 15, y = 225)

order_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
order_indicate.place(x = 10, y = 225, width = 2, height = 60)

family_btn = tk.Button(option_frame, text = "Family", font = ("Bradley Hand ITC" , 20, "italic", "bold" ), fg = "dodgerblue3", 
                        bd = 0, bg = "darkgray", activebackground = "darkgray",
                        command = lambda: indicate(family_indicate, family_page))
family_btn.place(x = 15, y = 275)

family_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
family_indicate.place(x = 10, y = 275, width = 2, height = 60)

genus_btn = tk.Button(option_frame, text = "Genus", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),
                       fg = "dodgerblue3",bd = 0, bg = "darkgray",  activebackground = "darkgray",
                    command = lambda: indicate(genus_indicate, genus_page))
genus_btn.place(x = 15, y = 325)

genus_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
genus_indicate.place(x = 10, y = 325, width = 2, height = 60)

species_btn = tk.Button(option_frame, text = "Species", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),
                         fg = "dodgerblue3", bd = 0, bg = "darkgray", activebackground = "darkgray",
                        command = lambda: indicate(species_indicate, species_page))
species_btn.place(x = 15, y = 375)

species_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
species_indicate.place(x = 10, y = 375, width = 2, height = 60)


about_btn = tk.Button(option_frame, text = "About", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),
                       fg = "dodgerblue3", bd = 0, bg = "darkgray", activebackground = "darkgray",
                        command = lambda: indicate(about_indicate, about_page))
about_btn.place(x = 15, y = 425)

about_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
about_indicate.place(x = 10, y = 425, width = 2, height = 60)

option_frame.pack(side = "left")
option_frame.pack_propagate(False)
option_frame.configure(width = "150", height = "500")

main_frame = tk.Frame(root, highlightbackground= "dodgerblue3",  highlightthickness= "5", bg = "darkgrey")
main_frame.pack(side = "left")
main_frame.pack_propagate(False)
main_frame.configure(width = "650", height = "500")

root.mainloop()