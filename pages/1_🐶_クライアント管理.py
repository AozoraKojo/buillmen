from multiprocessing.connection import Client
from tkinter import Menu
from xmlrpc import client
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3 
import time
import streamlit.components.v1 as stc

st.set_page_config(page_title="Client", page_icon="🐶")



# サイドバーに登録ページへ遷移するselect配置

Menu = st.sidebar.radio(
     "メニュー",
     ('クライアント一覧', 'クライアント登録', 'クライアント編集'))

# クライアント一覧表示
if Menu == 'クライアント一覧':

    st.title("クライアント一覧")
    
    ## データベース接続 ##
    dbname = 'buillmen.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()


    # 3.テーブルのデータを取得
    # 例では、personsテーブルデータを全件取得
    cur.execute('SELECT * FROM Client')

    # テーブル表示用にデータ整形
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


    # 取得したデータを行ごとに整形
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

    # テーブルデータの作成
    table_data = {
        '顧客番号' : Client_ID_List,
        '顧客名'   : client_name_List,
        '代表'     : CEO_name_List,
        '郵便番号'  : post_code_List,
        '住所'     : address_List,
        '電話番号'     : tell_List,
        'FAX番号'     : fax_List,
        'メール'     : mail_List,
        '設立'     : establish_List,
        '資本金'     : capital_List,
        '雇用人数'     : employee_List,
        '法人番号'     : corporate_number_List,
        '担当者'     : manager_List,
        '担当者電話'     : manager_tell_List,
    }

    dataframe = pd.DataFrame(
        table_data,
        index = Client_ID_List
    )

    st.dataframe(dataframe)




    

    # 4.データベースの接続を切断
    cur.close()
    conn.close()


elif Menu == 'クライアント登録':

    st.title("クライアント登録")

    ## データベース接続 ##
    dbname = 'buillmen.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #DBにユーザーを登録する関数
    def create_user():
        cur.execute('CREATE TABLE IF NOT EXISTS Client(Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,client_name TEXT,CEO_name TEXT,post_code TEXT,address TEXT,tell TEXT,fax TEXT,mail TEXT,establish TEXT,capital TEXT,employee TEXT,corporate_number TEXT,manager TEXT,manager_tell TEXT)')
    #DBに追加したユーザーにユーザー情報を追加する関数
    def add_user(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell):
        cur.execute('INSERT INTO Client(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell))
        conn.commit()


    client_name         = st.text_input('クライアント名')
    CEO_name            = st.text_input('代表名')
    post_code           = st.text_input('郵便番号')
    address             = st.text_input('住所')
    tell                = st.text_input('電話番号')
    fax                 = st.text_input('FAX番号')
    mail                = st.text_input('メール')
    establish           = st.text_input('設立年月日')
    capital             = st.text_input('資本金')
    employee            = st.text_input('従業員数')
    corporate_number    = st.text_input('法人番号')
    manager             = st.text_input('担当者')
    manager_tell        = st.text_input('担当者電話')




        # Every form must have a submit button.
    submitted = st.button("登録")
    if submitted:
        create_user()
        test = add_user(client_name,CEO_name,post_code,address,tell,fax,mail,establish,capital,employee,corporate_number,manager,manager_tell)
        st.success("ユーザーの作成に成功しました")

    # 4.データベースの接続を切断
    cur.close()
    conn.close()




elif Menu == 'クライアント編集':

    st.title("クライアント編集")












# クライアントの一覧




# クライアントの登録




# クライアントの編集





# クライアントの削除


















