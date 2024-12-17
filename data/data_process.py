import json

# 读取原始 .jsonl 文件并转换为目标格式
def convert_jsonl_to_target_format(input_file, output_file):
    data_list = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            data = json.loads(line.strip())
            question = data.get("question", "")
            options = f"A:{data.get('A')}, B:{data.get('B')}, C:{data.get('C')}, D:{data.get('D')}"
            output = f"{data.get('answer_idx')}:{data.get('answer')}"
            
            converted_data = {
                "instruction": f"The question is: {question} Choose the correct option",
                "input": options,
                "output": output
            }
            data_list.append(converted_data)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data_list, outfile, ensure_ascii=False, indent=2)

# 示例调用convert_jsonl_to_target_format函数
convert_jsonl_to_target_format('medqa_edited_train.jsonl', 'train.jsonl')
