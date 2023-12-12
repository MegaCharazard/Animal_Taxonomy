from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.geometry("800x500")
root.title("Animal Taxonomy")
root.maxsize(width = "800", height = "500")
root.iconbitmap(r"icon/favicon1.ico")

con = sqlite3.connect("Animal_Taxonomy_DB.db")
cur = con.cursor()

option_chosen = ""

#It is executed when dropdown is changed
def drop_down_index_changed(event) :
    global option_chosen
    option_chosen = event

def on_enter_global(e):
    e.widget['background'] = 'deepskyblue3'

def on_leave_global(e):
    e.widget['background'] = 'dodgerblue3'

def on_enter(e):
    search_btn['background'] = 'deepskyblue3'

def on_leave(e):
    search_btn['background'] = 'dodgerblue3'

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=PAGES=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#global buildFrame()
def buildFrame(frame, highlightbackground, highlightthickness, bg = "dodgerblue3"):
    return tk.Frame(frame, highlightbackground = highlightbackground,  highlightthickness= highlightthickness, bg = bg)

def home_page():
    #global search_result_ypos 
    #search_result_ypos = 160
    #home_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")
    home_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(home_frame, text = "HOME",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(home_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    global radio_value
    def radio_value(value_before):
        if value_before == "":
            label = tk.Label(home_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              bg = "darkgrey", fg = "red")
            label.place(x = "1", y = "470")
        else:
            global home_value
            home_value = value_before
            #print(value)


    search_name_btn = tk.Radiobutton(home_frame, text = "NAME", bg = "darkgrey", activebackground = "darkgrey",
                                       activeforeground = "dodgerblue3", value = "NAME", command = lambda:(radio_value("name")))
    search_name_btn.place(x = "4", y = "100")

    search_kingdom_btn = tk.Radiobutton(home_frame, text = "KINGDOM", bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "KINGDOM", command = lambda:(radio_value("kingdom")))
    search_kingdom_btn.place(x = "71", y = "100")

    search_phylum_btn = tk.Radiobutton(home_frame, text = "Phylum", bg = "darkgrey", activebackground = "darkgrey",
                                         activeforeground = "dodgerblue3", value = "Phylum", command = lambda:(radio_value("phylum")))
    search_phylum_btn.place(x = "159", y = "100")

    search_class_btn = tk.Radiobutton(home_frame, text = "CLASS", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "CLASS", command = lambda:(radio_value("class")))
    search_class_btn.place(x = "233", y = "100")

    search_order_btn = tk.Radiobutton(home_frame, text = "ORDER", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "ORDER", command = lambda:(radio_value("naturalorder")))
    search_order_btn.place(x = "300", y = "100")

    search_family_btn = tk.Radiobutton(home_frame, text = "FAMILY", bg = "darkgrey", activebackground = "darkgrey",
                                         activeforeground = "dodgerblue3", value = "FAMILY", command = lambda:(radio_value("family")))
    search_family_btn.place(x = "370", y = "100")

    search_genus_btn = tk.Radiobutton(home_frame, text = "Genus", bg = "darkgrey", activebackground = "darkgrey",
                                        activeforeground = "dodgerblue3", value = "Genus", command = lambda:(radio_value("genus")))
    search_genus_btn.place(x = "444", y = "100")

    search_species_btn = tk.Radiobutton(home_frame, text = "SPECIES", bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "SPECIES", command = lambda:(radio_value("species")))
    search_species_btn.place(x = "510", y = "100")

    search = tk.Entry(home_frame, width = "30", bg = "aliceblue", fg = "dodgerblue3")
    search.place(x = "1", y = 130)
    global contents
    contents = tk.StringVar()
    contents.set("Search according to your option.")
    search["textvariable"] = contents

    result_frame = buildFrame(home_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 165)
    result_frame.configure(width = 570, height = 265)

    def on_home_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            tosearch = tosearch

        if home_value == "name":
            for label in result_frame.winfo_children():
                label.destroy()
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  name = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = 1, y = 10) 
            #if cur.execute("SELECT EXISTS"("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  name = '"+tosearch+"' ")) == False:  
            #    label = tk.Label(home_frame, text = "No Records", font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            #    label.place(x = 1, y = 180) 

        elif home_value == "kingdom":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
                #print(row)
        elif home_value == "phylum":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27
        elif home_value == "class":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27
        elif home_value == "naturalorder":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27
        elif home_value == "family":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27
        elif home_value == "genus":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27
        elif home_value == "species":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species = '"+tosearch+"' "):
                label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = ypos)
                ypos = ypos + 27

    label = tk.Label(home_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey",)
    label.place(x = 1, y = 150)

    global search_btn
    search_btn = tk.Button(home_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",
                             activeforeground = "dodgerblue3", command = lambda:(on_home_search_btn_click()))
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = 127)

    home_frame.pack(padx = 20, pady = 20)
    home_frame.configure(width = "650", height = "500")

def kingdom_page():
    kingdom_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(kingdom_frame, text = "KINGDOM",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(kingdom_frame, text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    result_frame = buildFrame(kingdom_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 145)
    result_frame.configure(width = "575", height = "290")

    def on_search_animal_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Animalia:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = 1, y = ypos)
            ypos = ypos + 27 

    #global search_animal_btn
    search_animal_btn = tk.Button(kingdom_frame, text = "ANIMALS", bg = "dodgerblue3",
                                        activeforeground = "dodgerblue3", command = lambda:(on_search_animal_btn_click()))
    search_animal_btn.bind("<Enter>", on_enter_global)
    search_animal_btn.bind("<Leave>", on_leave_global)
    search_animal_btn.place(x = "3", y = "98")


    def on_search_plant_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Plantae:"
        ypos = 11 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = 1, y = ypos) 
            ypos = ypos + 27 

    #global search_plant_btn
    search_plant_btn = tk.Button(kingdom_frame, text = "PLANT", bg = "dodgerblue3",
                                        activeforeground = "dodgerblue3", command = lambda:(on_search_plant_btn_click()))
    search_plant_btn.bind("<Enter>", on_enter_global)
    search_plant_btn.bind("<Leave>", on_leave_global)
    search_plant_btn.place(x = "78", y = "98")


    def on_search_fungi_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Fungi:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = 1, y = ypos) 
            ypos = ypos + 27 

    #global search_fungi_btn
    search_fungi_btn = tk.Button(kingdom_frame, text = "FUNGI", bg = "dodgerblue3",
                                        activeforeground = "dodgerblue3", command = lambda:(on_search_fungi_btn_click()))
    search_fungi_btn.bind("<Enter>", on_enter_global)
    search_fungi_btn.bind("<Leave>", on_leave_global)
    search_fungi_btn.place(x = "138", y = "98")


    def on_search_protista_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Protista:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = 1, y = ypos) 
            ypos = ypos + 27 
    
    #global search_protista_btn
    search_protista_btn = tk.Button(kingdom_frame, text = "PROTISTA", bg = "dodgerblue3",
                                        activeforeground = "dodgerblue3", command = lambda:(on_search_protista_btn_click()))
    search_protista_btn.bind("<Enter>", on_enter_global)
    search_protista_btn.bind("<Leave>", on_leave_global)
    search_protista_btn.place(x = "196", y = "98")


    def on_search_monera_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Monera:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = 1, y = ypos) 
            ypos = ypos + 27 

    #global search_monera_btn
    search_monera_btn = tk.Button(kingdom_frame, text = "MONERA", bg = "dodgerblue3",
                                        activeforeground = "dodgerblue3", command = lambda:(on_search_monera_btn_click()))
    search_monera_btn.bind("<Enter>", on_enter_global)
    search_monera_btn.bind("<Leave>", on_leave_global)
    search_monera_btn.place(x = "271", y = "98")

    label = tk.Label(kingdom_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey",)
    label.place(x = 1, y = 130)

    #search = tk.Entry(kingdom_frame, width = "30", bg = "aliceblue", fg = "dodgerblue3")
    #search.place(x = "1", y = "135")
    #contents = tk.StringVar()
    #contents.set("Type The Kingdom.")
    #search["textvariable"] = contents

    """"    def on_kingdom_search_btn_click():#=-=-=-=-=-=-=-=WRONG CONCEPT
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            tosearch = tosearch

        if value == "animals":
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = Animalia: "):
                label = tk.Label(kingdom_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = 1, y = 180) 

        elif value == "plant":
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = Plantae: "):
                label = tk.Label(kingdom_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = "175")
        elif value == "fungi":
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
                label = tk.Label(kingdom_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = "150")
        elif value == "protista":
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = tk.Label(kingdom_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = "150")
        elif value == "monera":
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = tk.Label(kingdom_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = "1", y = "150")
"""

    #global search_btn
    #search_btn = tk.Button(kingdom_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",
    #                         activeforeground = "dodgerblue3", command = lambda:(on_kingdom_search_btn_click()))
    #search_btn.bind("<Enter>", on_enter)
    #search_btn.bind("<Leave>", on_leave)
    #search_btn.place(x = "191", y = "132")


    kingdom_frame.pack(padx = 20, pady = 20)
    kingdom_frame.configure(width = "650", height = "500")

def phylum_page():
    global search_result_ypos 
    search_result_ypos = 160
    phylum_frame = tk.Frame(main_frame, highlightbackground= "dodgerblue3",  highlightthickness= "4", bg = "darkgrey")

    label = tk.Label(phylum_frame, text = "PHYLUM",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(phylum_frame , text = "Search by :-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    def radio_value(value_before):
        if value_before == "":
            label = tk.Label(phylum_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              bg = "darkgrey", fg = "red")
            label.place(x = "1", y = "470")
        else:
            global phylum_value
            phylum_value = value_before
            #print(value)
            if phylum_value == "Animalia":
                combo = Combobox(phylum_frame)
                combo["values"] = [ 
                "Chordate", 
                "Arthrpod", 
                "Molusc", 
                "Echinoderm", 
                "Annalid"
                ] 
                combo.set("Animalia")
                combo.current()
                combo.place(x = "1", y = "125")

            elif phylum_value == "Plantae":
                combo = Combobox(phylum_frame)
                combo["values"] = [  
                "Bryophyta", 
                "Cycadophyta", 
                "Ginkgophyta", 
                "Chlorophyta", 
                "Lycophyta"
                ]
                combo.set("Plantae")
                combo.current()
                combo.place(x = "1", y = "125")

            elif phylum_value == "Fungi":
                combo = Combobox(phylum_frame)
                combo["values"] = [ 
                "Ascomycota", 
                "Basidiomycota", 
                "Zygomycota",
                "Microsporidia",  
                "Bigyra",
                "Aphelida",
                "Mycetozoa"
                ]
                combo.set("Fungi")
                combo.current()
                combo.place(x = "1", y = "125")

            elif phylum_value == "Protista":
                combo = Combobox(phylum_frame)
                combo["values"] = [ 
                "Dinoflagellates", 
                "Amoebozoa", 
                "Rhodophyta",
                "Ciliates"  
                ] 
                combo.set("Protista")
                combo.current()
                combo.place(x = "1", y = "125")

            elif phylum_value == "Monera": 
                combo = Combobox(phylum_frame)
                combo["values"] = [ 
                "Archaebacteria", 
                "Schizopyta", 
                "Cyanophyta",
                "Prochlorophyta"  
                ] 
                combo.set("Monera")
                combo.current()
                combo.place(x = "1", y = "125")

    #label = tk.Label(phylum_frame, text = "Animals:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"),
    #                 bg = "darkgrey", fg = "black")
    #label.place(x = "1", y = 100)

    search_phylum_animal_menu =tk.Radiobutton( phylum_frame ,text = "Animal" , bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "Animalia", command = lambda:(radio_value("Animalia")))
    search_phylum_animal_menu.place(x = "1", y= "100") 

    #label = tk.Label(phylum_frame, text = "Plant:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
    #                   fg = "black")
    #label.place(x = "100", y = 100)

    search_phylum_plant_menu =tk.Radiobutton( phylum_frame ,text = "Plant" , bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "Plantae", command = lambda:(radio_value("Plantae")))
    search_phylum_plant_menu.place(x = "71", y= "100") 
    
    #label = tk.Label(phylum_frame, text = "Fungi:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
    #                   fg = "black")
    #label.place(x = "205", y = 100)

    search_phylum_fungi_menu =tk.Radiobutton( phylum_frame,text = "Fungi" , bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "Fungi", command = lambda:(radio_value("Fungi")))
    search_phylum_fungi_menu.place(x = "130", y= "100") 
    
    #label = tk.Label(phylum_frame, text = "Protista:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
    #                   fg = "black")
    #label.place(x = "323", y = 100)

    search_phylum_protista_menu =tk.Radiobutton( phylum_frame ,text = "Protista" , bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "Protista", command = lambda:(radio_value("Protista")))
    search_phylum_protista_menu.place(x = "190", y= "100") 
    
    #label = tk.Label(phylum_frame, text = "Monera:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
    #                   fg = "black")
    #label.place(x = "433", y = 100)

    search_phylum_monera_menu =tk.Radiobutton( phylum_frame ,text = "Monera" , bg = "darkgrey", activebackground = "darkgrey",
                                          activeforeground = "dodgerblue3", value = "Monera", command = lambda:(radio_value("Monera")))
    search_phylum_monera_menu.place(x = "253", y= "100") 
    
    """search = tk.Entry(phylum_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "153")
    contents = tk.StringVar()
    contents.set("Type The Order.")    
    contents = tk.StringVar()
    contents.set(clicked.get() )
    search["textvariable"] = contents
    
    global search_btn   
    search_btn = tk.Button(phylum_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3", command = show )
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "150")"""

    result_frame = buildFrame(phylum_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 165)
    result_frame.configure(width = 575, height = 270)

    label = tk.Label(phylum_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey",)
    label.place(x = 1, y = 150)
    
    combo = Combobox(phylum_frame)
    combo["values"] = ("Choose An Option!")
    combo.set("Please Choose An Option!")
    combo.current()
    contents = tk.StringVar()
    combo["textvariable"] = contents
    combo.place(x = "1", y = "125")
    
    def on_pylum_search_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        ypos = 10 
        tosearch = combo.get()
        tosearch = tosearch.title() + ":"
        print(tosearch)
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
            label = tk.Label(result_frame, text = row,font = ("Arial" , 10, "italic" ), bg = "darkgrey")
            label.place(x = "1", y = ypos)
            ypos = ypos + 27


    global search_btn
    search_btn = tk.Button(phylum_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",
                             activeforeground = "dodgerblue3", command = on_pylum_search_btn_click())
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "149", y = "123")


    phylum_frame.pack(padx = 20, pady = 20)
    phylum_frame.configure(width = "650", height = "500")

def class_page():
    class_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(class_frame, text = "CLASS",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(class_frame, text = "Search by Order:-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    result_frame = buildFrame(class_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 145)
    result_frame.configure(width = "575", height = "290")


    """search_mammallia_btn = tk.Radiobutton(class_frame, text = "MAMMALIA", bg = "darkgrey",
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
    search_diplopoda_btn.place(x = "285", y = "100")"""

    search = tk.Entry(class_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "105")
    contents = tk.StringVar()
    contents.set("Type The Class.")
    search["textvariable"] = contents

    global search_btn
    search_btn = tk.Button(class_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "101")

    label = tk.Label(class_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "130")

    class_frame.pack(padx = 20, pady = 20)
    class_frame.configure(width = "650", height = "500")

def order_page():
    order_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(order_frame, text = "ORDER",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(order_frame, text = "Search by Order:-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    """clicked1 = StringVar() 
    clicked1.set( "Primates" ) 
    options = [  
    "--Select--",
    "Primates", 
    "Chiroptera", 
    "Afrosoricida", 
    "Eriaceomorph", 
    "Rodentia"
    ] 
    
    label = tk.Label(order_frame, text = "Mammals:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
                       fg = "black")
    label.place(x = "1", y = 100)

    search_kingdom_menu = OptionMenu( order_frame , clicked1 , *options, command= drop_down_index_changed)# back = "dodgerblue3",) 
    search_kingdom_menu.place(x = "1", y= "125") 
    
    def show(): 
        search.config(contents.set(option_chosen)) 
        
    clicked2 = StringVar() 
    clicked2.set("Bryophyta") 

    options = [ 
    "--Select--",
    "Bryophyta", 
    "Gymnosperms", 
    "Angiosperms",
    "Ferns",  
    "Algea"
    ] 
    
    label = tk.Label(order_frame, text = "Plants:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
                       fg = "black")
    label.place(x = "110", y = 100)

    search_plant_menu = OptionMenu( order_frame,clicked2, *options, command= drop_down_index_changed)
    search_plant_menu.place(x = "110", y= "125") 

    def show(): 
        search.config(contents.set(option_chosen)) 

    clicked3 = StringVar() 
    clicked3.set("Glomeromycota") 

    options = [ 
    "--Select--",
    "Glomeromycota", 
    "Ascomycota", 
    "Chytridiomycota",
    "Basidiomycetes"  
    ] 
    
    label = tk.Label(order_frame, text = "Fungi:-",font = ("Bradley Hand ITC" , 12, "italic", "bold"), bg = "darkgrey",
                       fg = "black")
    label.place(x = "222", y = 100)

    search_Fungi_menu = OptionMenu( order_frame , clicked3 , *options, command= drop_down_index_changed)
    search_Fungi_menu.place(x = "222", y= "125") """
    

    result_frame = buildFrame(order_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)

    search = tk.Entry(order_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "105")
    contents = tk.StringVar()
    contents.set("<Search Orders>")
    search["textvariable"] = contents

    def on_order_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = tk.Label(order_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = 1, y = 170)
                print(row)
 
    global search_btn
    search_btn = tk.Button(order_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",
                            activeforeground = "dodgerblue3", command = on_order_page_search_btn_click )#, command = show 
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "101")

    label = tk.Label(order_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "130")

    order_frame.pack(padx = 20, pady = 20)
    order_frame.configure(width = "650", height = "500")

def family_page():
    family_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(family_frame, text = "FAMILY",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(family_frame, text = "Search by Family:-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search = tk.Entry(family_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "105")
    contents = tk.StringVar()
    contents.set("Type The Family.")
    search["textvariable"] = contents

    def on_family_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = tk.Label(family_frame, text = row, font = ("Arial" , 10, "italic" ), bg = "darkgrey")
                label.place(x = 1, y = 170)
                print(row)
    
    result_frame = buildFrame(family_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)


    label = tk.Label(family_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "130")

    global search_btn
    search_btn = tk.Button(family_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",
                             activeforeground = "dodgerblue3", command = on_family_page_search_btn_click())
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "101")

    family_frame.pack(padx = 20, pady = 20)
    family_frame.configure(width = "650", height = "500")

def genus_page():
    genus_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(genus_frame, text = "GENUS",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(genus_frame, text = "Search by Genus:-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search = tk.Entry(genus_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "105")
    contents = tk.StringVar()
    contents.set("Type The Genus.")
    search["textvariable"] = contents
    
    result_frame = buildFrame(genus_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)

    global search_btn
    search_btn = tk.Button(genus_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "101")

    label = tk.Label(genus_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "130")

    genus_frame.pack(padx = 20, pady = 20)
    genus_frame.configure(width = "650", height = "500")

def species_page():
    species_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

    label = tk.Label(species_frame, text = "SPEICES",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), bg = "darkgrey",
                      highlightbackground= "deepskyblue3",  highlightthickness= "3", fg = "dodgerblue3")
    label.place(x = "7", y = "3")
    label.configure(width = "28")

    label = tk.Label(species_frame, text = "Search by Speices:-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "70")

    search = tk.Entry(species_frame, width = "30", fg = "dodgerblue3")
    search.place(x = "1", y = "105")
    contents = tk.StringVar()
    contents.set("Type The Species.")
    search["textvariable"] = contents
    
    result_frame = buildFrame(species_frame,  "dodgerblue3",  "4", "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)

    global search_btn
    search_btn = tk.Button(species_frame, text = "SEARCH", bg = "dodgerblue3", activebackground = "darkgrey",  activeforeground = "dodgerblue3")
    search_btn.bind("<Enter>", on_enter)
    search_btn.bind("<Leave>", on_leave)
    search_btn.place(x = "191", y = "101")

    label = tk.Label(species_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), bg = "darkgrey")
    label.place(x = "1", y = "130")

    species_frame.pack(padx = 20, pady = 20)
    species_frame.configure(width = "650", height = "500")

def about_page():
    about_frame = buildFrame(main_frame,  "dodgerblue3",  "4", "darkgrey")

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

phylum_btn = tk.Button(option_frame, text = "Phylum-\n-Division", font = ("Bradley Hand ITC" , 15, "italic", "bold" ), fg = "dodgerblue3",
                     bd = 0, bg = "darkgray",  activebackground = "darkgray",
                    command = lambda: indicate(phylum_indicate, phylum_page))
phylum_btn.place(x = 15, y = 125)

phylum_indicate = tk.Label(option_frame, text = " ", bg = "darkgray")
phylum_indicate.place(x = 10, y = 125, width = 2, height = 65)

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

main_frame = buildFrame(root,  "dodgerblue3",  "4", "darkgrey")
main_frame.pack(side = "left")
main_frame.pack_propagate(False)
main_frame.configure(width = "650", height = "500")

root.mainloop()
