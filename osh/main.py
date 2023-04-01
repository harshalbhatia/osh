import os
import sys

from dotenv import load_dotenv

if os.path.isfile(os.path.expanduser('~/.osh_env')):
    load_dotenv(os.path.expanduser('~/.osh_env'))
else:
    print(
        "ERROR: Error loading env file. Please create a file at ~/.osh_env and add the following"
        " env variables: OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_API_BASE,"
        " OPENAI_API_VERSION, OPENAI_API_DEPLOYMENT_ID, CURRENT_MODEL.")
    sys.exit(1)

from osh.models import models

current_model = models.get(os.getenv("CURRENT_MODEL"))


def callCurrentModelWithData(input):
    # take even number of args, where every pair represents key value
    data = {}
    for i in range(0, len(input), 2):
        data.update({input[i]: input[i + 1]})
    print(current_model(data))


def main():
    if (len(sys.argv) >= 4) and ((len(sys.argv) - 1) % 2 == 0):
        callCurrentModelWithData(sys.argv[1:])
    else:
        print("Invalid number of arguments provided:" + str(len(sys.argv)))


if __name__ == "__main__":
    main()
