class StringParser:
    def validate_strings(self, strings):
        return all(isinstance(s, str) and len(s) == 16 for s in strings)

    def parse_string(self, string, mode="binary"):
        if mode == "binary":
            return [int(char, 16) for char in string]
        else:
            return [int(char, 16) for char in string]

    def parse_all_strings(self, strings, mode="binary"):
        return [self.parse_string(s, mode) for s in strings]
# Handles parsing and validation of sequences
