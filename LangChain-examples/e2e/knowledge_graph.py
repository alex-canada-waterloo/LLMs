from pyvis.network import Network

# Define the triples
triples = [
    ("Output parsers", "are responsible for", "transforming LLM outputs to suitable formats"),
    ("Output parsers", "are useful for", "generating structured data with LLMs"),
    ("LangChain", "offers", "various types of output parsers"),
    ("LangChain OutputParsers", "support", "streaming"),
    ("OpenAITools", "pass", "tools to model"),
    ("OpenAIFunctions", "pass", "functions to model"),
    ("JSON Output Parser", "returns", "a JSON object as specified"),
    ("XML Output Parser", "returns", "a dictionary of tags"),
    ("CSV Output Parser", "returns", "a list of comma-separated values"),
    ("OutputFixingParser", "wraps", "another output parser"),
    ("OutputFixingParser", "calls", "an LLM to fix errors"),
    ("Pydantic Output Parser", "returns", "data in a user-defined Pydantic model format"),
    ("YAML Output Parser", "returns", "data in a user-defined Pydantic model format using YAML"),
    ("PandasDataFrame Output Parser", "is useful for", "operations with pandas DataFrames"),
    ("Enum Output Parser", "parses response into", "one of the provided enum values"),
    ("Datetime Output Parser", "parses response into", "a datetime string"),
    ("Structured Output Parser", "returns", "structured information"),
    ("Structured Output Parser", "is useful when", "working with smaller LLMs"),
]

# Create a PyVis Network
net = Network(height="800px", width="100%", notebook=True, directed=True)

# Add nodes and edges to the network
for subject, relation, obj in triples:
    net.add_node(subject, label=subject, shape="ellipse")
    net.add_node(obj, label=obj, shape="ellipse")
    net.add_edge(subject, obj, title=relation)

# Generate and display the network
net.set_options('''
var options = {
  "nodes": {
    "font": {
      "size": 16
    },
    "shape": "dot",
    "size": 20
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true
      }
    },
    "smooth": {
      "enabled": true,
      "type": "dynamic"
    }
  }
}
''')

# Save and show the visualization
net.show("knowledge_graph.html")
