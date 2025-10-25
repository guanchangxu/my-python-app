import json
import os

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class SecretManager:
    """管理应用密钥"""

    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "My Python App")
        self.secret_key = os.getenv("SECRET_KEY")
        self.debug = os.getenv("DEBUG", "False").lower() == "true"

    def validate_secrets(self):
        """验证必要的密钥是否存在"""
        if not self.secret_key:
            print("❌ SECRET_KEY 未设置")
            return False
        return True

    def get_config(self):
        """获取配置信息"""
        return {
            "app_name": self.app_name,
            "debug": self.debug,
            "secret_key_set": bool(self.secret_key),
        }


def format_message(message):
    """格式化消息"""
    if not message:
        return ""
    return message.strip().capitalize()


def calculate_stats(text):
    """计算文本统计信息"""
    if not text:
        return {}

    words = text.split()
    chars = len(text)
    word_count = len(words)
    avg_word_length = (
        round(sum(len(word) for word in words) / word_count, 2) if word_count > 0 else 0
    )

    return {
        "character_count": chars,
        "word_count": word_count,
        "average_word_length": avg_word_length,
    }


def process_data(data):
    """处理输入数据"""
    if not data:
        return {"error": "输入数据不能为空"}

    formatted_message = format_message(data)
    stats = calculate_stats(data)

    return {"original": data, "formatted": formatted_message, "stats": stats}


def main():
    """主应用入口"""
    print("=== Python 应用启动 ===")

    secret_manager = SecretManager()

    print("🔐 检查环境变量...")
    if not secret_manager.validate_secrets():
        print("请设置必要的环境变量")
        return

    config = secret_manager.get_config()
    print(f"🎯 应用配置: {json.dumps(config, indent=2, ensure_ascii=False)}")

    print("\n📝 开始数据处理演示:")
    print("输入一些文字，我会帮你格式化和统计")
    print("输入 'quit' 退出程序")
    print("-" * 40)

    while True:
        try:
            user_input = input("请输入文字: ")
            if user_input.lower() == "quit":
                print("👋 再见!")
                break

            result = process_data(user_input)
            print("📊 处理结果:")
            print(f"   原始文本: {result['original']}")
            print(f"   格式化后: {result['formatted']}")
            print(f"   字符数: {result['stats']['character_count']}")
            print(f"   单词数: {result['stats']['word_count']}")
            print(f"   平均单词长度: {result['stats']['average_word_length']}")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\n👋 用户中断，再见!")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    main()
