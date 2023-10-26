import codecs
import json

with open('chinese_character.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用列表推導式將字串分割為單一字元的列表
chinese_characters = [char for char in text]

# 建立一個空的字典，用來儲存BIG5編碼和Unicode編碼
character_data = []

# 產生BIG5編碼和Unicode編碼
for character in chinese_characters:
    try:
        big5_code = codecs.encode(character, 'big5').hex().upper()
        unicode_code = hex(ord(character)).upper()
    
        character_data.append({
            #"Character": character,
            "BIG5": "0x" + big5_code,
            "UNICODE": unicode_code
        })
    except UnicodeEncodeError:
        print(f"無法編碼字符：{character}")

data_dict = {"CP950": character_data}

with open("./script_ntut/CP950.json", "w", encoding="utf-8") as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=2)
