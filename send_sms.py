from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7966364dc66cb23c401ae1d3bd78028e"
# Your Auth Token from twilio.com/console
auth_token  = "4bf3599560bd1fa2f57486880a62bf15"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6581211012",
    from_="+12056196811",
    body="Hello from Python!")

print(message.sid)
