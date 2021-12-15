from ui.console import Console
from infrastructure.shape_repo import ShapeRepository
import tests
import data_examples


tests.run_all()
print("\n")
data_examples.run_all()
print("\n")

c = Console(ShapeRepository())
c.start()
