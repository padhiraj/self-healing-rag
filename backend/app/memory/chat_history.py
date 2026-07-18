from langchain_core.chat_history import InMemoryChatMessageHistory

# Store chat history for each user session
chat_store = {}


def get_chat_history(session_id: str) -> InMemoryChatMessageHistory:
    """
    Returns chat history for a session.
    Creates one if it doesn't exist.
    """
    if session_id not in chat_store:
        chat_store[session_id] = InMemoryChatMessageHistory()

    return chat_store[session_id]