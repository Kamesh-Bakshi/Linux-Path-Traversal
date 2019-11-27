from pathtraversal import PathTraversal


if __name__ == "__main__":

    print("$​ <Starting your application...> ")
    Root = PathTraversal()

    while True:
        start = "$ "
        user_input = input(start)
        if user_input == "session clear":
            Root = PathTraversal()
            print("    SUCC: CLEARED: RESET TO ROOT")
            continue
        if user_input == "exit":
            break
        print(Root.execute(user_input))
