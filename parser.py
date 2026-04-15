import json

# 1. 模拟从 MakeMeAHanzi 的 graphics.txt 读取的原始数据
# "明" 字的 8 个笔画 SVG Path (真实的 MakeMeAHanzi 数据格式)
raw_data = {
    "character": "明",
    "strokes": [
        "M36.25,32.25c1.25,1.25... ", # 1. 日-竖
        "M40,34c5.17-0.79... ",       # 2. 日-横折
        "M40,51.25c4.62-0.5... ",     # 3. 日-横
        "M40.25,70.25c5.38... ",      # 4. 日-横
        "M69.46,16.75c1.04... ",      # 5. 月-撇
        "M71.75,19.25c4.75... ",      # 6. 月-横折钩
        "M71.75,39.5c5... ",          # 7. 月-横
        "M71.75,58.75c4.88... "       # 8. 月-横
    ]
}

# 2. 核心魔法：汉字笔顺的天然规律
# 汉字书写规则是“从左到右，从上到下”。
# 所以“明”字的前 4 画一定是“日”，后 4 画一定是“月”。
# 我们可以通过字典配置表，定义每个字的“拆解配方”和“对应笔画数”。
dictionary_config = {
    "明": [
        {"name": "日", "stroke_count": 4},
        {"name": "月", "stroke_count": 4}
    ],
    "休": [
        {"name": "亻", "stroke_count": 2},
        {"name": "木", "stroke_count": 4}
    ]
}

def parse_hanzi(character, raw_strokes):
    config = dictionary_config.get(character)
    if not config:
        return None
        
    result = {
        "character": character,
        "components": []
    }
    
    current_stroke_index = 0
    for comp in config:
        count = comp["stroke_count"]
        # 截取属于这个偏旁部首的 SVG 笔画
        comp_strokes = raw_strokes[current_stroke_index : current_stroke_index + count]
        
        result["components"].append({
            "name": comp["name"],
            "strokes": comp_strokes
        })
        
        current_stroke_index += count
        
    return result

# 3. 执行拆解并输出 JSON
parsed_json = parse_hanzi(raw_data["character"], raw_data["strokes"])
print(json.dumps(parsed_json, ensure_ascii=False, indent=2))
