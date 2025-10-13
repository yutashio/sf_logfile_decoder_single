# Salesforce イベントログ Base64 デコードツール

**SalesforceのEvent Log File**の  `LogFile` 項目に格納された **Base64 文字列**をデコードし、人間が読める文章＆CSV形式に変換するためのシンプルなPythonスクリプトを作成してみました。  

## はじめに

SalesforceのEvent Log File を**Data Loader を使用して一括でダウンロード**しました。  

しかし、Data Loaderで出力される `EventLogFile`の`LogFile`項目は**Base64 形式でエンコードされており**、そのままでは中身を確認することができません。  

内容を確認したいときは、Base64からのデコードが必要です。  

そこで、Base64文字列をセットしてPythonスクリプトを実行すればログの中身を確認できる
**シンプルなデコードツール**を作成しました 🧑‍💻  

※最小限の構成です。  
今後の拡張（ファイル入力対応・自動化・加工処理など）のベースとしてご活用ください💁‍♂️  

## 使い方

### 1. Base64 文字列を貼り付ける
`logfile_decode.py` の以下箇所に、  
Data Loaderで出力された`LogFile`のBase64文字列を貼り付けます。

```python
logfile_b64 = """
<ここに[LogFile]の値をセット>
"""
```

### 2. スクリプトを実行
ターミナルまたはコマンドプロンプトから下記を実行します。
```bash
python logfile_decode.py
```

### 3. 出力結果

#### 成功時
- `EVENT_TYPE`列に値がある場合 → その値をファイル名にして CSV ファイルを出力  
	- 例：`LOGIN.csv`  
- `EVENT_TYPE`列に値がない場合 → `logfile_decode.csv` として出力  

結果：  
```
✅ デコード完了: LOGIN.csv を出力しました。
```

#### エラー発生時
Base64 が不正な場合はエラーメッセージを表示して処理を終了します。