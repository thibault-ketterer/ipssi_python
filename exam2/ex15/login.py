from hashlib import md5


def compare_pass(given_pass):
    passw = "82771f9740d5e024ab823c12a9b51289"
    md5_val = md5(given_pass.encode('utf-8')).hexdigest()
    print("""md5 "ipssi": """, passw)
    print("""md5   pass : """, md5_val)
    if passw == md5_val:
        return True
    return False
