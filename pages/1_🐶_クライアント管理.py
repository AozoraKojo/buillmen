from multiprocessing.connection import Client
from tkinter import Menu
from xmlrpc import client
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3 
import time
import streamlit.components.v1 as stc

st.set_page_config(page_title="Client", page_icon="ð¶")



# ãµã¤ããã¼ã«ç»é²ãã¼ã¸ã¸é·ç§»ããselectéç½®

Menu = st.sidebar.radio(
     "ã¡ãã¥ã¼",
     ('ã¯ã©ã¤ã¢ã³ãä¸è¦§', 'ã¯ã©ã¤ã¢ã³ãç»é²', 'ã¯ã©ã¤ã¢ã³ãç·¨é'))

# ã¯ã©ã¤ã¢ã³ãä¸è¦§è¡¨ç¤º
if Menu == 'ã¯ã©ã¤ã¢ã³ãä¸è¦§':

    st.title("ã¯ã©ã¤ã¢ã³ãä¸è¦§")
    
    ## ãã¼ã¿ãã¼ã¹æ¥ç¶ ##
    dbname = 'buillmen.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()


    # 3.ãã¼ãã«ã®ãã¼ã¿ãåå¾
    # ä¾ã§ã¯ãpersonsãã¼ãã«ãã¼ã¿ãå¨ä»¶åå¾
    cur.execute('SELECT * FROM Client')

    # ãã¼ãã«è¡¨ç¤ºç¨ã«ãã¼ã¿æ´å½¢
    Client_ID_List = []
    client_name_List = []
    CEO_name_List = []
    post_code_List = []
    address_List = []
    tell_List = []
    fax_List = []
    mail_List = []
    establish_List = []
    capital_List = []
    employee_List = []
    corporate_number_List = []
    manager_List = []
    manager_tell_List = []


    # åå¾ãããã¼ã¿ãè¡ãã¨ã«æ´å½¢
    for row in cur.fetchall():
        Client_ID_List.append(row[0])
        client_name_List.append(row[1])
        CEO_name_List.append(row[2])
        post_code_List.append(row[3])
        address_List.append(row[4])
        tell_List.append(row[5])
        fax_List.append(row[6])
        mail_List.append(row[7])
        establish_List.append(row[8])
        capital_List.append(row[9])
        employee_List.append(row[10])
        corporate_number_List.append(row[11])
        manager_List.append(row[12])
        manager_tell_List.append(row[13])

        st.write(row)

    # ãã¼ãã«ãã¼ã¿ã®ä½æ
    table_data = {
        'é¡§å®¢çªå·' : Client_ID_List,
        'é¡§å®¢å'   : client_name_List,
        'ä»£è¡¨'     : CEO_name_List,
        'éµä¾¿çªå·'  : post_code_List,
        'ä½æ'     : address_List,
        'é»è©±çªå·'     : tell_List,
        'FAXçªå·'     : fax_List,
        'ã¡ã¼ã«'     : mail_List,
        'è¨­ç«'     : establish_List,
        'è³æ¬é'     : capital_List,
        'éç¨äººæ°'     : employee_List,
        'æ³äººçªå·'     : corporate_number_List,
        'æå½è'     : manager_List,
        'æå½èé»è©±'     : manager_tell_List,
    }

    dataframe = pd.DataFrame(
        table_data,
        index = Client_ID_List
    )

    st.dataframe(dataframe)




    

    # 4.ãã¼ã¿ãã¼ã¹ã®æ¥ç¶ãåæ­
    cur.close()
    conn.close()


elif Menu == 'ã¯ã©ã¤ã¢ã³ãç»é²':

    st.title("ã¯ã©ã¤ã¢ã³ãç»é²")

    ## ãã¼ã¿ãã¼ã¹æ¥ç¶ ##
    dbname = 'buillmen.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #DBã«ã¦ã¼ã¶ã¼ãç»é²ããé¢æ°
    def create_user():
        cur.execute('CREATE TABLE IF NOT EXISTS Client(Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,client_name TEXT,CEO_name TEXT,post_code TEXT,address TEXT,tell TEXT,fax TEXT,mail TEXT,establish TEXT,capital TEXT,employee TEXT,corporate_number TEXT,manager TEXT,manager_tell TEXT)')
    #DBã«è¿½å ããã¦ã¼ã¶ã¼ã«ã¦ã¼ã¶ã¼æå ±ãè¿½å ããé¢æ°
    def add_user(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell):
        cur.execute('INSERT INTO Client(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell))
        conn.commit()


    client_name         = st.text_input('ã¯ã©ã¤ã¢ã³ãå')
    CEO_name            = st.text_input('ä»£è¡¨å')
    post_code           = st.text_input('éµä¾¿çªå·')
    address             = st.text_input('ä½æ')
    tell                = st.text_input('é»è©±çªå·')
    fax                 = st.text_input('FAXçªå·')
    mail                = st.text_input('ã¡ã¼ã«')
    establish           = st.text_input('è¨­ç«å¹´ææ¥')
    capital             = st.text_input('è³æ¬é')
    employee            = st.text_input('å¾æ¥­å¡æ°')
    corporate_number    = st.text_input('æ³äººçªå·')
    manager             = st.text_input('æå½è')
    manager_tell        = st.text_input('æå½èé»è©±')




        # Every form must have a submit button.
    submitted = st.button("ç»é²")
    if submitted:
        create_user()
        test = add_user(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell)
        st.success("ã¦ã¼ã¶ã¼ã®ä½æã«æåãã¾ãã")

    # 4.ãã¼ã¿ãã¼ã¹ã®æ¥ç¶ãåæ­
    cur.close()
    conn.close()




elif Menu == 'ã¯ã©ã¤ã¢ã³ãç·¨é':

    st.title("ã¯ã©ã¤ã¢ã³ãç·¨é")












# ã¯ã©ã¤ã¢ã³ãã®ä¸è¦§




# ã¯ã©ã¤ã¢ã³ãã®ç»é²




# ã¯ã©ã¤ã¢ã³ãã®ç·¨é





# ã¯ã©ã¤ã¢ã³ãã®åé¤


















