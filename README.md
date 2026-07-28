# hello
description of files:
* `planner_demo.ipynb` creates a custom objective, creates a new adversary with that objective from the "everything bagel" adversary, and runs the operation with the look-ahead planner.
* `get_deploy_script.py` prints the script to deploy the Sandcat agent on a windows machine.
* `caldera_helper.py` constains helper functions (e.g. wrapper for HTTP requests) to interact with the caldera server.
* `8b160fd0-6323-412b-83b9-3a33e0f8fd1c.yml` is a copy of my custom "cheese ability", which is just an echo command. the other copy is in `caldera/plugins/stockpile/data/abilities/collection` of the caldera server.
* `custom_ability_demo.py` (old) is the minimum code to run the cheese ability. (create adversary+operation)
* `print_adversaries.py` (old) is self explanatory