"""Utilities for cleaning text and names."""

def clean_name(raw):
    """Clean a name by removing extra spaces and converting it to title case."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
