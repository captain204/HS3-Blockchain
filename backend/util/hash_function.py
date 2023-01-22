import hashlib
import json

def hash_function(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"hash-output('one', 2, [3]): {hash_function('one', 2, [3])}")
    print(f" hash-output(2, 'one', [3]): {hash_function(2, 'one', [3])}")

if __name__ == '__main__':
    main()
