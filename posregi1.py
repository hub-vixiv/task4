import pandas as pd
import datetime as dt

from pandas.core.algorithms import mode


class PosRegi():

    def __init__(self, items_master_csv):
        # 商品マスタ―のファイル名を引数として受け取って
        # 商品マスターのデータフレームを作成
        #1列目の商品コードをindexに指定
        # self.master_df = pd.read_csv(items_master_csv, encoding='utf-8',index_col=0)

        self.master_df=pd.DataFrame(columns=['code','name','unit_price'])
        with open(items_master_csv,mode='r',encoding='utf-8') as f:
            next(f)
            i=1
            for line in f:
                iteminfo = line.strip().split(',')
                self.master_df.loc[i]=iteminfo
                i+=1
        self.master_df.set_index('code',inplace=True)
        self.master_df = self.master_df.astype({'unit_price':int})

        #空のオーダーリストを作成
        self.order_list = []

        #空のオーダーDF作成
        self.order_df=pd.DataFrame(columns=['注文番号','商品コード','商品名','数','単価','小計'])
        self.order_df.set_index('注文番号', inplace=True)

        #合計用の変数
        self.order_total = 0
        self.p_total=""

        #預かり金額用の変数
        self.deposit = 0
        self.p_deposit=""

        #お釣り用の変数
        self.change_amount = 0
        self.p_change=""

    # オーダーの合計を計算して返す
    def cal_total(self):      
        self.order_total = self.order_df['小計'].sum()
        # 合計を表示
        self.p_total= f"合 計　{self.order_total:>5}円"
        print(self.p_total)

    # お釣りを計算
    def cal_change(self): 
        self.deposit = int(input("お預かり金額を入力してください。："))
        while True:
            if self.deposit < self.order_total :
                print(f'お金が{self.order_total - self.deposit}円足りません。')
                self.deposit += int(input('追加する金額を入力して下さい'))
                continue
            else:
                break
        self.change_amount = self.deposit - self.order_total
        self.p_deposit= f"お預り　{self.deposit:>5}円"
        self.p_change = f"お釣り　{self.change_amount:>5}円"
        print(self.p_change)


    #csvファイル出力
    def order_df_to_csv(self):
        now_time = dt.datetime.now()
        file_name = f"{now_time:%Y%m%d-%H%M%S}.txt"
        self.order_df.to_csv(file_name,encoding='utf-8')

        with open(file_name, mode='a',encoding='utf-8') as f:
            f.write('－－－－－－－－\n')
            f.write(self.p_total + "\n")
            f.write(self.p_deposit + "\n")
            f.write(self.p_change + "\n")

    #オーダーを受付て、データフレームへ格納
    #商品名と価格を返す
    def accept_order(self):
        order_number=0
        #商品コードに0が入力されるまでwhileで回す
        while True:
            order_number += 1

            #商品コードの入力を受付
            itemcode = input('商品コードを入力して下さい。（オーダーストップは0エンター）：')
            if itemcode == '0':     #0が入力されたのでオーダー終了
                break               #while　抜ける
            elif itemcode == '':
                continue
            else:       #オーダー受付中
                #数の入力を受付
                quantity = int(input('オーダー数を入力して下さい。：'))

                #入力された商品コードの商品名を、商品マスターから取得
                item_name = self.master_df.loc[itemcode, 'name']

                #入力された商品コードの単価を、商品マスターから取得
                price = self.master_df.loc[itemcode, 'unit_price']

                # オーダー内容を表示
                print(f"{item_name}　{quantity}個")
                #注文内容をデータフレームに追加
                self.order_df.loc[str(order_number)] = [itemcode,item_name,quantity,str(price),price*quantity]

        #オーダー受付終了、一覧表示
        print(self.order_df)

        #合計を計算して、表示
        self.cal_total()

        #お金を預かって、お釣りを計算
        self.cal_change()

        #レシートcsv出力
        self.order_df_to_csv()
