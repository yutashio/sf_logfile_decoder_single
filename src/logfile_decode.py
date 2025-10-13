import base64
import sys

# Base64にエンコードされている[LogFile]の値をセット
logfile_b64 = """
<ここに[LogFile]の値をセット>
"""

try:
    # Base64 → bytesへ変換
    decodedLogFile = base64.b64decode(logfile_b64).decode("utf-8")
except Exception as e:
    print("❌ Base64のデコードに失敗しました。")
    print(f"詳細: {e}")
    sys.exit(1)

# 改行コードで分割
lines = decodedLogFile.strip().splitlines()
headers = lines[0].split(",")
values = lines[1].split(",")

# EVENT_TYPEをファイル名とする。
fileName = "logfile_decode"
if '"EVENT_TYPE"' in headers:
    idx = headers.index('"EVENT_TYPE"')
    fileName = values[idx].strip('"\'')

# CSV出力
with open(fileName + ".csv", "w", encoding="utf-8", newline="") as f:
    f.write(decodedLogFile)
print(f"✅ デコード完了: {fileName}.csv を出力しました。")