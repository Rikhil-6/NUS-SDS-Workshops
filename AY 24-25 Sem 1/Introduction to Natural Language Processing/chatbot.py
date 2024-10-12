class chatbot:
    def __init__(self, sys_prompt):
        self.client = Groq()
        self.sys_prompt = sys_prompt

    def extract_response(self, response):
        pass

    def fetch_response(self, user_prompt):
        # use chat completion function and insert this here
        pass
