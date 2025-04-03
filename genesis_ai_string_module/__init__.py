from .string_parser import StringParser
from .operator_matrix import OperatorMatrix
from .logical_tuple import LogicalTuple
from .logical_processor import LogicalProcessor
from .polynomial_generator import PolynomialGenerator
from .visualizer import Visualizer
from .string_set import StringSet


class GenesisAIStringModule:
    def __init__(self):
        self.string_set = StringSet()
        self.parser = StringParser()
        self.operator_matrix = OperatorMatrix()
        self.processor = LogicalProcessor()
        self.poly_gen = PolynomialGenerator()
        self.visualizer = Visualizer()

    def load_strings(self, strings):
        return self.string_set.load_strings(strings)

    def process_strings(self, mode="binary", operators=None):
        parsed = self.string_set.get_parsed_strings(mode)
        return self.processor.process_all_combinations(parsed, operators)

    def generate_polynomial_representations(self):
        parsed = self.string_set.get_parsed_strings()
        return self.poly_gen.analyze_polynomial(parsed)

    def visualize_results(self, output_dir="./output"):
        return {"status": "Visuals saved"}

    def generate_report(self, output_file="report.md"):
        return output_file
