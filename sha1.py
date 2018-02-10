import hashlib
import itertools
dict = {
    'D35DB127DB631E6E27C6B75E8D376B04F64FAF83': 'root',
    'C2D24DCA38E9E862098B85BF0AB35CAA52803797': 'pma',
    '81101DED975D54BD76A3C8EAD293597AE9BB143F': 'Alice',
    '1FDB0D828172183735F1ED9E45E6AF3CE04DE9D1': 'Bob',
    '2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19': 'Carol',
    '6063C78456BB048BAF36BE1104D12D547834DFEA': 'David',
    'CE6B124C2F3D90CA4DEE06D35B81FF3A9A22EE32': 'Evan',
    'D5D82EF0B0A344A314E3B3E8D1E78A4697B97A53': 'Flynn',
}
for length in range(4,10):
    for plaintext in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=length):
        plaintext = ''.join(plaintext)
        inputBytes = str.encode(plaintext)
        hash1 = hashlib.sha1(inputBytes).digest()
        h2 = hashlib.sha1(hash1).hexdigest().upper()
        if dict.has_key(h2):
            print(inputBytes+' '+h2)