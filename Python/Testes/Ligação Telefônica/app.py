from twilio.rest import Client # quem fará a ligação

account_sid = 'ACd9ca8f4a3107f2284e740cf3b6e180cf'
auth_token = 'cb8a2aed74a486ddbd58daee0c844d5d'
numero_twilio = '+15074286420'
meu_numero = '+5562992844543'

client = Client(account_sid, auth_token)

mensagem ='''
Olá Paulo Victor, tudo bem?
Seja bem-vindo a Editora W!
Agradecemos a sua preferência.'''

ligacao = client.calls.create(twiml=f'<Response><Say language="pt-BR">{mensagem}</Say></Response>',to=meu_numero, from_=numero_twilio)

print(ligacao.sid)
