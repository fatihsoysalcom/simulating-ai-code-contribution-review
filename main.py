class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        """Processes the data by doubling each numeric item."""
        return [x * 2 for x in self.data if isinstance(x, (int, float))]

    def __str__(self):
        return f"DataProcessor with data: {self.data}"

# --- Simulated Pull Requests (Contributions) ---

# Human-authored contribution: Specific, concise, and adds clear value
def apply_human_pr(processor_instance):
    """
    Adds a feature to filter out negative numbers from the processor's data.
    This is a focused and clear enhancement, directly addressing a common need.
    """
    print("\n--- Human PR: Adding 'filter_non_positive' feature ---")
    original_data = list(processor_instance.data) # Make a copy for demonstration
    processor_instance.data = [x for x in processor_instance.data if x > 0]
    print(f"  Original data: {original_data}")
    print(f"  Data after human PR: {processor_instance.data}")
    return processor_instance

# AI-generated contribution (simulated): Generic, verbose, potentially redundant
def apply_ai_pr(processor_instance):
    """
    Simulates an AI-generated contribution. Often characterized by generic boilerplate,
    excessive comments, or slightly off-topic utility functions that look correct
    but lack specific project context.
    """
    print("\n--- AI PR: Adding 'get_data_summary_generic' utility ---")
    # This function might be overly verbose or not perfectly aligned
    # with the project's specific needs, but looks "correct" on the surface.
    def get_data_summary_generic(data_list):
        """
        Calculates a summary of the provided data list.
        This includes the total count, sum, and average of numeric items.
        Handles non-numeric items by skipping them.
        It is important to ensure data integrity.
        """
        numeric_items = [item for item in data_list if isinstance(item, (int, float))]
        if not numeric_items:
            # Explicitly handle empty list case, a common AI pattern
            return {"count": 0, "sum": 0, "average": 0}

        total_count = len(numeric_items)
        total_sum = sum(numeric_items)
        average_value = total_sum / total_count
        return {
            "count": total_count,
            "sum": total_sum,
            "average": average_value
        }

    # Attach this utility function to the processor instance for demonstration
    processor_instance.get_data_summary_generic = get_data_summary_generic
    print(f"  AI PR added 'get_data_summary_generic' method.")
    print(f"  Example summary: {processor_instance.get_data_summary_generic(processor_instance.data)}")
    return processor_instance

# --- Simulated Reviewer ---

def review_pull_request(pr_code_snippet: str, pr_type: str):
    """
    Simulates a reviewer's perspective, highlighting common AI-generated code characteristics.
    In a real scenario, this would involve static analysis, semantic checks, and human judgment.
    Here, we use simple keyword matching and verbosity checks.
    """
    print(f"\n--- Reviewing {pr_type} PR ---")
    issues_found = []

    # Check for excessive boilerplate/generic phrases, often seen in AI output
    generic_phrases = [
        "This function calculates",
        "Handles non-numeric items",
        "It is important to ensure",
        "This includes the total count"
    ]
    for phrase in generic_phrases:
        if phrase.lower() in pr_code_snippet.lower():
            issues_found.append(f"  - Potential boilerplate/generic phrase detected: '{phrase}'")

    # Check for overly verbose or redundant comments
    # AI often generates extensive comments, sometimes stating the obvious
    if pr_code_snippet.count('"""') > 1 and len(pr_code_snippet.split('"""')[1]) > 200: # Arbitrary length threshold for docstrings
        issues_found.append("  - Potentially overly verbose or generic docstring.")
    if pr_code_snippet.count('#') > 5: # Arbitrary threshold for inline comments
        issues_found.append("  - Many inline comments, some potentially redundant.")

    # Check for common AI patterns like overly explicit or redundant checks
    if "if not numeric_items:" in pr_code_snippet and "len(numeric_items)" in pr_code_snippet:
        issues_found.append("  - Redundant check for empty list before calculating length/sum.")

    if not issues_found:
        print("  ✅ PR appears concise and focused. No obvious AI-like patterns detected.")
    else:
        print("  ⚠️ Potential issues detected (common in AI-generated code):")
        for issue in issues_found:
            print(issue)
        # This line directly reflects the article's point about reviewer fatigue
        print("  Reviewer fatigue: This PR might require extra scrutiny due to generic patterns or verbosity.")

# --- Main execution ---
if __name__ == "__main__":
    initial_data = [1, 2, 3, -4, 5.5, "text"]
    my_processor = DataProcessor(initial_data)
    print(f"Initial Processor: {my_processor}")
    print(f"Processed data (initial): {my_processor.process()}")

    # Simulate Human PR and review it
    human_pr_code = """
def apply_human_pr(processor_instance):
    processor_instance.data = [x for x in processor_instance.data if x > 0]
    return processor_instance
    """
    my_processor_human = apply_human_pr(DataProcessor(initial_data)) # Apply to a fresh instance
    review_pull_request(human_pr_code, "Human")

    # Simulate AI PR and review it
    ai_pr_code = """
def apply_ai_pr(processor_instance):
    def get_data_summary_generic(data_list):
        """
        Calculates a summary of the provided data list.
        This includes the total count, sum, and average of numeric items.
        Handles non-numeric items by skipping them.
        It is important to ensure data integrity.
        """
        numeric_items = [item for item in data_list if isinstance(item, (int, float))]
        if not numeric_items:
            return {"count": 0, "sum": 0, "average": 0}
        total_count = len(numeric_items)
        total_sum = sum(numeric_items)
        average_value = total_sum / total_count
        return {
            "count": total_count,
            "sum": total_sum,
            "average": average_value
        }
    processor_instance.get_data_summary_generic = get_data_summary_generic
    return processor_instance
    """
    my_processor_ai = apply_ai_pr(DataProcessor(initial_data)) # Apply to a fresh instance
    review_pull_request(ai_pr_code, "AI")
