from rag.rag_chain import build_rag_chain


def run_chain_demo():
    agent = build_rag_chain()

    query = "What is task decomposition?"
    for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()
