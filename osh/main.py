import os
import sys
from osh.models import models
from dotenv import load_dotenv
load_dotenv()


current_model = models.get(os.getenv("CURRENT_MODEL"))


def callCurrentModelWithData(input):
    # take even number of args, where every pair represents key value
    data = {}
    for i in range(0, len(input), 2):
        data.update({input[i]: input[i+1]})
    print(current_model(data))


if __name__ == "__main__":
    if len(sys.argv) > 0:
        callCurrentModelWithData(sys.argv[1:])
