from reasoning import run_agent

def main():
    query = input("Ask me anything about stocks: ")
    response = run_agent(query)
    print(response)


if __name__ == "__main__":
    main()
