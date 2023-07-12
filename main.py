import sys
import os
import WitInterface







if __name__ == '__main__':
    print("Aviya!!!!!!!!")
    print("Esther!!!!!🤩🤩🤩🤩")
    # TODO: handle edge cases (don't send args,  wrong path...)
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)