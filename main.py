from genesis_ai_string_module import GenesisAIStringModule

strings = [
    "0123456789abcdef",
    "fedcba9876543210",
    "0000111122223333",
    "4444555566667777",
    "8888999900001111",
    "aaaabbbbccccdddd",
    "eeeeffffaaaabbbb",
    "ccccdddd00001111",
    "2222333344445555",
    "6666777788889999"
]

module = GenesisAIStringModule()
module.load_strings(strings)
results = module.process_strings(mode="operator")
polys = module.generate_polynomial_representations()
viz = module.visualize_results("./output")
print("Done.")