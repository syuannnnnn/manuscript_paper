import codecs
import json

with open('chinese_character.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用列表推導式將字串分割為單一字元的列表
chinese_characters = [char for char in text]

character_data = []
unicode_characters = []

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

        unicode_code_train = "\\u" + hex(ord(character))[2:].upper().zfill(4)
        unicode_characters.append(unicode_code_train)

    except UnicodeEncodeError:
        print(f"無法編碼字符：{character}")

data_dict = {"CP950": character_data}
data_dict2 = {"twTrain": unicode_characters}

#存檔
with open("./script_ntut/CP950.json", "w", encoding="utf-8") as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=2)

json_text = json.dumps(data_dict2, ensure_ascii=False,  separators=(', ', ':')).replace("\\\\", "\\")

with open("cjk.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_text)