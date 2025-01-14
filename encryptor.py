import hashlib

class NumberEncryptor:
    def __init__(self):
        
        pass

    def encrypt_number(self, input_data):
        # 숫자를 문자열로 변환하여 바이트로 인코딩
        if isinstance(input_data, tuple):
            input_data = ''.join(map(str, input_data))

        # 문자열을 바이트로 인코딩
        input_bytes = input_data.encode('utf-8')

        # SHA-256 해시 계산
        sha256_hash = hashlib.sha256(input_bytes).hexdigest()

        return sha256_hash
