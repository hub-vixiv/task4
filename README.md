## task4
課題４のREADME.mdだけで、作成

### クラス定義ファイルと実行ファイの対応
 クラス定義ファイル　　実行ファイル  
 posregi1.py　－－－－　minipos1.py  
 posregi2.py　－－－－　minipos2.py  



### 違い
#### １．posregi1.py
商品マスターのcsvファイルをopenで読み込み  
一行ずつDataFrameに追加で、格納

#### ２．posregi2.py
商品マスターのcsvファイルを  
key：商品コード  
value：［商品名，単価］（リスト）  
の辞書型に格納

### read_csvでは・・・  


DataFrameにlocで値を取りに行ったときに、エラーで使えなかったため  
csvファイルの読み込み方法を変更  


1つのファイル内で実行する際はエラーなし  
DataFrameをインスタンス変数にして使おうとするとエラー  
クラス変数にしても同じ
