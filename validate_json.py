import json
import os

# 验证生成的JSON文件
def validate_json_file(file_path):
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误: 文件 {file_path} 不存在")
            return False
        
        # 读取文件大小
        file_size = os.path.getsize(file_path)
        print(f"文件大小: {file_size/1024:.2f} KB")
        
        # 验证JSON格式
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 检查数据类型
        if not isinstance(data, list):
            print(f"错误: 文件内容应该是JSON数组，实际类型: {type(data).__name__}")
            return False
        
        print(f"总共有 {len(data)} 个视频源")
        
        # 检查前3个元素的格式
        if len(data) > 0:
            print("\n前3个元素的格式检查:")
            for i, item in enumerate(data[:3]):
                print(f"\n元素 {i+1}:")
                required_fields = ['key', 'name', 'api', 'searchable', 'filterable', 'group', 'disabled', 'is_adult', 'detail']
                missing_fields = [field for field in required_fields if field not in item]
                
                if missing_fields:
                    print(f"  警告: 缺少字段 {missing_fields}")
                else:
                    print(f"  所有必需字段都存在")
                    print(f"  key: {item['key']}")
                    print(f"  name: {item['name']}")
                    print(f"  api: {item['api']}")
                    print(f"  searchable: {item['searchable']}")
                    print(f"  group: {item['group']}")
                    print(f"  disabled: {item['disabled']}")
        
        print("\n验证成功! JSON文件格式正确。")
        return True
        
    except json.JSONDecodeError as e:
        print(f"错误: JSON格式无效 - {e}")
        return False
    except Exception as e:
        print(f"验证过程中出错: {e}")
        return False

if __name__ == "__main__":
    output_file = "source-2025.11.20.json"
    validate_json_file(output_file)