"""工具函数模块"""


def welcome_message(name):
    """生成欢迎消息"""
    return f"欢迎 {name} 使用我们的 Python 应用!"


def check_text_length(text, max_length=100):
    """检查文本长度"""
    if len(text) > max_length:
        return False, f"文本超过 {max_length} 字符限制"
    return True, "文本长度合适"
