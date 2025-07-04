from openai import OpenAI
import os
from dotenv import load_dotenv
import re
from datetime import datetime
from typing import Optional

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def search_conference_website(conf_name: str, conf_acronym: str) -> Optional[str]:
    """
    Use gpt-4o-mini-search-preview to find the most likely URL for a given conference this year.
    """
    year = datetime.now().year
    completion = client.chat.completions.create(
        model="gpt-4o-mini-search-preview",
        web_search_options={
        "search_context_size": 'low',
        },
        messages=[{
            "role": "user",
            "content": f"Find me the {year} conference website for the {conf_name} ({conf_acronym})",
        }],
        
    )
    response_text = completion.choices[0].message.content
    
    # Get token usage
    token_usage = completion.usage
    print("Token usage:", token_usage)
    
    if response_text:
        url_match = re.search(r'https?://[^\s)]+', response_text)
        if url_match:
            return(url_match.group(0))
    return None




