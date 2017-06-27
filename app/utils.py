def sha256(string):
    from hashlib import sha256
    return sha256(string.encode()).hexdigest()
