def format_output(output):
    """
    Format the output received from the inference model for better readability.
    
    Args:
        output: The output from the inference model.
    
    Returns:
        A formatted string representation of the output.
    """
    if isinstance(output, list):
        return "\n".join(map(str, output[:5]))  # Only show the first 5 results
    return str(output)  # Convert other types to string
