import pytest
import os
from app.main import SecretManager, process_data, format_message

class TestSecretManager:
    
    def test_secret_validation_success(self):
        """测试密钥验证成功"""
        # 设置环境变量
        os.environ['SECRET_KEY'] = 'test-secret-key'  # 注意是 environ，不是 env/ron
        os.environ['APP_NAME'] = 'Test App'
        
        manager = SecretManager()
        assert manager.validate_secrets() == True
        
        # 清理环境变量
        del os.environ['SECRET_KEY']
        del os.environ['APP_NAME']
    
    def test_secret_validation_failure(self):
        """测试密钥验证失败"""
        manager = SecretManager()
        assert manager.validate_secrets() == False

class TestProcessData:
    
    def test_process_data_success(self):
        """测试数据处理成功"""
        result = process_data("hello world")
        
        assert result['original'] == "hello world"
        assert result['formatted'] == "Hello world"
        assert result['stats']['word_count'] == 2  # 注意是 stats，不是 state
        assert result['stats']['character_count'] == 11
    
    def test_process_data_empty(self):
        """测试空数据处理"""
        result = process_data("")
        assert 'error' in result
        assert result['error'] == "输入数据不能为空"