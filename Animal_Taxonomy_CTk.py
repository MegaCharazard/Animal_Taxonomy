
from customtkinter import *
import sqlite3

root = CTk()
root.geometry("1000x550")
root.title("Animal Taxonomy")
root.maxsize(width = 1000, height = 550)
root.iconbitmap(r"icon/favicon6.ico")

set_appearance_mode("Dark")

con = sqlite3.connect("Animal_Taxonomy_DB.db")
cur = con.cursor()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=PAGES=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def buildFrame(frame, border_color, border_width, fg_color = "dodgerblue3"):
    return CTkFrame(frame, border_color = border_color,  border_width= border_width, fg_color = fg_color)

def createRadioButton (_frame ,_text, _fg_color , _value , _command, _argu,  _xpos, _ypos ):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , fg_color = _fg_color, value = _value, command = lambda:(_command(_argu)))
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn

def home_page():
    home_frame = buildFrame(main_frame,  "dodgerblue3",  4, "transparent")

    label = CTkLabel(home_frame, text = "HOME",font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 300, y = 5)

    label = CTkLabel(home_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 10, y = 70)

    global radio_value
    def radio_value(value_before):
        if value_before == "":
            label = CTkLabel(home_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              fg_color = "transparent", fg = "red")
            label.place(x = 1, y = 470)
        else:
            global home_value
            home_value = value_before

    search_name_btn = createRadioButton (home_frame , "NAME", "darkgrey" , "NAME" , radio_value, "name", 10, 100 )

    search_kingdom_btn = createRadioButton (home_frame ,"KINGDOM", "darkgrey" , "NAME" , radio_value, "kingdom", 81, 100)

    search_phylum_btn = createRadioButton (home_frame ,"PHYLUM", "darkgrey" , "NAME" , radio_value, "phylum", 177, 100)

    search_class_btn = createRadioButton (home_frame ,"CLASS", "darkgrey" , "NAME" , radio_value, "class", 262, 100)

    search_order_btn = createRadioButton(home_frame ,"ORDER", "darkgrey" , "NAME" , radio_value, "naturalorder", 335, 100)

    search_family_btn = createRadioButton (home_frame ,"FAMILY", "darkgrey" , "NAME" , radio_value, "family", 415, 100)

    search_genus_btn = createRadioButton (home_frame ,"GENUS", "darkgrey" , "NAME" , radio_value, "genus", 495, 100)

    search_species_btn = createRadioButton (home_frame ,"SPECIES", "darkgrey" , "NAME" , radio_value, "species", 570, 100)

    search = CTkEntry(home_frame, width = 200, text_color = "#c850c0")
    search.place(x = 10, y = 130)
    global contents
    contents = StringVar()
    contents.set("Search As Per Your Option.")
    search["textvariable"] = contents

    result_frame = buildFrame(home_frame,  "#c850c0",  4, "transparent")
    result_frame.place(x = 20, y = 173)
    result_frame.configure(width = 770, height = 305)

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
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 30, "italic" ), text_color = "aliceblue")
                label.place(x = 1, y = 10) 

        elif home_value == "kingdom":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "phylum":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "class":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "naturalorder":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "family":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "genus":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "species":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

    label = CTkLabel(home_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
    label.place(x = 10, y = 160)

    
    search_btn = CTkButton(home_frame, text = "SEARCH", fg_color = "dodgerblue3",hover_color = "#c850c0",corner_radius = 35,
                            command = lambda :(on_home_search_btn_click()))
    search_btn.place(x = 215, y = 130)

    home_frame.pack(padx = 20, pady = 25)
    home_frame.configure(width = 850, height = 500)

def kingdom_page():
    kingdom_frame = buildFrame(main_frame,  "dodgerblue3",  4, "transparent")

    label = CTkLabel(kingdom_frame, text = "KINGDOM",font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 300, y = 5)

    label = CTkLabel(kingdom_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 10, y = 70)

    result_frame = buildFrame(kingdom_frame,  "#c850c0",  4, "transparent")
    result_frame.place(x = 20, y = 142)
    result_frame.configure(width = 770, height = 340)

    def on_search_animal_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Animalia:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos)
            ypos = ypos + 27 

    search_animal_btn = CTkButton(kingdom_frame, text = "ANIMALS", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                  command = lambda:(on_search_animal_btn_click()))
    search_animal_btn.place(x = 10, y = 98)


    def on_search_plant_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Plantae:"
        ypos = 11 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_plant_btn = CTkButton(kingdom_frame, text = "PLANT", fg_color = "dodgerblue3",hover_color = "#c850c0",  corner_radius = 40,
                                 command = lambda:(on_search_plant_btn_click()))
    search_plant_btn.place(x = 158, y = 98)


    def on_search_fungi_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Fungi:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_fungi_btn = CTkButton(kingdom_frame, text = "FUNGI", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                     command = lambda:(on_search_fungi_btn_click()))
    search_fungi_btn.place(x = 305, y = 98)


    def on_search_protista_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Protista:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 
    
    search_protista_btn = CTkButton(kingdom_frame, text = "PROTISTA", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                     command = lambda:(on_search_protista_btn_click()))
    search_protista_btn.place(x = 453, y = 98)


    def on_search_monera_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Monera:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_monera_btn = CTkButton(kingdom_frame, text = "MONERA", fg_color = "dodgerblue3",hover_color = "#c850c0",  corner_radius = 40,
                                     command = lambda:(on_search_monera_btn_click()))
    search_monera_btn.place(x = 600, y = 98)

    label = CTkLabel(kingdom_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent",text_color = "dodgerblue3")
    label.place(x = 10, y = 130)

    kingdom_frame.pack(padx = 20, pady = 25)
    kingdom_frame.configure(width = 850, height = 500)

def phylum_page():
    global search_result_ypos 
    search_result_ypos = 160
    phylum_frame = buildFrame(main_frame,  "dodgerblue3",  4, "transparent")

    label = CTkLabel(phylum_frame, text = "PHYLUM",font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 300, y = 5)
    label.configure(width = 28)

    label = CTkLabel(phylum_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 10, y = 70)


    def radio_value(value_before):
        if value_before == "":
            label = CTkLabel(phylum_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              fg_color = "darkgrey", fg = "red")
            label.place(x = 10, y = 470)
        else:
            global phylum_value
            phylum_value = value_before
        
            if phylum_value == "Animalia":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Chordate", 
                "Arthrpod", 
                "Molusc", 
                "Echinoderm", 
                "Annalid"
                ] 
                combo.set("Animalia")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Plantae":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [  
                "Bryophyta", 
                "Cycadophyta", 
                "Ginkgophyta", 
                "Chlorophyta", 
                "Lycophyta"
                ]
                combo.set("Plantae")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Fungi":
                combo = CTkComboBox(phylum_frame, width = 200)
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
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Protista":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Dinoflagellates", 
                "Amoebozoa", 
                "Rhodophyta",
                "Ciliates"  
                ] 
                combo.set("Protista")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Monera": 
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Archaebacteria", 
                "Schizopyta", 
                "Cyanophyta",
                "Prochlorophyta"  
                ] 
                combo.set("Monera")
                #combo.current()
                combo.place(x = 10, y = 130)

    search_phylum_animal_menu =createRadioButton (phylum_frame ,"Animal", "darkgrey" , "NAME" , radio_value, "Animalia", 10, 100)

    search_phylum_plant_menu =createRadioButton (phylum_frame ,"Plant", "darkgrey" , "NAME" , radio_value, "Plantae", 85, 100)

    search_phylum_fungi_menu =createRadioButton (phylum_frame ,"Fungi", "darkgrey" , "NAME" , radio_value, "Fungi", 150, 100)

    search_phylum_protista_menu =createRadioButton (phylum_frame ,"Protista", "darkgrey" , "NAME" , radio_value, "Protista", 215, 100)

    search_phylum_monera_menu =createRadioButton (phylum_frame ,"Monera", "darkgrey" , "Monera" , radio_value, "Animalia", 295, 100)

    result_frame = buildFrame(phylum_frame,  "#c850c0",  4, "transparent")
    result_frame.place(x = 20, y = 173)
    result_frame.configure(width = 770, height = 305)

    label = CTkLabel(phylum_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
    label.place(x = 10, y = 160)
    
    combo = CTkComboBox(phylum_frame, width = 200)
    combo["values"] = ("Choose", "An", "Option!")
    combo.set("Please Choose An Option!")
    #combo.current()
    contents = StringVar()
    combo["textvariable"] = contents
    combo.place(x = 10, y = 130)
    
    def on_pylum_search_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        ypos = 10 
        tosearch = combo.get()
        tosearch = tosearch.title() + ":"
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
            label.place(x = 1, y = ypos)
            ypos = ypos + 27


    global search_btn
    search_btn = CTkButton(phylum_frame, text = "SEARCH", fg_color = "dodgerblue3", hover_color = "#c850c0", corner_radius = 40, 
                           command = on_pylum_search_btn_click())
    search_btn.place(x = 230, y = 130)

    phylum_frame.pack(padx = 20, pady = 25)
    phylum_frame.configure(width = 850, height = 500)

def class_page():
    class_frame = buildFrame(main_frame,  "dodgerblue3",  4, "transparent")

    label = CTkLabel(class_frame, text = "CLASS",font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 300, y = 5)

    label = CTkLabel(class_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 10, y = 70)

    result_frame = buildFrame(class_frame,  "#c850c0",  4, "transparent")
    result_frame.place(x = 20, y = 153)
    result_frame.configure(width = 770, height = 325)

    search = CTkEntry(class_frame, width = 200, text_color = "#c850c0")
    search.place(x = 10, y = 105)
    global contents
    contents = StringVar()
    contents.set("Search For Classes.")
    search["textvariable"] = contents

    def on_class_search_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
        else:
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
 
    search_btn = CTkButton(class_frame, text = "SEARCH", fg_color = "dodgerblue3", hover_color = "#c850c0", corner_radius = 40,
                           command = on_class_search_click())
    search_btn.place(x = 221, y = 105)

    label = CTkLabel(class_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
    label.place(x = 10, y = 140)

    class_frame.pack(padx = 20, pady = 25)
    class_frame.configure(width = 850, height = 500)

def order_page():
    order_frame = buildFrame(main_frame,  "dodgerblue3",  4, "transparent")

    label = CTkLabel(order_frame, text = "CLASS",font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 300, y = 5)

    label = CTkLabel(order_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    label.place(x = 10, y = 70)

    result_frame = buildFrame(order_frame,  "#c850c0",  4, "transparent")
    result_frame.place(x = 20, y = 153)
    result_frame.configure(width = 770, height = 325)

    search = CTkEntry(order_frame, width = 200, text_color = "#c850c0")
    search.place(x = 10, y = 105)
    contents = StringVar()
    contents.set("Search For Orders")
    search["textvariable"] = contents

    def on_order_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
        else:
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
 
    search_btn = CTkButton(order_frame, text = "SEARCH", fg_color = "dodgerblue3", hover_color = "#c850c0", corner_radius = 40,
                           command = on_order_page_search_btn_click())
    search_btn.place(x = 221, y = 105)


    label = CTkLabel(order_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), text_color = "dodgerblue3")
    label.place(x = 10, y = 140)

    order_frame.pack(padx = 20, pady = 25)
    order_frame.configure(width = 850, height = 500)

def family_page():
    family_frame = buildFrame(main_frame,  "dodgerblue3",  4, "darkgrey")

    label = CTkLabel(family_frame, text = "FAMILY",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), fg_color = "darkgrey",
                      border_color= "deepskyblue3",  border_width= 3)
    label.place(x = 7, y = 3)
    label.configure(width = 28)

    label = CTkLabel(family_frame, text = "Search by Family:-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 70)

    search = CTkEntry(family_frame, width = 30)
    search.place(x = 1, y = 105)
    contents = CTk.StringVar()
    contents.set("Search For Family.")
    search["textvariable"] = contents

    def on_family_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            for label in result_frame.winfo_children():
                label.destroy()
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = CTkLabel(family_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = 170)
    
    result_frame = buildFrame(family_frame,  "dodgerblue3", 4, "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)


    label = CTkLabel(family_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 130)

    global search_btn
    search_btn = CTkButton(family_frame, text = "SEARCH", fg_color = "dodgerblue3", activebackground = "darkgrey",hover_color = "#c850c0",
                             activeforeground = "dodgerblue3", command = on_family_page_search_btn_click())
    search_btn.place(x = 191, y = 101)

    family_frame.pack(padx = 20, pady = 20)
    family_frame.configure(width = 650, height = 500)

def genus_page():
    genus_frame = buildFrame(main_frame,  "dodgerblue3",  4, "darkgrey")

    label = CTkLabel(genus_frame, text = "GENUS",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), fg_color = "darkgrey",
                      border_color= "deepskyblue3",  border_width= 3)
    label.place(x = 7, y = 3)
    label.configure(width = 28)

    label = CTkLabel(genus_frame, text = "Search by Genus:-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 70)

    search = CTkEntry(genus_frame, width = 30)
    search.place(x = 1, y = 105)
    contents = CTk.StringVar()
    contents.set("Search For Genus.")
    search["textvariable"] = contents
    
    result_frame = buildFrame(genus_frame,  "dodgerblue3",  4, "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)

    global search_btn
    search_btn = CTkButton(genus_frame, text = "SEARCH", fg_color = "dodgerblue3", activebackground = "darkgrey",hover_color = "#c850c0", 
                           activeforeground = "dodgerblue3")
    search_btn.place(x = 191, y = 101)

    label = CTkLabel(genus_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 130)

    genus_frame.pack(padx = 20, pady = 20)
    genus_frame.configure(width = 650, height = 500)

def species_page():
    species_frame = buildFrame(main_frame,  "dodgerblue3",  4, "darkgrey")

    label = CTkLabel(species_frame, text = "SPEICES",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), fg_color = "darkgrey",
                      border_color= "deepskyblue3",  border_width= 3)
    label.place(x = 7, y = 3)
    label.configure(width = 28)

    label = CTkLabel(species_frame, text = "Search by Speices:-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 70)

    search = CTkEntry(species_frame, width = 30)
    search.place(x = 1, y = 105)
    contents = CTk.StringVar()
    contents.set("Search For Species.")
    search["textvariable"] = contents
    
    result_frame = buildFrame(species_frame,  "dodgerblue3",  4, "darkgrey")
    result_frame.place(x = 10, y = 144)
    result_frame.configure(width = 575, height = 290)

    global search_btn
    search_btn = CTkButton(species_frame, text = "SEARCH", fg_color = "dodgerblue3", activebackground = "darkgrey",hover_color = "#c850c0", 
                           activeforeground = "dodgerblue3")
    search_btn.place(x = 191, y = 101)

    label = CTkLabel(species_frame, text = "Search Results(s):-",font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = 1, y = 130)

    species_frame.pack(padx = 20, pady = 20)
    species_frame.configure(width = 650, height = 500)

def about_page():
    about_frame = buildFrame(main_frame,  "dodgerblue3",  4, "darkgrey")

    label = CTkLabel(about_frame, text = "ABOUT",font = ("Bradley Hand ITC" , 25, "italic", "bold" ), fg_color = "darkgrey",
                      border_color= "deepskyblue3",  border_width= 3)
    label.place(x = 7, y = 3)
    label.configure(width = 28)

    
    label = CTkLabel(about_frame, text = "We are a group of students studying in XI std,\n\
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
        Thank you for using this program © AnimalTaxonaomy HAPAA™", 
                        font = ("Brush Script MT" , 15, "italic" ), fg_color = "darkgrey")
    label.place(x = "0", y = 100)

    about_frame.pack(padx = 20, pady = 20)
    about_frame.configure(width = 650, height = 500)

#=-=-=-=-=-=-=-EXTRA-=-=-=-=-=-=-=#

def hide_indicator():
    home_indicate.configure(fg_color = "transparent")
    kingdom_indicate.configure(fg_color = "transparent")
    phylum_indicate.configure(fg_color = "transparent")
    class_indicate.configure(fg_color = "transparent")
    order_indicate.configure(fg_color = "transparent")
    family_indicate.configure(fg_color = "transparent")
    genus_indicate.configure(fg_color = "transparent")
    species_indicate.configure(fg_color = "transparent")
    about_indicate.configure(fg_color = "transparent")

def indicate(lb, page):
    hide_indicator()
    #lb.configure(fg_color = "dodgerblue3")
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

option_frame = CTkFrame(root, fg_color = "transparent")

home_btn = CTkButton(option_frame, text = "Home", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                     command = lambda: indicate(home_indicate, home_page))
home_btn.place(x = 15, y = 95)

home_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
home_indicate.place(x = 10, y = 25)

kingdom_btn = CTkButton(option_frame, text = "Kingdom", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                        command = lambda: indicate(kingdom_indicate, kingdom_page))
kingdom_btn.place(x = 15, y = 140)

kingdom_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
kingdom_indicate.place(x = 10, y = 75)

phylum_btn = CTkButton(option_frame, text = "Phylum-\n-Division", font = ("Bradley Hand ITC" , 15, "italic", "bold" ),hover_color = "#c850c0", 
                       command = lambda: indicate(phylum_indicate, phylum_page))                  
phylum_btn.place(x = 15, y = 185)

phylum_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 65)
phylum_indicate.place(x = 10, y = 125)

class_btn = CTkButton(option_frame, text = "Class", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                      command = lambda: indicate(class_indicate, class_page))
class_btn.place(x = 15, y = 245)

class_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
class_indicate.place(x = 10, y = 175)

order_btn = CTkButton(option_frame, text = "Order", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                      command = lambda: indicate(order_indicate, order_page))
order_btn.place(x = 15, y = 290)

order_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
order_indicate.place(x = 10, y = 225)

family_btn = CTkButton(option_frame, text = "Family", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                       command = lambda: indicate(family_indicate, family_page))
family_btn.place(x = 15, y = 335)

family_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
family_indicate.place(x = 10, y = 275)

genus_btn = CTkButton(option_frame, text = "Genus", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                      command = lambda: indicate(genus_indicate, genus_page))
genus_btn.place(x = 15, y = 380)

genus_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
genus_indicate.place(x = 10, y = 325)

species_btn = CTkButton(option_frame, text = "Species", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                        command = lambda: indicate(species_indicate, species_page))
species_btn.place(x = 15, y = 425)

species_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
species_indicate.place(x = 10, y = 375)


about_btn = CTkButton(option_frame, text = "About", font = ("Bradley Hand ITC" , 20, "italic", "bold" ),hover_color = "#c850c0", 
                      command = lambda: indicate(about_indicate, about_page))
about_btn.place(x = 15, y = 470)

about_indicate = CTkLabel(option_frame, text = " ", fg_color = "transparent", width = 2, height = 60)
about_indicate.place(x = 10, y = 425)

option_frame.pack(side = "left")
option_frame.pack_propagate(False)
option_frame.configure(width = 150, height = 500)

main_frame = buildFrame(root,  "#FFCC70",  4, "transparent")
main_frame.pack(side = "left")
main_frame.pack_propagate(False)
main_frame.configure(width = 950, height = 550)

root.mainloop()