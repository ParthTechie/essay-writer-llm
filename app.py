import streamlit as st
import time
from models.simple import generate_essay
from utils.helpers import timed_execution
from config.settings import DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS

def main():
    # Set up page configuration
    st.set_page_config(
        page_title="Essay Writer LLM",
        page_icon="📝",
        layout="wide",
    )
    
    # Title and introduction
    st.title("📝 Essay Writer LLM")
    st.subheader("Generate high-quality essays in seconds!")
    st.markdown(
        "This application uses advanced language models to generate essays based on your topic. "
        "Simply enter a topic and click 'Generate Essay'."
    )
    
    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        model = st.selectbox(
            "Model",
            ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"],
            index=0
        )
        
        max_tokens = st.slider(
            "Maximum Length",
            min_value=500,
            max_value=8000,
            value=DEFAULT_MAX_TOKENS,
            step=500,
            help="Maximum number of tokens in the generated essay"
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.1,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.1,
            help="Higher values make output more random, lower values more deterministic"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown(
            "Enter your essay topic and click Generate to create an essay."
        )
    
    # Main content area - essay generation
    topic = st.text_input("Essay Topic", placeholder="Enter your essay topic here...")
    
    # Generate button
    if st.button("Generate Essay", type="primary", disabled=not topic):
        if not topic:
            st.error("Please enter an essay topic.")
        else:
            # Display a spinner while generating
            with st.spinner(f"Generating essay on '{topic}'... This may take a minute."):
                try:
                    # Generate essay with timing
                    essay, generation_time = timed_execution(
                        generate_essay, 
                        topic,
                        model_name=model,
                        max_tokens=max_tokens,
                        temperature=temperature
                    )
                    
                    # Display metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Generation Time", f"{generation_time:.2f} seconds")
                    with col2:
                        st.metric("Word Count", len(essay.split()))
                    with col3:
                        st.metric("Character Count", len(essay))
                    
                    # Display the essay
                    st.subheader("Generated Essay")
                    st.markdown(essay)
                    
                    # Download button
                    st.download_button(
                        label="Download Essay",
                        data=essay,
                        file_name=f"{topic.replace(' ', '_').lower()}_essay.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"Error generating essay: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.caption("Essay Writer LLM | Powered by ParthTechie")

if __name__ == "__main__":
    main()