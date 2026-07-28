# hello
description of files:
* `test_objective.ipynb` creates a custom objective, creates a new adversary with that objective from the "everything bagel" adversary, and runs the operation with the look-ahead planner.
* `deploy_agent.py` prints the script to deploy the Sandcat agent on a windows machine.
* `request_caldera.py` constains helper functions (e.g. wrapper for HTTP requests) to interact with the caldera server.
* `8b160fd0-6323-412b-83b9-3a33e0f8fd1c.yml` is a copy of my custom "cheese ability", which is just an echo command. the other copy is in `caldera/plugins/stockpile/data/abilities/collection` of the caldera server.
* `cheese_operation.py` (old) is the minimum code to run the cheese ability. (create adversary+operation)
* `print_adversaries.py` (old) is self explanatory