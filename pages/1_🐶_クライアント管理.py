from multiprocessing.connection import Client
from xmlrpc import client
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3 
import time
import numpy as np

st.set_page_config(page_title="Client", page_icon="🐶")
st.title("クライアント管理")



## クライアントの一覧表示 ##


# カレントディレクトリにTEST.dbがなければ、作成します。
# すでにTEST.dbが作成されていれば、TEST.dbに接続します。
dbname = 'buillmen.db'
conn = sqlite3.connect(dbname)

# 2.sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# 3.テーブルのデータを取得
# 例では、personsテーブルデータを全件取得
cur.execute('SELECT * FROM Client')



# df = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)


# # テーブル表示用にデータ整形
# Client_ID_List = []
# client_name_List = []
# CEO_name_List = []
# post_code_List = []
# address_List = []
# tell_List = []
# fax_List = []
# mail_List = []
# establish_List = []
# capital_List = []
# employee_List = []
# corporate_number_List = []
# manager_List = []
# manager_tell_List = []

# # 取得したデータを出力
# for row in cur:
#     st.write(row)
#     Client_ID_List.append(row[0])
#     client_name_List.append(row[1])
#     CEO_name_List.append(row[2])
#     post_code_List.append(row[3])
#     address_List.append(row[4])
#     tell_List.append(row[5])
#     fax_List.append(row[6])
#     mail_List.append(row[7])
#     establish_List.append(row[8])
#     capital_List.append(row[9])
#     employee_List.append(row[10])
#     corporate_number_List.append(row[11])
#     manager_List.append(row[12])
#     manager_tell_List.append(row[13])


    



# st.write(Client_ID_List)
# st.table(df.style.highlight_max(axis=0))

# 4.データベースの接続を切断
cur.close()
conn.close()
















# クライアントの一覧




# クライアントの登録




# クライアントの編集





# クライアントの削除





















###### Demo #########

# st.sidebar.header("")
# st.write(
#     """This demo illustrates a combination of plotting and animation with
# Streamlit. We're generating a bunch of random numbers in a loop for around
# 5 seconds. Enjoy!"""
# )

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")

###### Demo #########