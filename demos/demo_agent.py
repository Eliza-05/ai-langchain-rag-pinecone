from rag.rag_agent import build_rag_agent

def run_agent_demo_interactive() -> None:
    agent = build_rag_agent()

    print("\nINTERACTIVE AGENTIC RAG")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("> ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            break
        if not query:
            continue

        for event in agent.stream(
            {"messages": [{"role": "user", "content": query}]},
            stream_mode="values",
        ):
            event["messages"][-1].pretty_print()
