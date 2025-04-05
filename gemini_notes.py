# Install required package (Only first time)
pip install google-generativeai python-dotenv

import os
import google.generativeai as genai
from datetime import datetime

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def create_note(prompt):
    try:
        response = model.generate_content(prompt)
        
        # Create note content
        note_content = f"""# {datetime.now().strftime('%Y-%m-%d')} - Gemini Response

**Prompt:**  
{prompt}

**AI Response:**  
{response.text}

---

## My Thoughts:
<!-- Start writing here -->"""
        
        # Save to Obsidian
        filename = f"Gemini_Response_{datetime.now().strftime('%H%M%S')}.md"
        vault_path = os.getenv('OBSIDIAN_VAULT_PATH')
        
        with open(os.path.join(vault_path, filename), 'w') as f:
            f.write(note_content)
            
        print(f"Note created: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")
