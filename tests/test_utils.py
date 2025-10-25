from app.utils import welcome_message, check_text_length


def test_welcome_message():
    """测试欢迎消息函数"""
    result = welcome_message("关")
    assert result == "欢迎 关 使用我们的 Python 应用!"

    result = welcome_message("戮")
    assert "戮" in result


def test_check_text_length():
    """测试文本长度检查"""
    # 测试短文本
    is_ok, message = check_text_length("hello")
    assert is_ok == True
    assert "合适" in message

    # 测试长文本
    long_text = "a" * 150  # 创建150个字符的文本
    is_ok, message = check_text_length(long_text)
    assert is_ok == False
    assert "超过" in message
