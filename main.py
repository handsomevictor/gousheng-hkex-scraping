import pandas as pd
import os
import datetime


# def get_companies_before_2000():
#     data = pd.read_csv(os.path.join(os.getcwd(), '香港交易所上市公司列表.csv'), encoding='utf-8')
#
#     # first filter out those without 上市日期 (there is a '-' in the column)
#     data = data[data['上市日期'] != '-']
#
#     # filter out those not in format: %Y年%m月%d日
#     data = data[data['上市日期'].apply(lambda x: len(str(x)) <= 13)]
#
#     # change formate of 1972年11月1日 to datetime
#     data['上市日期'] = pd.to_datetime(data['上市日期'], format='%Y年%m月%d日', errors='coerce')
#
#     # sort by 上市日期
#     data = data.sort_values(by='上市日期')
#
#     # filter out those before 2000
#     data = data[data['上市日期'] < datetime.datetime(2000, 1, 1)]
#
#     # save to local
#     data.to_csv(os.path.join(os.getcwd(), '香港交易所上市公司列表_before_2000.csv'), index=True)
#     return data


def generate_summary():
    # res = get_companies_before_2000()
    # stock_id_list = [int(i) for i in res['香港交易所代号'].tolist()]
    # stock_id_list.sort()
    # print(f'there are {len(stock_id_list)} stocks before 2000')

    director_list_df = pd.read_excel(os.path.join(os.getcwd(), 'Director_List.xls'), sheet_name='Director List')

    # filter out those in stock_id_list in colume: Stock Code
    # director_list_df = director_list_df[director_list_df['Stock Code'].isin(stock_id_list)]

    # director_list_df.to_csv(os.path.join(os.getcwd(), 'Director_List_before_2000_full_list.csv'), index=False)

    # only filter those that had any changes before 2000 and after 1997
    director_list_df['Appointment Date (yyyy-mm-dd)'] = pd.to_datetime(director_list_df
                                                                       ['Appointment Date (yyyy-mm-dd)'],
                                                                       format='%Y-%m-%d')
    director_list_df['Resignation Date (yyyy-mm-dd)'] = pd.to_datetime(director_list_df
                                                                       ['Resignation Date (yyyy-mm-dd)'],
                                                                       format='%Y-%m-%d')

    # filter out either Appointment Date (yyyy-mm-dd) or Resignation Date (yyyy-mm-dd) is before 2000 and after 1997
    director_list_df = director_list_df[
        ((director_list_df['Appointment Date (yyyy-mm-dd)'] < datetime.datetime(2000, 1, 1)) &
         (director_list_df['Appointment Date (yyyy-mm-dd)'] > datetime.datetime(1997, 1, 1))) |
        ((director_list_df['Resignation Date (yyyy-mm-dd)'] < datetime.datetime(2000, 1, 1)) &
         (director_list_df['Resignation Date (yyyy-mm-dd)'] > datetime.datetime(1997, 1, 1)))
        ]

    director_list_df = director_list_df.sort_values(by='Stock Code')
    # add 0 to the front of the stock code to make it 5 digits
    director_list_df['Stock Code'] = director_list_df['Stock Code'].apply(lambda x: str(x).zfill(5))

    director_list_df.to_csv(os.path.join(os.getcwd(), 'Director_List_before_2000_final_list.csv'), index=False)


if __name__ == '__main__':
    generate_summary()
