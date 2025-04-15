from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict
from agents.scorer import score_matches
from agents.query_builder import build_query
from agents.embedder import embed_query
from agents.matcher import match_investors


class MatchState(TypedDict):
    query: str
    embedding: List[float]
    raw_matches: List[Dict]
    matches: List[Dict]

graph = StateGraph(MatchState)

graph.add_node("query_builder", build_query)
graph.add_node("embedder", embed_query)
graph.add_node("matcher", match_investors)
graph.add_node("scorer", score_matches)


graph.set_entry_point("query_builder")
graph.add_edge("query_builder", "embedder")
graph.add_edge("embedder", "matcher")
graph.add_edge("matcher", "scorer")


app = graph.compile()
