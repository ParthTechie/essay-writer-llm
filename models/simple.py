import groq
from config.settings import GROQ_API_KEY, DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE

client = groq.Client(api_key=GROQ_API_KEY)

def generate_essay(prompt, model_name=DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE):
    """Simple essay generation function """
    formatted_prompt = f"""
    You are an expert essay writer. Write a comprehensive, well-structured essay on the following topic:
    
    Topic: {prompt}
    
    Your essay should include:
    - A clear introduction with a thesis statement
    - Well-developed body paragraphs with supporting evidence
    - A thoughtful conclusion
    - Proper transitions between paragraphs
    
    Make the essay engaging, informative, and approximately 1000-1500 words.
    """
    
    # Call API
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are an expert essay writer who creates well-structured, informative, and engaging essays."},
            {"role": "user", "content": formatted_prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    
    # Extract and return the essay
    return response.choices[0].message.content