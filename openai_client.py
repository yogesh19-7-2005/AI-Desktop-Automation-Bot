from openai_client import client

command = '''
[9:04 PM, 1/8/2026] Sachin Ranila: Koi balk s esa jo Manish ki kl practical dede
[9:04 PM, 1/8/2026] ...: Bhai rohtak to koy na jaata
[9:05 PM, 1/8/2026] ...: Sachin bi dadri jaan laga ib        
[9:05 PM, 1/8/2026] ...: Navneet jaa s n
[9:05 PM, 1/8/2026] ...: Wo kise t de dega
[9:05 PM, 1/8/2026] ...: Anshul jaa h syd jangra
[9:05 PM, 1/8/2026] Sachin Ranila: Acha
[9:05 PM, 1/8/2026] ...: Hmm
[9:05 PM, 1/8/2026] ...: Number hoga uska ter p
[9:05 PM, 1/8/2026] Sachin Ranila: Ha s
[9:05 PM, 1/8/2026] ...: Thik h bhuj le usp
[9:05 PM, 1/8/2026] ...: Na to koy or btauga
'''

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You are yogesh, an Indian coder who speaks Hindi and English. "
                "You analyze WhatsApp chat history and reply naturally like yogesh."
            )
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

print(response.choices[0].message.content)
