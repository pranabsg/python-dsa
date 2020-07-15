"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.
Formula Used-
Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
"""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string) -> None:
        """Input a string that's stored in
        the table."""
        hash_val = self.calculate_hash_value(string)
        if hash_val != -1:
            if self.table[hash_val] is not None:
                self.table[hash_val].append(string)
            else:
                self.table[hash_val] = [string]
        self.table[hash_val] = [string]

    def lookup(self, string) -> int:
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_val = self.calculate_hash_value(string)
        if self.table[hash_val] is not None:
            return hash_val
        else:
            return -1

    @staticmethod
    def calculate_hash_value(string) -> int:
        """Helper function to calulate a
        hash value from a string."""
        first_char = string[0]
        second_char = string[1]
        hash_val = ord(first_char) * 100 + ord(second_char)
        return hash_val


def main():
    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    # Should be 8568
    print(hash_table.calculate_hash_value('UDACITY'))

    # Test lookup edge case
    # Should be -1
    print(hash_table.lookup('UDACITY'))

    # Test store
    hash_table.store('UDACITY')
    # Should be 8568
    print(hash_table.lookup('UDACITY'))

    # Test store edge case
    hash_table.store('UDACIOUS')
    # Should be 8568
    print(hash_table.lookup('UDACIOUS'))


if __name__ == '__main__':
    main()
