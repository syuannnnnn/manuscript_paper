import codecs

with open('chinese_character.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用列表推导式将字符串分割为单个字符的列表
chinese_characters = [char for char in text]

# 创建一个空的字典，用于存储BIG5编码和Unicode编码
character_data = []

# 生成BIG5编码和Unicode编码
for character in chinese_characters:
    try:
        # 使用codecs库进行BIG5编码
        big5_code = codecs.encode(character, 'big5').hex().upper()
        
        # 使用ord()函数获取Unicode编码
        unicode_code = hex(ord(character)).upper()
        
        # 将BIG5编码和Unicode编码添加到字典中
        character_data.append({
            "Character": character,
            "BIG5": "0x" + big5_code,
            "UNICODE": unicode_code
        })
    except UnicodeEncodeError:
        print(f"无法编码字符：{character}")

# 将数据保存为JSON文件
import json

with open("chinese_characters.json", "w", encoding="utf-8") as json_file:
    json.dump(character_data, json_file, ensure_ascii=False, indent=2)
