# Mwanza Irrigation Data Collection Tool

This is a Streamlit app for collecting irrigation scheme data, connected to a Supabase backend.

## Setup

1. Create a Supabase project.
2. Create the `irrigation_data` table using the provided SQL.
3. Add row level security policies for anon insert/select.
4. Deploy this app on Streamlit Cloud.
5. Add your Supabase URL and anon key as secrets in Streamlit Cloud:

   ```
   [supabase]
   url = "your-supabase-url"
   key = "your-supabase-anon-key"
   ```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```