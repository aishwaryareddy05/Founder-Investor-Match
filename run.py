from utils.langgraph_matcher import app

if __name__ == "__main__":
    user_input = input("Describe your startup idea: ")
    result = app.invoke({"query": user_input})
    
    print("\n🔍 Top Matching Investors:\n")
    for r in result["matches"]:
        print(r["profile"])  # full formatted profile including name, score, and other details

    