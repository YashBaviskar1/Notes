import re

# Assume 'man_page_text' is a multiline string containing the htop manual
man_page_text = """
HTOP(1)                                             User Commands                                             HTOP(1)

NAME
       htop, pcp-htop - interactive process viewer

SYNOPSIS
       htop [-dCFhpustvH]
       pcp htop [-dCFhpustvH] [--host/-h host]

DESCRIPTION
       htop is a cross-platform ncurses-based process viewer.
...
"""

def parse_man_page_to_dict(text):
    """Parses a man page text into a dictionary of sections."""
    sections = {}
    current_section = None
    current_content = []
    
    # Pattern to identify section headers (e.g., NAME, SYNOPSIS, etc.)
    # It looks for lines that are fully uppercase, potentially with spaces.
    header_pattern = re.compile(r'^[A-Z][A-Z\s]+$')

    lines = text.strip().split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        # Check if the line is a section header
        if header_pattern.match(stripped_line) and len(stripped_line) > 1:
            # If we were already in a section, save its content
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            
            # Start a new section
            current_section = stripped_line
            current_content = []
        elif current_section:
            # If we are inside a section, append the line to its content
            current_content.append(line)
            
    # Don't forget to save the last section after the loop finishes
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
        
    return sections

# Run the parser
htop_sections = parse_man_page_to_dict(man_page_text)

# Print a part of the result to verify
import json
print(json.dumps({k: v[:200] + '...' for k, v in htop_sections.items()}, indent=2))