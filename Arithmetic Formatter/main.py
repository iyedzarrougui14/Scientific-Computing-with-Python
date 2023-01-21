# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

problems = ["1+1", "2*3", "5/2", "5**2"]
print(arithmetic_arranger(problems, show_ans=True))
# Output:   1      + 1    = 2
#        ---

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(['-vv'])
