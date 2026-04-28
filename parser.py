import re

def parse_smart_prompt(text):
    block_pattern = r"(?im)^[a-z]+\s+([\d\.]+)(?:[:\-]([\d\.]+))?\s*:\s*$"
    super_segments = text.split('|')

    parsed_segments = []

    for super_seg in super_segments:
        parts = re.split(block_pattern, super_seg)
        current_text = parts[0]

        if current_text.strip():
            parsed_segments.append(_extract_inline(current_text, None))

        # parts looks like: [text_before, val1, val2_opt, text_after, val1, val2_opt, text_after...]
        for i in range(1, len(parts), 3):
            val1 = float(parts[i])
            val2_str = parts[i+1]
            text_part = parts[i+2]

            # If it's a range like "Second 1-3:", weight is 3-1 = 2
            if val2_str is not None:
                weight = float(val2_str) - val1
            else:
                # If it's just "Second 1:", "Second 2:", we assume each step is an equal chunk
                # so base weight is 1.0, not the index itself!
                weight = 1.0

            parsed_segments.append(_extract_inline(text_part, weight))

    for seg in parsed_segments:
        if not seg["text"]:
            seg["text"] = " "

    return parsed_segments

def _extract_inline(text, default_weight):
    inline_pattern = r"\[([\d\.]+)(?:[:\-]([\d\.]+))?\]"
    match = re.search(inline_pattern, text)
    weight = 1.0
    if default_weight is not None:
        weight = default_weight

    if match:
        val1 = float(match.group(1))
        val2_str = match.group(2)
        if val2_str is not None:
            weight = float(val2_str) - val1
        else:
            weight = val1
        text = re.sub(inline_pattern, "", text)

    return {"text": text.strip(), "weight": weight}

