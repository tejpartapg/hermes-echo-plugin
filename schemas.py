ECHO_TEXT_SCHEMA = {
    "name": "echo_text",
    "description": "Returns the supplied text unchanged. Use this tool when asked to echo or repeat text exactly.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The text to return unchanged."
            }
        },
        "required": ["text"]
    }
}
